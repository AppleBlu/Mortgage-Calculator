class Banks:

    available_banks = {
        "HSBC Holdings": 4,
        "Lloyds Banking Group": 4,
        "NatWest Group": 5,
        "Barclays": 3
    }

    def __init__(self):
        pass


    def __repr__():
        print("{:<26} {:<15}".format('Bank','Interest Rate'))
        print('----------------------------------------')
        for key, value in Banks.available_banks.items():
            value = str(value) + '%'
            print("{:<26} {:<15}".format(key, value))
