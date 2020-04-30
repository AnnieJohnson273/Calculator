import calculator as cal
o=0
while o!=6:
    o=int(input("\nEnter 1.ADD \n 2.SUBTRACT \n 3.PRODUCT \n 4.DIVISION \n 5.MODULUS \n 6.EXIT\n"))
    if(o==1):
        a=int(input("\nEnter the first number :\n"))
        b=int(input("\nEnter the second number:\n"))
        c=cal.add(a,b)
        print("\nThe sum is ",c)
    elif(o==2):
        a=int(input("\nEnter the first number:\n"))
        b=int(input("\nEnter the second number:\n"))
        c=cal.sub(a,b)
        print("\nThe difference is ",c)
    elif(o==3):
        a=int(input("\nEnter the first number:\n"))
        b=int(input("\nEnter the second number:\n"))
        c=cal.mul(a,b)
        print("\nThe product is ",c)
    elif(o==4):
        a=int(input("\nEnter the dividend\n"))
        b=int(input("\nEnter the divisor\n"))
        c=cal.div(a,b)
        print("\nThe quoitent is ",c)
    elif(o==5):
        a=int(input("\nEnter the dividend\n"))
        b=int(input("\nEnter the divisior\n"))
        c=cal.mod(a,b)
        print("\nThe remainder is ",c)
    elif(o==6):
        print("\nExit\n")
    else:
        print("\nInvalid number\n")