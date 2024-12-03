# checking whether the number is prime or not

n=int(input("Enter a number:"))
for i in range(2,n):
    if(n%i)==0:
        print("The given number is not a prime number")
        break
else:
    print("The given number is a prime number")