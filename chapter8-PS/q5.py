# to print first n lines of the following pattern using function
'''
***
**
*
'''
# for n=3

def pattern(n):
    if(n==0): # base condition
        return
    print("*"*n)
    pattern(n-1)
n=int(input("Enter a number:"))
pattern(n)