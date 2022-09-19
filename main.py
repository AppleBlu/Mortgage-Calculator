import banks
# import customer
import customer_database
import art
from time import sleep

is_on = True


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
        print("-------------------------------------------------")
        print("Please, choose the option")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print("-------------------------------------------------")
        customer_option_one = input("Enter your option here: ")

        if customer_option_one == '1':
            customer_database.CustomerDatabase.register_customer()
            print("Taking you back to the main menu...")
            sleep(3)
            initial_screen()
        elif customer_option_one == '2':
            application()
        elif customer_option_one == '3':
            print("Thank you and hope to see you soon!")
            exit()
        else:
            print("Wrong input")
            user_choice_initial()


def application():
    print(art.art)
    print("-------------------------------------------------")
    print("Please, choose the option")
    print("1. Available banks and rates")
    print("2. Calculate the mortgage")
    print("3. Contact support")
    print("4. Exit")
    print("-------------------------------------------------")
    customer_option_two = input("Enter your option here: ")

    if customer_option_two == '1':
        banks.Banks.__repr__()
        user_choice_application()
    elif customer_option_two == '2':
        pass
    elif customer_option_two == '3':
        pass
    elif customer_option_two == '4':
        print("Thank you and hope to see you soon!")
        exit()
    else:
        print("Wrong input")
        user_choice_application()


initial_screen()
