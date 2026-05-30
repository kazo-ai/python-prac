class Dog :
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

my_dog = Dog("nooody", "pug")

print(my_dog.name, my_dog.breed, my_dog.bark())