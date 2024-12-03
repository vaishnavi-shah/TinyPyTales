with open("log.txt") as f:
    content=f.read()
if("python" in content):
    print("Yes python is in the content")
else:
    print("No python is not in the content")