class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof!"

class Cat(Animal):
    def speak(self):
        return "meow!"

# Function to make any animal speak
def animal_sound(animal):
    print(animal.speak())

# Creating Instances of Dog and Cat
dog = Dog()
cat = Cat()

# Using polymorphism to call the speak method
animal_sound(dog)
animal_sound(cat)