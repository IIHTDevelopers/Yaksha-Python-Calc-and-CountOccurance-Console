def add(x,y):
    pass

def mul(x,y):
    pass

def div(x,y):
    pass

def sub(x,y):
    pass

def floor_div(x,y):
    pass

def power(x,y):
    pass

def calculator(n,x,y):
    pass

if __name__=="__main__":
    print("1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Floor Division\n 6.Power")
    n=int(input("Choose your choice"))
    x,y=[int(k) for k in input("Enter 2 integers with space seperated ").split()]
    print(calculator(n,x,y))
