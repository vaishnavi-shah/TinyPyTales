tp = (1, 2, 3, 2, 2, 4)
# Returns the number of times a specified value appears in the tuple.
print(tp.count(2))  

tp1=("Clifton","Loves","Vaishnavi",777,"Clifton","Pookie","Honey")
print(tp1.count("Clifton"))

tuple1 = (1, 2, 3, 4)
# Returns the index of the first occurrence of a specified value in the tuple
print(tuple1.index(3))  # 

tuple2=(91,"Japan","Korea","Thailand","Nepal","Sri Lanka","Indoneisa")
print(tuple2.index("Nepal"))

tup1 = (1, 2)
tup2 = (3, 4)
tup3 = tup1 + tup2 # Concatenation
print(tup3)

t1 = ("Love")
t1_repeated = t1 * 5 # Repetition
print(t1_repeated)

t2 = (1, 2, 3)
print(2 in t2)  # membership operator (in operator)
print(4 not in t2) #memberhsip operator (not in operator)

t3 = (1, 2, 3, 4)
print(t3[1:3]) # slicing
print(len(t3))
