import Sql.Airline as Airline
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="Magic@2005",database="airline")
cur=mycon.cursor()
def cancel():
    
    print('''               - - - - - - - Flight Cancellation Section - - - - - - - 

           ( Cancel Flights ) ?
    -------------------------------------

    ''')
    a=str(input("Your Choice:"))
    if a.lower()=='cancel' or a.lower()=='cancel flights':
        print(" Cancelling Flights From Muthulakshmi Airlines")
        a=[]
        a=cur.execute("Select Flight_no,Company_name,Airline_name,Location1,Location2 from flights")
        res=a.fetchall()
        for i in res:
            print('\n')
            ls=[]
            for j in i:
                ls.append(j)
            print("Flight Number =",ls[0],"\nCompany Name=",ls[1],"\nAirline Name =",ls[2],"\nDepature =",ls[3],"\nDestination=",ls[4])
            print('____________________________________________________________________________________________________________________')
            print('\n')
            a.append(r[0])
        fno=int(input("Enter the Fligh Number That We Are Cancelling:"))
        if fno in a:
            print('\n')
            print("Getting details of the Flight . . . .")
            a="Select Flight_no,Company_name,Airline_name,Location1,Location2 from flights where Flight_no=%s"
            val=fno
            r=cur.execute(a,val)
            res1=r.fetchall()
            for i in res1:
                print('\n')
                ls=[]
                ls.append(i)
            print("Flight Number =",ls[0],"\nCompany Name=",ls[1],"\nAirline Name =",ls[2],"\nDepature =",ls[3],"\nDestination=",ls[4])
            print('____________________________________________________________________________________________________________________')
            print('\n')
            con=input("Confirm to cancel the flight ? :")
            if con.lower()=='confirm':
                rf=str(input("Reason why we are getting off of this flight:"))
                q="Delete from Flights where Flight_no = %s"%val
                q1="Delete from seats where Flights_no = %s"%val
                ex=cur.execute(q)
                ex1=cur.execute(q1)
                mycon.commit()
                print('''

                Submiting Details And ....

                Cancelling the Flight's Contract. . . .
                _________________________________________________________________________________________________________________________________

                Successfully Removed The Flight From Muthulakshmi Airlines
                _________________________________________________________________________________________________________________________________

                ''')
                print("Returning To Home Page ")
                Airline.airline()
            else:
                print("Flight Not Cancelled")
                Airline.airline()
            
    else:
        print("No Action Taken")
        print("Directing to Home Page")
        Airline.airline()
