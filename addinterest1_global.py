# addinterest1.py

amount = 1000

def addInterest(rate):
    amount = amount * (1+rate)
    #amount = newBalance

def test():
    rate = 0.05
    amount = addInterest(rate)
    print(amount)
    
test()