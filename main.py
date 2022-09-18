import art
import banks
import customer

is_on = True

def user_choice():
    global is_on
    user_option = input("Do you want to continue?(yes/no): ")
    if user_option == 'yes':
        application()
    else:
        is_on = False

def application():
    while is_on:
        print(art.art)
        print("-------------------------------------------------")
        print("Please, choose the option")
        print("1. Available banks and rates")
        print("2. Calculate the mortgage")
        print("3. Contact support")
        print("4. Exit")
        print("-------------------------------------------------")

        customer_option = input("Enter your option here: ")

        if customer_option == '1':
            banks.Banks.__repr__()
            user_choice()
        elif customer_option == '2':
            pass
        elif customer_option == '3':
            pass
        elif customer_option == '4':
            print("Thank you and hope to see you soon!")
            exit()
        else:
            print("Wrong input")
            exit()


application()
