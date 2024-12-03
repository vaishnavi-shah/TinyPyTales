men=["clifton","aaron","sunjae","minmin","atlas"]
print(men)

men.append("fictional") # adds element at the end of the list
men.remove("minmin") #delecting element

print(men)

list1=[19,23,32,40,35,16,67,98,49]
list1.sort() #ascending order
list1.reverse() # descending order
print(list1)

list2=["ngt","ai","spm","iot","awp","marathi"]
list2.pop(5) # removing element at 4th index
list2.insert(4,"power BI")
print(list2)

list3=["ngt","ai","spm","iot","awp","marathi"]
value = list3.pop(5) # storing removed element
print(value)
