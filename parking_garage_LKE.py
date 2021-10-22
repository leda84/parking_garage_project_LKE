#Your parking gargage class should have the following methods:
# takeTicket
#- This should increase the number of tickets sold by 1
#- This should decrease the amount of parkingSpaces available by 1
#- Add the ticket to the currentTicket dictionary with False(for unpaid)

#payForParking
#- Display an input that waits for an amount from the user and store it in a variable
#- Display a message to the user that their ticket has been paid and they have 15mins to leave
#- This should update the "currentTicket" dictionary key "paid" to True

#leaveGarage
#- If the ticket has not been paid, display an input prompt for payment
#- If the ticket has been paid, display a message of "Thank You, have a nice day"
#- Update parkingSpaces list to increase availability by 1 

#You will need a few attributes as well:
#- tickets (sold) -> integer(counter of sorts)
#- parkingSpaces -> list
#- currentTicket (is ticket paid?) -> dictionary

dict = 



# class Lke_parking():

    def __init__(self, capacity, spaces, ):
        self.capacity = capacity
        self.spaces = spaces


a
    def takeTicket(self, capacity):
         print("Your ticket is..")

    def payForParking(self, tik_num):
        self.tik_num = tik_num



# spaces = []
# if spaces < 6:
#     print("your ticket number is ")






# create a function to run the garage
def showOptions():
        action = input("What would you like to do? " "\n \t 1.Take Ticket" "\n \t 2.Pay Ticket" "\n \t 3.Leave Garage" "\n \t 4.Quit" "\n")
        return action

showOptions()