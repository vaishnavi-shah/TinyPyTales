# inches to centimeters convertor
def inch_to_cms(inch):
    return inch * 2.54
n = int(input("Enter your height in inches:"))
print(f"Your corresponding height in cms is:{inch_to_cms(n)}")