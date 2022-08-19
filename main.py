class Rentalsystem:
    def rent(self):
        print("\nWelcome to our Rental System")
        self.operation = int(input(''' Please type a operation you would like to complete:
        1 for Add Customer
        2 for Add Rental booking
        3 for See Customer list
        4 for See Rental booking list
        5 for See Inventory of vehicles available
        
        Enter your choice: '''))
        self.a = {'bikes': 2, 'cycle': 3, 'car': 1, 'boat': 2}
        self.b = {'Sameer Sayed': 'Kalyan', 'Nitin': 'Pawai'}  # customer name, address,
        self.c = {'Sameer Sayed': 'Car', 'Nitin Pandey': 'Bike','Karan Dubey':'Boat'}
        if self.operation == 1:
            print('add Customer')
            self.b.update({input("Enter name: "):input("Enter address: ")})
            print(self.b)
        elif self.operation == 2:
            print('Add Rental booking')
            self.c.update({input("Enter name: "):input("Enter Vehicle name: ")})
            print(self.c)
        elif self.operation == 3:
            print('Customer list')
            print(self.b)
        elif self.operation == 4:
            print('Rental booking list')
            return self.c
        elif self.operation == 5:
            print('Inventory of vehicles available')
            print(self.a)
        else:
            print("You Press a Invalid Key")

class Again(Rentalsystem):
    def again(self):
        x = Rentalsystem()
        print(x.rent())
        cal_again = input('''
        Do you want to see options again?
        Please type y for YES or n for NO.
        ''')

        if cal_again == 'y':
            a = Rentalsystem()
            print(a.rent())
        elif cal_again == 'n':
            print("See You Later")
        else:
            print('Invalid key')
            b = Again()
            print(b.again())

b = Again()
b.again()

