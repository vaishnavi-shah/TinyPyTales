import os
# Select the directory whose content you want to list
directory_path = "/"
# use the os module to list the content
contents = os.listdir(directory_path)
# printing the content of the directory
print(contents)