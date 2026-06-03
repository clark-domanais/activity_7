class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Accelerate
    def accelerate(self):
        self.__speed += 5

    # Brake
    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    # Getter for speed
    def get_speed(self):
        return self.__speed

# Create the Car object
my_car = Car(2020, "Toyota")

# Accelerate 5 times
print("Accelerating:")
for i in range(5):
    my_car.accelerate()
    print(f"Speed after accelerate {i+1}: {my_car.get_speed()}")
