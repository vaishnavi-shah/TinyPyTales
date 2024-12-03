name="Vaishnavi"  #Single quotes
name2='Vaishnavi'  #double qoutes
name3='''Vaishnavi''' #triple qoutes,also used for multi-line strings

#String slicing
nameshort=name[0:5] #Excluding 5th index character , starting from index 0
print(nameshort)

#negative indexing
char=name[-1] #will return last character of the string
print(char)

print(name[-5:-1]) # Excluding -1 index character
print(name[1:5]) #corresponding positive index

char1="Harshu"
print(char1[-3:-1])
print(char1[1:3])

print(name[:5]) #0 to 5 index value character , excluding 5th index ,[0:5]
print(name[5:]) # lenght-5 (starting 0 to 4 index values characters excluded),
print(name[:]) # printing entire string

print(len(name)) # printing length of the string

# skip functinality
str="Cliftonlobo"
print(str[1:3:2])
print(str[1:3])

str1="0123456789"
print(str1[1:5:4])
print(str1[1:5])

str2="amazing"
print(len(str2))
print(str2[:7]) #[0:7]
print(str2[0:]) #[0:7]
print(str2[0:7])










