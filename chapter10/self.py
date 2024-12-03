class Employee:
    language = "Python"  # class attribute 1
    salary = 1200000      # class attribute 2

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    def greet(self):
        print(f"Good Morning! {self.name}")

vaish = Employee()
vaish.name = "Vaishnavi"  # object (instance) attribute
print(vaish.name,vaish.language,vaish.salary)

vaish.getInfo()
vaish.greet()
# Employee.getInfo(vaish)