class Category:
  ledger = []

  def __init__(self, name):  
        self.name = name  
        self.ledger = []
      
  def deposit(self, amount, description = None):
    if description == None:
      description = ""
    dict = {"amount": amount, "description": description}
    self.ledger.append(dict)

  def withdraw(self, amount, description = None):
    if self.check_funds(amount):
      if description == None:
        description = ""
      dict = {"amount": - amount, "description": description}
      self.ledger.append(dict)
      return True 
    else:
      return False

  def get_balance(self):
    balance = 0 
    for elem in self.ledger:
      balance = balance + float(elem["amount"])
    return balance
  
  def __str__(self):
    final_string = self.name.center(30,"*") + "\n"
    for elem in self.ledger:
      final_string = final_string + str(elem["description"])[:23].ljust(23) + str(format(elem["amount"], '.2f')).rjust(7) + "\n"
    
    return final_string + "Total: " + str(self.get_balance())

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  def check_funds(self, amount):
    if self.get_balance() < amount:
      return False
    else:
      return True


def create_spend_chart(categories):
  percentage = ["100|"," 90|", " 80|", " 70|", " 60|", " 50|", " 40|", " 30|", " 20|", " 10|", "  0|"]
  
  spent = {}
  all_together = 0
  for category in categories:
    spent[category.name] = 0
    for elem in category.ledger:
      if float(elem["amount"]) - 0:
        spent[category.name] = spent[category.name] + abs(float(elem["amount"]))
    all_together =+ spent[category.name]  

  n_of_circles = []
  for iter in range (len(categories)):
    n_of_circles[iter] = int(spent[categories[iter].name] / all_together) + 1
    print(n_of_circles)


    

  return 0