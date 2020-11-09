class BankAccount:
  def __init__(self, name):
    self.full_name = name
    self.routing_number = 86948275
    self.account_number = 38576938
    self.balance = 0
  
  def deposit(self, amount):
    self.balance += amount
    print (f"Amount Deposited: ${amount}")

anneka = BankAccount("Anneka Curry")
anneka.deposit(50)
