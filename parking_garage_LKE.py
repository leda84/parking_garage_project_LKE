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

class ParkingLot():

    def __init__(self):
        self.spaces = [1, 2, 3, 4, 5, 6]
        self.tickets = 0
        self.currentTicket = {}


    def takeTicket(self):
# This method will pop from spaces add to current ticket and print ticket number
        if self.tickets >= 6:
            print("There's no tickets available")
        else:
            print(f"Your ticket is {self.spaces[0]}")
            self.currentTicket[self.spaces[0]] = True
            self.spaces.pop(0)
            self.tickets += 1
            
garage = ParkingLot()
print(garage.spaces)
print(garage.tickets)
print(garage.currentTicket)
garage.takeTicket()
print(garage.spaces)
print(garage.tickets)
print(garage.currentTicket)
garage.takeTicket()
garage.takeTicket()
garage.takeTicket()
garage.takeTicket()
garage.takeTicket()
garage.takeTicket()
    # def payTicket(self):
# This method is going to check if there's a valid ticket number and also 

    # def leaveGarage(self):
        

# spaces = []
# if spaces < 6:
#     print("your ticket number is ")


# lke_parking =

# garage = ParkingLot([1,2,3,4,5,6,7,8,9,10])
# create a function to run the garage

# def showOptions():
    # while True:
    #    action = input("What would you like to do? " "\n \t Take Ticket" "\n \t Pay Ticket" "\n \t Leave Garage" "\n \t Quit" "\n")
        
        # if action.lower() == 'quit':
            # print("Thank you for visitng ")
            # break
        # elif action.lower() == 'take ticket':

        #     lke_parking.takeTicket()

        # elif lke_parking.lower() == 'pay ticket':
        #     lke_parking.payTicket()






