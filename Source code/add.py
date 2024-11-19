import mysql.connector
import random
import Airline
mycon=mysql.connector.connect(host="localhost",user="root",passwd="Magic@2005",database="airline")
cur=mycon.cursor()
def add():
    print('''               - - - - - - - Flight Additing Section - - - - - - - 

           ( Add New Flights ) ?
    -------------------------------------

    ''')
    a=str(input("Give Your Choice :"))
    if a.lower()=='add' or a.lower()=='add new flights' or a=='1' or a.lower()=='new flights':
        print(" Adding New Flight To Muthulakshmi Airlines")
        cn=str(input("Enter The Company Name Having Contract With Us :"))
        print("\n")
        if cn.lower()=='muthulakshmi airlines'or cn.lower()=='muthulakshmi':
            print("Congratulations, Glad To Say That Muthulakshmi Airlines Owning A New Flight")
            fn="Muthulakshmi Airlines"
        else:
            print("Congratulations",cn,"Company Having a Contract With Us and Adding A New Flight")
            fn=str(input("Enter Airline Name: "))
        
        def again():
            global st,fs,ss,ts
            st=int(input("Enter number of seats : "))
            fs=int(input("Enter number of first class seats: "))
            ss=int(input("Enter number of second class seats: "))
            ts=int(input("Enter number of third class seats: "))
            print('\n')
            while st!=(fs+ss+ts):
                again()
        again()
        if st>150:
            hs=15
        elif st>100:
            hs=10
        else:
            hs=8
        print("Number of Airhostess in the flight:",hs)
        a=random.randint(100,999)
        b=random.randint(100,999)
        con=str(input("Submit to add the flight: "))
        if con.lower()=='submit':
            
            fno=str(a)+str(b)
            print("The Flight Number is",fno)
            val=(fno,cn,fn)
            ins="insert into flights (Flight_no, Company_name, Airline_name) values ( %s, %s, %s )"
            try:
                cur.execute(ins,val)
                mycon.commit()
            except:
                mycon.rollback()
            vals=(fno,st,fs,ss,ts,hs)
            inst="insert into seats (Flight_no, No_of_seats, First_class, Second_class, Third_class, Airhostess) values ( %s, %s, %s, %s, %s, %s )"
            try:
                cur.execute(inst,vals)
                mycon.commit()
                print(fn,"Successfully added to our flights list")
            except:
                mycon.rollback()
                print("Flight not added")
            vals=(fno,st,fs,ss,ts)
            inst="insert into avl_seats (Flight_no,avl_tot_seats,avl_fst,avl_sec,avl_trd) values ( %s, %s, %s, %s, %s )"
            try:
                cur.execute(inst,vals)
                mycon.commit()
            except:
                mycon.rollback()
        else:
            print("Flight Not Added")
    else:
        print("No Action Taken")
        Airline()