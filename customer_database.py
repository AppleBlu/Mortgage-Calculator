from time import sleep
import re

customers = { 0: {'name': 'Dummy', 'surname': 'Joe', 'email': 'joe@dummy.com', 'phone': '00000000',
         'username': 'dummyjoe', 'password': 'dumbpass123'},
    }

class CustomerDatabase:
    
    def register_customer():

        user_first_name = input("Please enter your name below \nFirst name: ")
        regex = re.search(r"^[a-zA-Z]+$", user_first_name)
        if not regex:
            print('First name should only contain letters. Please try again')
            exit()

        user_surname = input("Surname: ")
        regex = re.match(r"^[a-zA-Z]+$", user_surname)
        if not regex:
            print('Surname should only contain letters. Please try again')
            exit()

        user_email = input('Please enter your email below \nEmail: ')
        regex = re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', user_email)
        print('Checking email... Please wait!')
        sleep(2)
        if regex:
            print("Email valid")
        else:
            print('Invalid email address. Please try again')
            exit()
        
        user_number = input('Enter your phone number here: ')
        regex = re.match(r"^[0-9]{7,12}$", user_number)
        print('Checking phone number... Please wait!')
        sleep(2)
        if regex:
            print('Number valid')
        else:
            print('Invalid number. You should enter a number between 7 and 12 numbers long. Please try again')
            exit()

        username = input("Please enter your username: ")
        regex = re.search(r"^[a-zA-Z0-9\_]+$", username)
        if not regex:
            print('Username can not contain spaces but can containe underscores, numbers and letters. \nPlease try again.')
            exit()

        password = input("Please enter your password: ")
        regex = re.search(r"^[a-zA-Z0-9\_]+$", password)
        if not regex:
            print('Passwords can not contain spaces but can containe underscores, numbers and letters. \nPlease try again.')
            exit()

        #Cannot be two underscores, two hypens or two spaces in a row
#Cannot have a underscore, hypen or space at the start or end

        print("Registering customer... please, wait!")
        customers[1] = {}
        customers[1]['name'] = user_first_name
        customers[1]['surname'] = user_surname
        customers[1]['email'] = user_email
        customers[1]['phone'] = user_number
        customers[1]['username'] = username
        customers[1]['password'] = password
        sleep(5)
        print("Customer created. You may now login with your username and password.")
        print(customers)

login = CustomerDatabase.register_customer()
print(login)