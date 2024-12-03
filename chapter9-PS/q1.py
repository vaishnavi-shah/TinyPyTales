f=open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in this content")
else:
    print("The word twinkle is not present in this content")

f.close()