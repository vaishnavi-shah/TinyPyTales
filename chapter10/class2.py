class Employee:
    language = "Python"  # class attribute 1
    salary = 1200000      # class attribute 2

vaish = Employee()
vaish.name = "Vaishnavi"  # object (instance) attribute
print(vaish.name,vaish.language,vaish.salary)

clif = Employee()
clif.name = "Clifton"  # object (instance) attribute
print(clif.name,clif.language,clif.salary)

# here names are object (instance) attributes and language and salary
# are class attributes as they directly belong to class