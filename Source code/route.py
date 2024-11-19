import mysql.connector
import Airline as airline
mycon=mysql.connector.connect(host="localhost",user="root",passwd="Magic@2005",database="airline")
cur=mycon.cursor()
def airroute():
    print("            - - - - - - - - - Fly High Our Flights With New Routes - - - - - - - - - ")
    print('\n')
    print("Set New Routes To Our New Flights . . . .")
    print('\n')
    print("Sure that you are going to set the route for the flights ")
    ans=str(input("(Y/N)?"))
    print('\n')
    if ans.lower()=='y':
        r=[]
        a=cur.execute("select Flight_no,Airline_name,location1 from flights where location1 is null")
        rr=cur.fetchall()
        print("The Flights With No Routes are . . .")
        for i in rr:
            ls=[]
            for j in i:
                ls.append(j)
            print("Flight Number =",ls[0],"\nAirline Name =",ls[1],"\nDepature =",ls[2])
            print('____________________________________________________________________________________________________________________')
            print('\n')
            r.append(i[0])
        print('\n')
        fno=int(input("Enter The Flight Number That You Want To Set Route: "))
        if fno in r:
            dp=str(input("Enter the depature place: "))
            rt=str(input("Enter the city that the flight travels: "))
            pn=str(input("Set a Pilot for the Flight: "))
            dt=input("Set the Date (YYYY-MM-DD) : ")
            tt=input("Set the Time (HH:MM  +12:00) : ")
            ap=input("AM or PM : ")
            sql ="Update Flights set Location1=%s,Location2=%s,Pilot_name=%s,Depature_Date=%s,Depature_Time=%s,ampm=%s where Flight_no = %s"
            val =(dp,rt,pn,dt,tt,ap,fno)
            try:
                cur.execute(sql,val)
                mycon.commit()
                print("Details are updated .")
            except:
                mycon.rollback()
                print("Value Not Inserted")
        else:
            print("Flight Not Found")
            ans=str(input("Press 1 to Re-enter the page :"))
            if ans==1:
                print("Re-directing to Route Setting page . . .")
                airroute()
            else:
                print("Directing to Home Page")
                airline()
    else:
        print("Invalid Option")
        print("Directing to Home Page . . . . .")
        print('\n')
        airline()
