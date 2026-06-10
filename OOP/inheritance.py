class Animal:
    def __init__(self, name):
        self.name = name

    def animals(self):
        print("All Animals Makes Sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f"{self.name} says Woof !")


name = Animal("buddy")
dog = Dog("buddy")
name.animals()
dog.bark()
