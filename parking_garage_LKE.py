# Group project for Week 2 Object Oriented Programming 
# Group members Laura, Kuda, Elias 
# Initial driver(Laura) 
# Laura contributed to a lot of the initial building 
# while the other members debugged We would all take turns driving 
# Through much googling and looking up different examples 
# we all contributed to the code and gave various inputs

class ParkingLot():

    def __init__(self):
        self.spaces = [1, 2, 3, 4, 5, 6]
        self.tickets = 0
        self.currentTicket = {}


    def takeTicket(self):
# This method will pop from spaces add to current ticket and print ticket number
        if self.tickets >= 6:
            print("Garage is full.")
        else:
            print(f"Your ticket number is {self.spaces[0]}")
            self.currentTicket[self.spaces[0]] = False #starts at False becasue it's unpaid
            self.spaces.pop(0)
            self.tickets += 1

            

    def payTicket(self):
#This method is going to check if there's a valid ticket number and also 
        while True:
            answer = input("Enter ticket number you would like to pay: (Enter 'quit') ")
            if answer.lower() == 'quit':
                break
            if int(answer) not in self.currentTicket.keys():
                print("Please enter a valid ticket number.")
                self.payTicket()
                break
        # this is going to be to check if the ticket is already paid, so that payment is not needed
        # if int(answer) in self.currentTicket and True:
        # print("This ticket has been paid. You can exit now.")
            elif self.currentTicket[int(answer)] == True:
                print("This ticket has already been paid for. Your 15 minutes to exit are running out.")
                break
            else:
                print("Thank you for paying. You have 15 minutes to exit garage.")
                self.currentTicket[int(answer)] = True
                self.spaces.append(int(answer))
                self.tickets -= 1
                break
            
    def exitGarage(self):
        while True:
            response = input("Ready to exit? Enter your ticket number: (Enter 'quit')")
            if response.lower() == 'quit':
                break
            if int(response) not in self.currentTicket.keys():
                print("Please enter a valid ticket number. ")
        #we need to check if it's paid by checking if it's true
        #if it's false then they have to pay ticket
            elif self.currentTicket[int(response)] == False:
                print("Please pay your ticket to exit. ")
                self.payTicket()
        #if it's true(paid) then they can leave 
            else:
                print("Thank you, have a nice day!")
                self.currentTicket.pop(int(response))
                break


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