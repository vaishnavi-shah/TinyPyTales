char1="In the world of boys \nhe is gentlemen \nI love him so much"
print(char1)

char2="he was \"sunshine\" \ni was midnight \'rain\'\nHe wanted it \"comfortable\" \ni wanted that\'pain\'" 
print(char2)

print("Hello\tWorld")
print("This is a backslash: \\")
print("He said, \"Hello\"")
print("Hello\b World") # backspace
print("Hello\fWorld") # Inserts a form feed, which is often used to clear the screen in old printers
print("Hello\rWorld") # Moves the cursor to the beginning of the line
print("Hello\vWorld") # vertical tab space

print("\a")
# Output: (Sound or visual alert, depending on the environment)

print("Hello\0World")
# Output: Hello World
# (Null character is usually invisible)

print("\N{GREEK SMALL LETTER ALPHA}")
# Output: α

print("\u03B1") #Inserts a Unicode character using a 16-bit hexadecimal value , Output: α

print("\U0001F600") 
# Inserts a Unicode character using a 32-bit hexadecimal value.
# Output: 😀

char3="Clifton said,\"We will have your favourite ice-cream \U0001F600\""
print(char3)


