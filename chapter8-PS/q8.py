 # printing multiplication table using function

def table(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
    return n
n = int(input("Enter a number:"))
table(n)