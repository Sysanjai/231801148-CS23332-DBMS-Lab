import random
import mysql.connector
import Airline
mycon=mysql.connector.connect(host="localhost",user="root",passwd="Magic@2005",database="airline")
cur=mycon.cursor()
def book():
    print("                            - - - - - - - - - - Booking Section - - - - - - - - - -                         ")
    print('\n')
    print("Book Your Tickets And Make Your Journey ♥")
    print('\n')
    st=int(input("Press 1 To Continue With The Journey :"))
    if st==1:
        print("        Book now        ")
        print('\n')
        sp=input("Take Off Place : ")
        dp=input("Your Destination : ")
        dt=input("Date Of Travel : ")
        val=(sp,dp,dt)
        q="Select Flight_no,Airline_name,Location1,location2,Depature_date,Depature_time,ampm from flights where location1=%s having location2=%s and depature_date=%s"
        tt=cur.execute(q,val)
        l=['Flight Number','Airline Name','Take off','Destination','Date','Time','Am or Pm']
        l1=[]
        res=cur.fetchall()
        print("\n")
        for i in res:
            for j in range(len(i)):
                print(l[j],': ',i[j])
                l1.append(i[0])
            print("___________________________________________________________________________________________________________________")
            print("\n")
        fno=int(input("Enter The Flight Number In Which You Want To Book Your Tickets: "))
        print('\n')
        if fno in l1:
            s="select A.flight_no,B.airline_name,A.no_of_seats,A.first_class,A.second_class,A.third_class from avl_seats A,Flights B where A.flight_no=B.flight_no having flight_no=%s"%fno
            a=cur.execute(s)
            l=['Flight Number','Airline Name','Total Seats','First Class Seats','Second Class Seats','Third Class Seats']
            re=cur.fetchall()
            ts=[]
            print("\n")
            for i in re:
                for j in range(len(i)):
                    print(l[j],': ',i[j])
                    ts.extend(i[2],i[3],i[4],i[5])
                print("___________________________________________________________________________________________________________________")
                print("\n")
                sb=int(input("Enter number of tickets want to be booked : "))
                p=[]
                for i in range(1,sb+1):
                    ps=input("Name of passenger",i,':')
                    p.append(ps)
                cl=input("Class in which you want to travel : ")
                if cl.lower()=='first class' and ts[1]>0:
                    print("Seats available to book on first class . .")
                    cn=input("Confirm to book tickets: ")
                    if cn.lower()=='confirm':
                        print("Tickets Booked")
                        ts[1]-=sb
                    else:
                        print("Ticket Not Booked")
                elif cl.lower()=='second class' and ts[2]>0:
                    if ts[1]==0:
                        print("As First class tickets are reserved..Try second class tickets")
                    cn=input("Confirm to book tickets: ")
                    if cn.lower()=='confirm':
                        print("Tickets Booked")
                        ts[2]-=sb
                    else:
                        print("Ticket Not Booked")
                elif cl.lower()=='third class' and ts[3]>0:
                    if ts[1]==0 and ts[2]==0:
                        print("Only third class seats are available for this trip ( First and Second Class tickets are already reserved)")
                    cn=input("Confirm to book tickets: ")
                    if cn.lower()=='confirm':
                        print("Tickets Booked")
                        ts[2]-=sb
                    else:
                        print("Ticket Not Booked")
                        Airline()
                    
                
                
             
        
        
        
