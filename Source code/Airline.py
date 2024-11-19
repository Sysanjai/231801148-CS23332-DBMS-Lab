import random
import Sql.change as change
import add
import route,checking, book, Airline,cancel
def airline():
    print('\n')
    print("           - - - - - - - - - - - - - - - - - Muthulakshmi Airlines - - - - - - - - - - - - - - - - -            ")
    print('\n')
    print("   - - - - - Over 10k+ Aeroplanes Runs Under Muthulakshmi Airlines With More Than 100M Passengers - - - - -      ")
    print("\n")
    print("Here are the services that are provided for the passengers:")
    print('''
    ___________________________________________________________________________________________________________________________

     1 • -- Ticket Booking -- •

     2 • -- Cancel Booking -- •
          
    ____________________________________________________________________________________________________________________________ 
      ''')
    print(" - - - - For Management Purposes - - - - ")
    print('''
    ___________________________________________________________________________________________________________________________

    1 •-- Add New Flights

    2 •-- New Air Route

    3 •-- Cancel Old Flights

    4 •-- Ticket Checking
          
    5 •-- Modify Route
    ____________________________________________________________________________________________________________________________

    Anything To Look Out For ?

    ''')
    ch=int(input(" Give Your Choice : "))
    if ch==1:
        print('''
        You Are Entering The Managing Sector Of Flights Of Muthulakshmi Airlines . . .
        ''')
        add.add()

    elif ch == 2:
        print(" - - - Adding new route to the flight - - - ")
        route()

    elif ch == 3:
        print(" - - - - Cancelling Old Flights - - - - ")
        cancel()

    elif ch == 4:
        print(" - - - - Checking Tickets whether available for the flights - - - -")
        checking()

    elif ch == 5:
        print(" - - - - Modifying the flight route - - - -")
        change()

    elif ch == 6:
        print(" - - - - You are now in passesgers section - - - -")
        print('\nNow what are your choices to do with it . . . . ')
        cho = int(input("Enter your choice : "))
        if cho == 1 : 
            print(" - - - - You are in the booking section - - - -")
            book()
        
          

Airline()
    
    
    
    
    
              
    
    
