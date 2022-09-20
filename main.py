import banks
import customer_database
import customer
import calculator
import art
from time import sleep
import sys
import time

is_on = True

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

# creating a function that types out strings super fast instead of printing them
def type_super_fast(str):
    for letter in str:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.03)
    print('\n')

def user_choice_application():
    user_option = input("Do you want to continue?(yes/no): ")
    if user_option == 'yes':
        application()
    else:
        exit()

def user_choice_initial():
    user_option = input("Let's try again?(yes/no): ")
    if user_option == 'yes':
        initial_screen()
    else:
        exit()

def initial_screen():
    while is_on:
        print(art.art)
        type_super_fast("--------------------------------------------------")
        type_fast("Please, choose the option")
        type_fast("1. Register")
        type_fast("2. Login")
        type_fast("3. Exit")
        type_super_fast("--------------------------------------------------")
        customer_option_one = input("Enter your option here: ")

        if customer_option_one == '1':
            customer_database.CustomerDatabase.register_customer()
            type_fast("Taking you back to the main menu...")
            sleep(3)
            initial_screen()
        elif customer_option_one == '2':
            application()
        elif customer_option_one == '3':
            type_fast("Thank you and hope to see you soon!")
            exit()
        else:
            type_fast("Wrong input")
            user_choice_initial()


def application():
    print(art.art)
    type_super_fast("--------------------------------------------------")
    type_fast("Please, choose the option you would like to proceed with")
    type_fast("1. Available banks and rates")
    type_fast("2. Calculate the mortgage")
    type_fast("3. Contact support")
    type_fast("4. Exit")
    type_super_fast("--------------------------------------------------")
    customer_option_two = input("Enter your option here: ")

    if customer_option_two == '1':
        banks.Banks.__repr__()
        user_choice_application()
    elif customer_option_two == '2':
        customer.Customer.user_inputs()
        print('\n')
        type_fast('The loan you would recive is:')
        type_fast('£' + str(customer.Customer.loan_amount))
        type_fast('What you would have to repay with interest is:')
        type_fast('£' + str(customer.Customer.loan_with_interest))
        type_fast(customer.Customer.interest_rate)
        #calculator.Calculator.calculate()
        #type_fast('The interest is')
        user_choice_application()
    elif customer_option_two == '3':
        pass
    elif customer_option_two == '4':
        type_fast("Thank you and hope to see you soon!")
        exit()
    else:
        type_fast("Wrong input")
        user_choice_application()

initial_screen()
