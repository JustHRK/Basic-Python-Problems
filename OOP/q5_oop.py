#Write a class train which has method to book a ticket,get status (no. of seats) and get fare information of trains runnning under Indian Railways.

import random
class Train:
    def bookTicket(self):
        print("Your Ticket is Booked.")

    def getStatus(self):
        r=random.randint(1,100)
        print("Seats Remaining: ",r)

    def getFare(self,t):
        if(t==1):
            print("Fare: 200 Rs.") 
        elif(t==2):
            print("Fare: 270 Rs.")
        elif(t==3):
            print("Fare: 300 Rs.")   

t=Train()
t.bookTicket()
t.getStatus()
t.getFare(2)