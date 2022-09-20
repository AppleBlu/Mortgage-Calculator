from time import sleep
import time 
import sys
import re

customers = {0: {'name': 'Dummy', 'surname': 'Joe', 'email': 'joe@dummy.com', 'phone': '00000000',
                 'username': 'dummyjoe', 'password': 'dumbpass123'},
             }

# creating a function that types out strings slow instead of printing them
def type_slow(str):
    for letter in str:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print('\n')
 
# creating a function that types out strings fast instead of printing them
def type_fast(str):
    for letter in str:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    print('\n')
    
class CustomerDatabase:

    def register_customer():

        user_first_name = input("Please enter your name below \nFirst name: ")
        regex = re.search(r"^[a-zA-Z]+$", user_first_name)
        if not regex:
            type_fast('First name should only contain letters. Please try again')
            sleep(2)
            exit()

        user_surname = input("Surname: ")
        regex = re.match(r"^[a-zA-Z]+$", user_surname)
        if not regex:
            type_fast('Surname should only contain letters. Please try again')
            sleep(2)
            exit()

        user_email = input('Please enter your email below \nEmail: ')
        regex = re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', user_email)
        type_slow('Checking email...')
        sleep(3)

        if regex:
            type_fast("Email valid")
        else:
            type_fast('Invalid email address. Please try again')
            sleep(2)
            exit()

        user_number = input('Enter your phone number here: ')
        regex = re.match(r"^[0-9]{7,12}$", user_number)
        type_slow('Checking phone number...')
        sleep(3)
        
        if regex:
            type_fast('Number valid')
        else:
            type_fast('Invalid number. You should enter a number between 7 and 12 numbers long. Please try again')
            sleep(2)
            exit()

        username = input("Please enter your username: ")
        regex = re.search(r"^[a-zA-Z0-9\_]+$", username)
        if not regex:
            type_fast('Username can not contain spaces but can containe underscores, numbers and letters. \nPlease try again.')
            sleep(2)
            exit()

        password = input("Please enter your password below \nPassword: ")
        regex = re.search(r"^[a-zA-Z0-9\_]+$", password)
        if not regex:
            type_fast('Passwords can not contain spaces but can containe underscores, numbers and letters. \nPlease try again.')
            sleep(2)
            exit()

        confirm_password = input('Confirm password: ')
        type_slow('Checking password...')
        sleep(3)
        if confirm_password == password:
            type_fast('Password match!')
        else:
            type_fast('Your password does not match. \nPlease try again.')
            sleep(2)
            exit()

        type_slow('We are registering you...')
        type_slow('Please wait!')
        sleep(2)
        type_slow('Please wait!')
        customers[1] = {}
        customers[1]['name'] = user_first_name
        customers[1]['surname'] = user_surname
        customers[1]['email'] = user_email
        customers[1]['phone'] = user_number
        customers[1]['username'] = username
        customers[1]['password'] = password
        sleep(4)
        type_fast("Customer created. You may now login with your username and password.")

# tests
# test1 = CustomerDatabase

# print(test1.register_customer())