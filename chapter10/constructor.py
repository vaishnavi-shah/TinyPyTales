class Student:
    age = 20
    std = "bscit"

    def __init__(self, name="Unknown", age=None, std=None):
        self.name = name
        # Use default values if no specific age/std is provided
        self.age = age if age is not None else Student.age
        self.std = std if std is not None else Student.std
        print("I love Python!")

    def getInfo(self):
        print(f"My age is {self.age}, studying in {self.std}")

    @staticmethod
    def greet():
        print("Hello!")

# Create an instance with all arguments
a = Student("vaishnavi", 20, "bms")
print(a.name, a.std, a.age)

# Create an instance without any arguments
b = Student()
b.greet()  # Call static method

