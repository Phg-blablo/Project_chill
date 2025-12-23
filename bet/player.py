class Player:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
        self.account = 1000
        self.bet = 0
        self.choice = ""
        self.result = 0 
        print('Welcome: ',self.name,'you have: ',self.account)