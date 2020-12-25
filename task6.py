class Bank:
    def __init__(self, code, address):
        self.code = code
        self.address = address
       
    def manages(self):
        return (f'Manages Bnak with ID {code} at {address}')
   
    def mantains(self, booth=None):
        if booth != None:
            return (f'mantains ATM at {booth.location}')
   
class ATM:
    def __init__(self, location, managedby):
        self.location = location
        self.managedby = managedby
       
    def identifies(self):
        return f"Managed by {self.managedby}"
   
    def transactions(self, tr):
        print(f'Transaction in {self.location} details:')
        print(tr)

class Customer:
    def __init__(self, name, address, dob, card_num, pin):
        self.name = name
        self.address = address
        self.dob = dob
        self.card_num = card_num
        self.pin = pin
   
    def verify_pass(self, pin):
        if self.pin == pin:
            return True
        return False

class Account:
    def __init__(self, customer, number, balance):
        self.customer = customer
        self.number = number
        self.balance = balance
       
    def deposit(self, amount):
        self.balance += amount
   
    def withdraw(self, amount):
        self.balance -= amount
       
    def createTransaction(self, amount):
        self.balance -= amount
       
       
class CurAcc(Account):
    def __init__(self, customer, number, balance):
        super(customer, number, balance)
       
class SavingAcc(Account):
    def __init__(self, customer, number, balance):
        super(customer, number, balance)
       
class ATM_Transactions:
    def __init__(self, tid, date, ttype, amount, post_bal):
        self.tid = tid
        self. date = date
        self.ttype = ttype
        self.amount = amount
        self.post_bal = post_bal
       
    def modifies(self, tid, date, ttype, amount, post_bal):
        self.tid = tid
        self. date = date
        self.ttype = ttype
        self.amount = amount
        self.post_bal = post_bal
   
    def __str__(self):
        return f'{self.tid} {self.date} {self.amount}'

ankon = Customer('Ankon', 'Dhaka', 'June 16 1998', '12333', '123')
ucb = Bank('01', 'Motejheel')
ucb_atm = ATM('cumilla', 'Rohim')
transec = ATM_Transactions('2', '2 jan 2020', 'card', '2000', '40000')

ucb_atm.transactions(transec)
