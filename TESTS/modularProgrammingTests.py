class Dog:
    def __init__(self, name, age, atwhom):
        self.name = name  # Attribute: dog's name
        self.age = age    # Attribute: dog's age
        self.atwhom = atwhom #attribute: whos the dog barking at

    def bark(self):
        print(f"{self.name} says: Woof! whenever it sees {self.atwhom}")

my_dog = Dog("remo", 20, "shelley")
my_dog.bark()