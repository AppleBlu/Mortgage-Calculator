# importing modules
import customer
import banks

# creating a class called calculator
class Calculator():
    rt = customer.Customer.reypayment_time
    pp = customer.Customer.purchase_price
    dp = customer.Customer.down_payment
    bs = customer.Customer.bank_selection

# creating a constructor for class Calculator():
    def __init__():
        pass

    def get_interest():
        banks_interest = banks.Banks.available_banks.get(Calculator.bs)
        print(banks_interest)


test1 = Calculator

print(test1.get_interest())