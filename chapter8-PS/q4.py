# recursive function to print sum of n natural numbers
'''
sum(1)= 1
sum(2)= 1+2
sum(3)= 1+2+3
sum(4)= 1+2+3+4
sum(5)= 1+2+3+4+5
sum(n)= 1+2+3+4+.....+(n-1)+n
sum(n)=sum(n-1)+n 

'''
# mera code logic 
def sum(n):
    if(n==1): # base condition1
        return 1
    elif(n==0): # base condition 2
        return 0
    n=sum(n-1)+n             # chutiya ladki formula dekh liya kar achese
    return n
n=int(input("Enter a number:"))
print(f"The sum of {n} natural numbers is {sum(n)}.")

# harry bhai ka code logic
def sum(n):
    if(n==1): # base condition
        return 1
    return sum(n-1)+n   
print(sum(4))

# bhai ka code redundunt hai boht :)