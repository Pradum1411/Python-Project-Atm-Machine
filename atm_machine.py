class Atm:
    def __init__(self):
        self.__pin="123"
        self.__balance=0
       
    def get_pin(self):
        return self.__pin  
    def set_pin(self,pin):
        self.__pin=pin
        print("Pin is Updated")    

    def __check_balance(self):
        pin=int(input("Entre pin:"))
        if(pin==self.__pin):
            print(self.__balance)   
        else:
            print("Wrong pin")    
    def deposite_money(self,money):
        pin=int(input("Entre pin:"))
        if(pin==self.__pin):
            self.__balance+=money
            print("money deposite successfully")
        else:
            print("Wrong pin")    

    def debited_money(self,money):
        pin=int(input("Entre pin:"))
        if(pin==self.__pin):
            if(self.__balance>=money):
                self.__balance-=money
                print("Successfully")
            else:
                print("Not efficient balance")    
        else:
            print("Wrong pin")

sbi=Atm()

while(True): 
    print("""
        1. get_pin 1
        2. set_pin 2
        3. check balance 3
        4. deposite money 4
        5. debited money 5
        6. quit press otherthan 1 2 3 4 5
        """)
    n=int(input("Enter your choice:"))   
    if(n==1):
        print(sbi.get_pin()) 
    elif(n==2):
        pin=int(input("Enter new pin:"))
        sbi.set_pin(pin)
    elif(n==3):
        sbi._Atm__check_balance()
    elif(n==4):
        money=int(input("Enter deposite money:"))
        sbi.deposite_money(money)
    elif(n==5):
        money=int(input("Enter money:"))
        sbi.debited_money(money)
    else:
        exit()
      