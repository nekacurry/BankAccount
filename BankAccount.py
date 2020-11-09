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


anneka = BankAccount("Anneka Curry")
anneka.deposit(50)
anneka.withdraw(10)
anneka.add_interest()
anneka.get_balance()
