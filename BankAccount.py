class BankAccount:
  def __init__(self, name):
    self.full_name = name
    self.routing_number = 86948275
    self.account_number = 38576938
    self.balance = 0
  
  def deposit(self, amount):
    self.balance += amount
    print (f"Amount Deposited: ${amount}")

  def withdraw(self,amount):
    overdraft_fee = 10
    if amount > self.balance:
      self.balance -= overdraft_fee
      print("Insufficient funds")
    else:
      self.balance -= amount
      print(f"Amount Withdrawn: ${amount}")

  def get_balance(self):
    print(f"You have ${round(self.balance, 2)} remaining in your account! Don't spend it all in one place ;)")

  def add_interest(self):
    m_interest = 0.00083
    interest = self.balance *  m_interest
    self.balance += interest

  def print_receipt(self):
    print(f"""
          {self.full_name}
          Account No.:****{str(self.account_number)[-4:]}
          Routing No.: {self.routing_number}
          Balance: ${round(self.balance, 2)}""")

anneka = BankAccount("Anneka Curry")
anneka.deposit(70)
anneka.withdraw(80)
anneka.add_interest()
anneka.get_balance()
anneka.print_receipt()

tori = BankAccount("Victoria Murray")
tori.deposit(500)
tori.withdraw(50)
tori.add_interest()
tori.get_balance()
tori.print_receipt()

cay = BankAccount("Caylin Kaunas")
cay.deposit(2000)
cay.withdraw(350)
cay.add_interest()
cay.get_balance()
cay.print_receipt()


