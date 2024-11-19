import Sql.Airline as Airline
import mysql.connector
import book
mycon=mysql.connector.connect(host="localhost",user="root",passwd="Magic@2005",database="airline")
cur=mycon.cursor()
def cheking():
    print('\n')
    print("                         - - - - - - - - - Muthulakshmi Airlines - - - - - - - - -                         ")
    print('\n')
    print(" Checking Your Tickets . . . . ")
    print('\n')
    print(" - - - Tickets Available - - - ")
    ch = str(input("Continue with the booking process (y/n)?"))
    if ch == 'y':
        print('\nGetting Started With Your Booking')
        book()
    else:
        Airline()
    
    
