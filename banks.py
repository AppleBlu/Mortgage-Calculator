from time import sleep
import random
import customer

class Banks:

    available_banks = {
        "HSBC Holdings": 0.4,
        "Lloyds Banking Group": 0.4,
        "NatWest Group": 0.5,
        "Barclays": 0.3
    }

    def __repr__():
        print("{:<26} {:<15}".format('Bank','Interest Rate'))
        print('----------------------------------------')
        for key, value in Banks.available_banks.items():
            value = str(value) + '%'
            print("{:<26} {:<15}".format(key, value))

    def contact_support(message):
        # message = input("Please, enter your message: ")
        ticket_number = random.randint(10000,30000)
        delay = 2
        ticket_delay = 4

        print("The following information is being sent to the bank:")
        print("----------------------------------------------------")
        print("Name: " + name)
        print("Surname: " + surname)
        print("Email: " + email)
        print("Phone number: " + phone)
        print("Message: " + message)
        print("----------------------------------------------------")
        print("Please, wait while we process the information.......")
        sleep(delay)
        print("Message sent!")
        print("Please, wait while we create a support ticket.......")
        sleep(ticket_delay)
        print("Support ticket created")
        print("----------------------------------------------------")
        print("Support ticket #" + str(ticket_number))
        print("Name: " + name)
        print("Surname: " + surname)
        print("Email: " + email)
        print("Phone number: " + phone)
        print("Message: " + message)
        print("----------------------------------------------------")
        print("Our staff is going to contact you as soon as we can. Thank you for contacting us!")