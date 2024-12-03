# find the greatest of three numbers

# mera code logic
def num(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print(f"The greatest number is {num1}")
    elif(num2>num1 and num2>num3):
        print(f"The greatest number is {num2}")
    else:
        print(f"The greatest number is {num3}")
num(4,5,9)

# harry bhai ka code logic

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a=8
b=10
c=34
print(greatest(a,b,c))