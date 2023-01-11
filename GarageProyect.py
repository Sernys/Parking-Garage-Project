#
# Parking Garage Project
# Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). 
class ParkingGarage():
# You will need a few attributes as well:
    ticket = []#-tickets -> list
    parkin_space = []#-parkingSpaces -> list
    client_info = []#store the client information 
    current_ticket = dict(ticket,client_info)#-currentTicket -> dictionary
    def __init__(self,owner_name,vehicle_brand,model,plate,year,payment):
        self.owner_name = owner_name
        self.vehicle_brand = vehicle_brand
        self.model = model
        self.plate = plate
        self.year = year
        self.payment = payment
        self.tickets = 10
        self.parking_spot = 10
        
# Your parking gargage class should have the following methods:
    def takeTicket(self):
        ticket_name = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1']#to give a ramdom name to each to the tickets
        print('Welcome to the Parking Grage')
        p_access = input('Do you like yo access our parking services:\n -Yes\n-No\n')
        if p_access.lower() == 'yes':
            while True:
                self.current_ticket -= 1 #This should decrease the amount of tickets available by 1
                self.parking_spot -=1  #This should decrease the amount of parkingSpaces available by 1
                if self.current_ticket == 0 or self.parking_spot == 0:
                    print('Thanks for choosing our Parking unfortunate, we ran out of spot at the moment come back another time!')
                    break
                if  self.current_ticket != 0 or self.parking_spot != 0:
                    self.owner_name = input('Enter the name of the registered with the vehicle:\n')
                    self.vehicle_brand = input('Enter the brand of the veicle:\n')
                    self.model = input('Enter the vehicle model:\n')
                    while True:
                        self.plate = input('Enter the plate regtistered with the vehicle:\n')
                        if len(self.plate) < 0 :
                            return 'You must enter a valid plate to proceed to the parking'
                        elif len(self.plate) > 7 :
                            return 'Error: Vehicle plate have only 7 character,Try again'
                        else:
                            break
                    self.year = input("Enter the Year of the vehicle:\n")
        else:
            print('Have a Nice day,come back soon!!')
            

# - payForParking   
#    - This should update the "currentTicket" dictionary key "paid" to True
    def payForParking(self):
        self.payment = 10
        pay = input('Enter the amount to pay:\n') #Display an input that waits for an amount from the user and store it in a variable 
        if pay == self.payment:#display a message to the user that their ticket has been paid and they have 15mins to leave
            return 'Ticket has been paid full you have 15 min to leave the parking'
        elif pay != self.payment:
            return 'Please Enter the amount to pay before you leave the parking!!'     
 # -leaveGarage
    def leaveGarage(self):
        self.ticket += 1#Update parkingSpaces list to increase by 1
        self.parking_spot +=1#Update tickets list to increase by 1
        if self.current_ticket == True: #If the ticket has been paid, display a message of "Thank You, have a nice day"
            return 'Thank you, have a nice day'#Once paid, display message "Thank you, have a nice day!"
        elif self.current_ticket == False:
            self.payForParking()# If the ticket has not been paid, display an input prompt for payment
            

