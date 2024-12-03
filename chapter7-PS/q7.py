'''
for n=3
  *
 ***
*****
'''
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")  # This prints the required leading spaces
    print("*" * (2 * i - 1))      # This prints the stars in each row

