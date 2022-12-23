from enum import Enum

users = []


class Account(Enum):
    RUB = 'RUB'
    KZT = 'KZT'
    USD = 'USD'


class BankAccount:
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.account = Account
        self.total_amount = 0

    def create_user(self):
        self.name, self.surname = input('Enter your name and surname: ').split()
        acc = int(input('Enter your account type: \n 1 - KZT \n 2 - USD \n 3 - RUB\n'))
        if acc == 1:
            account = Account.KZT
        elif acc == 2:
            account = Account.USD
        elif acc == 3:
            account = Account.RUB
        else:
            print('Please enter a valid input')
        # users.append(BankAccount(self, self.name, self.surname, self.account))

    def remove_user(self):
        users.remove(BankAccount(self))

    def addToBankAccount(self):
        amount = float(input('Enter amount you want to top up: '))
        self.total_amount += amount

    def subtractFromBankAccount(self):
        amount = float(input('Enter amount you want to withdraw: '))
        if amount > self.total_amount:
            print('Insufficient amount')
        else:
            self.total_amount -= amount

    def toString(self):
        print(f'Dear {self.name} {self.surname}, your current balance is: {self.total_amount} {self.account}.')

    def moneyConversion(self):
        kzt_rub = 0.147
        kzt_usd = 0.0021
        rub_usd = 0.015
        rub_kzt = 6.78
        usd_kzt = 470
        usd_rub = 68
        to_cur = int(input('what currency do you want to convert: \n 1 - USD\n 2 - KZT\n 3 - RUB\n'))

        if self.account == Account.KZT:
            if to_cur == 1:
                self.total_amount = total_amount * kzt_usd
                print(f'You receive {total_amount:.2f} USD')
                self.account = Account.USD
            elif to_cur == 3:
                self.total_amount = total_amount * kzt_rub
                print(f'You receive {total_amount:.2f} RUB')
                self.account = Account.RUB
        elif self.account == Account.RUB:
            if to_cur == 1:
                self.total_amount = total_amount * rub_usd
                print(f'You receive {total_amount:.2f} USD')
                self.account = Account.USD
            elif to_cur == 2:
                self.total_amount = total_amount * rub_kzt
                print(f'You receive {total_amount:.2f} KZT')
                self.account = Account.KZT
        elif self.account == Account.USD:
            if to_cur == 2:
                self.total_amount = total_amount * usd_kzt
                print(f'You receive {total_amount:.2f} KZT')
                self.account = Account.KZT
            elif to_cur == 3:
                self.total_amount = total_amount * usd_rub
                print(f'You receive {total_amount:.2f} RUB')
                self.account = Account.RUB


# if __name__=main:
bank = BankAccount()

while True:
    input_value = int(input('Choose your operation:'
                            '\n 1 - Create user'
                            '\n 2 - Remove user'
                            '\n 3 - Display account information and balance'
                            '\n 4 - Top up balance'
                            '\n 5 - Withdraw from balance'
                            '\n 6 - Currency exchange\n'))
    if input_value == 1:
        bank.create_user()
    elif input_value == 2:
        bank.remove_user()
    elif input_value == 3:
        bank.toString()
    elif input_value == 4:
        bank.addToBankAccount()
    elif input_value == 5:
        bank.subtractFromBankAccount()
    elif input_value == 6:
        bank.moneyConversion()
    else:
        print('Please enter a valid input.')