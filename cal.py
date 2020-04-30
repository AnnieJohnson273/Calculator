def add(a,b):
    z=a+b
    return z
def sub(a,b):
    z=a-b
    return z
def mul(a,b):
    z=a*b
    return z
def div(a,b):
    if(b==0):
        print("DIVISION BY ZERO!!!ERROR!!")
        return 'not defined'
    else:
        z=a/b
        return z 
def mod(a,b):
    if(b==0):
        print("DIVISION BY ZERO!!!ERROR!!")
        return 'not defined'
    else:
        z=a%b
        return z