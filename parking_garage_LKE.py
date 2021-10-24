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
            print("Garage is full")
        else:
            print(f"Your ticket number is {self.spaces[0]}")
            self.currentTicket[self.spaces[0]] = False #starts at False becasue it's unpaid
            self.spaces.pop(0)
            self.tickets += 1
            

    def payTicket(self):
#This method is going to check if there's a valid ticket number and also 
        answer = input("Enter ticket number you would like to pay: ")
        if int(answer) not in self.currentTicket.keys():
            print("Please enter a valid ticket number")
            self.payTicket()
        # this is going to be to check if the ticket is already paid, so that payment is not needed
        #if int(answer) in self.currentTicket and True:
            #print("This ticket has been paid. You can exit now.")
        elif self.currentTicket[int(answer)] == True:
            print("This ticket has already been paid for. You can head to garage exit now.")
            #might not want to make it send to exitGarage depending in function that will run this
            self.exitGarage()
        else:
            print("Thank you for paying. You can exit garage now.")
            self.currentTicket[int(answer)] = True
            self.spaces.append(int(answer))
            self.tickets -= 1
            #might not want to make it send to exitGarage depending in function that will run this
            self.exitGarage()
            
    def exitGarage(self):
        response = input("Ready to exit? Enter your ticket number: ")
        if int(response) not in self.currentTicket.keys():
            print("Please enter a valid ticket number")
        #we need to check if it's paid by checking if it's true
        #if it's false then they have to pay ticket
        elif self.currentTicket[int(response)] == False:
            print("Please pay your ticket to exit. ")
            self.payTicket()
        #if it's true(paid) then they can leave 
        else:
            print("Have a nice day!")
            self.currentTicket[int(response)] = False


#test runs:
# garage = ParkingLot()
# print(garage.spaces)
# print(garage.tickets)
# print(garage.currentTicket)
# garage.takeTicket()
# print(garage.spaces)
# print(garage.tickets)
# print(garage.currentTicket)
# garage.takeTicket()
# garage.takeTicket()
# garage.takeTicket()
# garage.takeTicket()
# garage.takeTicket()
# garage.takeTicket()
# print(garage.currentTicket)
# garage.payTicket()



lke_parking = ParkingLot() 

# created a function to run the garage

def showOptions():
    while True:
        action = input("What would you like to do? " "\n \t Take Ticket" "\n \t Pay Ticket" "\n \t Exit Garage" "\n \t Quit" "\n")
        
        if action.lower() == 'quit':
            print("Thank you for visiting ")
            break
        elif action.lower() == 'take ticket':
            lke_parking.takeTicket()

        elif action.lower() == 'pay ticket':
            lke_parking.payTicket()

        elif action.lower() == 'exit garage':
            lke_parking.exitGarage()

showOptions()