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



class Lke_parking():

    def __init__(self):

        def takeTicket(self, capacity):
        self.capacity = capacity
        tik_num = input("")

    def payForParking(self, tik_num):
        self.tik_num = tik_num




# create a function to run the garage
def showOptions():
        action = input("What would you like to do? " "\n \t 1.Take Ticket" "\n \t 2.Pay Ticket" "\n \t 3.Leave Garage" "\n \t 4.Quit")
        return action

showOptions()