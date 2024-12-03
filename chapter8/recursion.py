'''
factorial(0)= 1
factorial(1) = 1
factorial(2) = 1x2
factorial(3) = 1x2x3
factorial(4) = 1x2x3x4
factorial(5) = 1x2x3x4x5

factorial(n) = 1x2x3x4.......n-1xn

factorial(n) = n * factorial (n-1)

'''
n = int(input('Enter a number:'))
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
print(f"The factorial of this number is:{factorial(n)}")
