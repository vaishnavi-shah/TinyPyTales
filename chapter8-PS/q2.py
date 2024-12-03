# celsius_to_fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 # formula to be used
    return fahrenheit
celsius = int(input("Enter temperature in celsius:"))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")



# fahrenheit_to_celsius

def fahrenheit_to_celsius(f):
    return 5*(f-32)/9
f=int(input("Enter temperature in fahrenhiet:"))
c= fahrenheit_to_celsius(f)
print(f"{round(c,2)}°C") # rounding decimal upto 2 digits only