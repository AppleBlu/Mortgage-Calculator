import art
import customer

is_on = True

def application():
    while is_on:
        print(art.art)
        print("-------------------------------------------------")
        print("Please, choose the option")
        print("1. Calculate the mortgage")
        print("2. Available banks and rates")
        print("3. Contact support")
        print("4. Exit")
        print("-------------------------------------------------")

        customer_option = input("Enter your option here: ")

        if customer_option == '1':
            pass
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