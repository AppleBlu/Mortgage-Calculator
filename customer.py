# create a class for the customer
from collections import UserDict
import banks


class Customer():
    user_dict = {}
    loan_amount = 0
    interest_rate = 0
    loan_with_interest = 0
    

# making a function to return user inputs
    def user_inputs():
        down_payment = input('How much would you like to give as a down payment? \nPlease enter here: ')
        purchase_price = input('What is the value of the property you are trying to purchase? \nPlease enter here: ')
        repayment_time = input('How long do you need to repay the loan with interest? (in months) \nPlease enter here: ')
        bank_selection_input = input('What bank would you like to apply for a mortgage with? \nPlease enter here: ')

        Customer.user_dict['down_payment'] = down_payment
        Customer.user_dict['purchase_price'] = purchase_price
        Customer.user_dict['repayment_time'] = repayment_time
        Customer.user_dict['bank_selection'] = bank_selection_input

        repayment_time_int = int(repayment_time)
        Customer.loan_amount = int(purchase_price) - int(down_payment)
        Customer.interest_rate = repayment_time_int * banks.Banks.available_banks.get(bank_selection_input)
        Customer.loan_with_interest = Customer.interest_rate * Customer.loan_amount


# test1 = Customer