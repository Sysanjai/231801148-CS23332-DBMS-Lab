import Sql.Airline as Airline
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="Magic@2005",database="airline")
cur=mycon.cursor()
def change_route():
    print(" - - - - - - - - - - - - - - - Modifying Routes And Pilots - - - - - - - - - - - - - - - ")
    print('\n')
    an=input("Do You Really Want To Change The Airroute Of The Flights ? ( Y / N ) ")
    if an.lower()=='y':
        print(" . . . . Entering Modifying Section . . . .")
        print("________________________________________________________________________________________________________________")
        a=cur.execute("select Flight_no,Airline_name,Pilot_name,Location1,Location2,depature_date,depature_time,ampm from flights where location1 is not null")
        l=['Flight Number','Airline Name','Pilot Name','Take off','Destination','Date','Time','Am or Pm']
        l1=[]
        res=cur.fetchall()
        print("\n")
        for i in res:
            for j in range(len(i)):
                print(l[j],': ',i[j])
                l1.append(i[0])
            print("___________________________________________________________________________________________________________________")
            print("\n")
        fno=int(input("Enter The Flight Number That You Want To Modify : "))
        print('\n')
        if fno in l1:
            print("Here Are The New Detalis That Are Required To Modify The Flight's Route :")
            print('\n')
            dp=str(input("Enter the  New Depature place: "))
            rt=str(input("Enter the New City that the flight travels: "))
            pn=str(input("Set a  New Pilot for the Flight: "))
            dt=input("Set the Date (YYYY-MM-DD) : ")
            tt=input("Set the Time (HH:MM  +12:00) : ")
            ap=input("AM or PM : ")
            sub=input("Submit to continue -> ")
            if sub.lower()=='submit':
                sql ="Update Flights set Location1=%s,Location2=%s,Pilot_name=%s,Depature_Date=%s,Depature_Time=%s,ampm=%s where Flight_no = %s"
                val =(dp,rt,pn,dt,tt,ap,fno)
                try:
                    cur.execute(sql,val)
                    mycon.commit()
                    print("The Details Are Updated and Modified")
                    print("Returning to Home Page")
                    Airline.airline()
                except:
                    mycon.rollback()
                    print("Sorry,Details Not Updated Due To Some Error")
                    ta=input("Want to Try again ( Y / N ):")
                    if ta.lower()=='y':
                        print("Re-directing to Modifying Section ")
            else:
                print("Details Not Updated . . .")
                print("Directing to Home Page")
                Airline.airline()
        else:
            print("Flight Not Found . . . Returning To Home Page ")
            Airline.airline()
    else:
        print("Directing to Home Page")
        Airline.airline()
                           