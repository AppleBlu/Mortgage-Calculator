from time import sleep
class CustomerDatabase:
    customers = { 0: {'name': 'Dummy', 'surname': 'Joe', 'email': 'joe@dummy.com', 'phone': '00000000',
         'username': 'dummyjoe', 'password': 'dumbpass123'},
    }

    def register_customer():
        name = input("Please enter your name: ")
        surname = input("Please enter your surname: ")
        email = input("Please enter your email: ")
        phone = input("Please enter your phone: ")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        print("Registering customer... please, wait!")
        CustomerDatabase.customers[1] = {}
        CustomerDatabase.customers[1]['name'] = name
        CustomerDatabase.customers[1]['surname'] = surname
        CustomerDatabase.customers[1]['email'] = email
        CustomerDatabase.customers[1]['phone'] = phone
        CustomerDatabase.customers[1]['username'] = username
        CustomerDatabase.customers[1]['password'] = password
        sleep(5)
        print("Customer created. You may now login with your username and password.")
        print(CustomerDatabase.customers)