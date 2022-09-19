# create a class for the customer
class Customer():
    bank_selection = ''

# making a constructor
    def __init__(self):
        pass

# making a function to return user inputs
    def user_inputs():
        down_payment = input('How much would you like to give as a down payment? \nPlease enter here: ')
        purchase_price = input('What is the value of the property you are trying to purchase? \nPlease enter here: ')
        repayment_time = input('How long do you need to repay the loan with interest? (in months) \nPlease enter here: ')
        bank_selection_input = input('What bank would you like to apply for a mortgage with? \nPlease enter here: ')

        Customer.bank_selection += bank_selection_input 

test1 = Customer
print(test1.user_inputs())
print(test1.bank_selection)