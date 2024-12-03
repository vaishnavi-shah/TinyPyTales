char1="vaishnavi_lobo"
print(char1.title()) # Converts the first character of each word to uppercase
print(len(char1)) # len() - return length of the string
print(char1.endswith("Lobo")) #return true/false

char2="Clifton loves Vaishnavi"
print(char2.startswith("Clifton")) #returns true/false

char3="pookie"
print(char3.capitalize()) #capitalizes first cahracter in the string

char3 = " Hello Babe "
print(char3.upper())  
print(char3.lower())  
print(char3.strip())  #  removes space in the default
print(char3.replace("Babe", "Sweetu")) #Replaces all occurrences of a substring with another substring

# Returns the lowest index in the string where the substring sub is found.
# Returns -1 if the substring is not found.
print(char3.find("Hello"))

print(char3.split(" ")) # splits string based on seperator

char4=["Hey","Shawty"]
print(" ".join(char4)) #Joins the elements of an iterable (e.g., list) into a single string

char5="4567"
print(char5.isdigit()) # all characters in string are numeric

char6="Chingu"
print(char6.isalpha()) # all characters in the string are alphabetic

char7="clifvaish777"
print(char7.isalnum()) # alphanumeric 



