# creating a copy of existing file 

with open("this.txt") as f:
    content = f.read()
with open("this_copy.txt","w") as f:
    f.write(content)
