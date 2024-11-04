class Account:
  mess="..Welcome to the Allied Bank.."

  def __init__(self,account_number:int,balance:float,owner:str):
    self.account_number=account_number
    self.balance=balance
    self.owner=owner
    
  def acc_balance(self):
    print(f"Your actual balance is : $ {self.balance}")


  def deposit(self):
    self.dep_amt=int(input("Enter the amount you want to deposit : "))
    self.balance +=self.dep_amt
    print(f"Amount after deposing {self.dep_amt} is : $",self.balance)


  def withdraw(self):
    self.withdraw_amt=int(input("Enter the amount you want to withdraw : "))
    self.balance -=self.withdraw_amt
    print(f"Amount after deposing {self.withdraw_amt} is : $ ",self.balance)

  
  def display_info(self):
    print(f"Account name is : {self.owner} \n Account number is : {self.account_number} \n Your balance after deposit amount is : $ {self.balance} \n Your balance after credit amount is : $ {self.balance}")
    
class SavingsAccount(Account):

  def __init__(self,account_number:int,balance:float,owner:str,interest_rate:int):

    super().__init__(account_number,balance,owner)
    self.interest_rate=interest_rate

  def interest(self):
    self.interest_rate *=self.balance
    self.balance +=self.interest_rate
    print(f"The amount after taking interest is : $ {self.balance}")


class CheckingAmount(Account):

  def __init__(self,account_number:int,balance:float,owner:str,interest_rate:int,overdraft_limit:float):
    super().__init__(account_number,balance,owner)
    self.overdraft_limit=overdraft_limit


  def withdraw(self):
    withdraw_amt = float(input("Enter the amount you want to withdraw : "))
    if withdraw_amt > 0 and (self.balance - withdraw_amt) >= (self.overdraft_limit):
      print("You have reached the limit buddy....")
      print(f"The total balance is  : $ {self.balance}")
    
    else:
      print(f"The total balance is  : $ {self.balance-withdraw_amt}")

# a1=Account(12701,5000,"Taha Ahmed")
# print(Account.mess)
# a1.acc_balance()
# a1.deposit()
# a1.withdraw()
# a1.display_info()

# a2=SavingsAccount(12701,4700,"Taha",0.9)
# a2.interest()

a3=CheckingAmount(12701,5000,"Taha",0.5,250)
a3.withdraw()