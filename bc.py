import random
class BankAccount:
      def __init__(self,name,setpin,amount):
          self.name=name
          self.__setpin=setpin

      def __str__(self):
           return f" Account Created\n Holder Name: self.name \n The Amount: self.initialamount"
         

class CurrentAccount(BankAccount):
      def __init__(self,pin):          
      
      def getname(self):
          return self.name
      def getAccNo(self):
          return random.randrange(1000,2000)
      def getamount(self):
          if(self.__pin==1234):
             return self.__amount
      def DepositAmount(self,amount):
          self.__amount=self.__amount+amount
          return self.__amount
      def WidthDrawAmount(self,amount):
          self.__amount=self.__amount-amount
          return self.__amount


b1=BankAccount("Rakesh",1234,3000)
print("Bank Account Object Created ")
print("Account created Account no: ",b1.getAccNo())
print("Name of Account Holder",b1.getname())
print("Amount in bank of Account Holder",b1.getamount())
print("Deposit Amount",b1.DepositAmount(480))
print("WidthDraw Amount",b1.WidthDrawAmount(80))
print("Amount in bank of Account Holder",b1.getamount())
print

