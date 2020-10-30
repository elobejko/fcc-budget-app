class Category:
  ledger = []

  def __init__(self, name):  
        self.name = name  
        self.ledger = []
      
  def deposit(self, amount, description = ""):
    dict = {"amount": amount, "description": description}
    self.ledger.append(dict)

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      dict = {"amount": - amount, "description": description}
      self.ledger.append(dict)
      return True 
    return False

  def get_balance(self):
    balance = 0 
    for elem in self.ledger:
      balance = balance + float(elem["amount"])
    return balance
  
  def __str__(self):
    final_string = self.name.center(30,"*") + "\n"
    for elem in self.ledger:
      final_string += str(elem["description"])[:23].ljust(23) + str(format(elem["amount"], '.2f'))[:7].rjust(7) + "\n"
    return final_string + "Total: " + str(self.get_balance())

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    return False

  def check_funds(self, amount):
    if self.get_balance() < amount:
      return False
    return True


def create_spend_chart(categories):
  percentage = [i for i in range(100, -10, -10)]
  spent = []
  names = []
  all_together = 0
  for category in categories:
    tmp = 0
    names.append(category.name)
    for elem in category.ledger:
      if float(elem["amount"]) < 0:
        tmp += abs(float(elem["amount"]))
    spent.append(tmp)
    all_together += tmp

  s = "Percentage spent by category\n"
  for p in percentage:
    s += (str(p) + "| ").rjust(5)
    for value in spent:
      if int(10*value/all_together) >= p / 10:
        s += "o  "
      else:
        s += "   "
    s += "\n"
  s += 4 * " " + (3 * len(spent) + 1) * "-" + "\n"

  for ii in range(len(max(names, key = len))):
    s += 5 * " "
    for name in names:
      if len(name) > ii:
        s += name[ii] + "  "
      else:
        s += "   "
    if ii < len(max(names, key = len)) - 1:
      s += "\n"

  return s