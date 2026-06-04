class Pet:
    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Setters (Mutators)
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # Getters (Accessors)
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

# Create a Pet object
my_pet = Pet()

# Get user input
name = input("Enter your pet's name: ")
animal_type = input("Enter the type of animal (Dog, Cat, Bird, etc.): ")
age = int(input("Enter your pet's age: "))

# Set values using mutators
my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)
