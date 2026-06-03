class Fan:
    # added constants
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # Constructor
    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    # Getters
    def get_speed(self):
        return self.__speed
    def is_on(self):
        return self.__on
    def get_radius(self):
        return self.__radius
    def get_color(self):
        return self.__color

    # Setters
    def set_speed(self, speed):
        self.__speed = speed
    def set_on(self, on):
        self.__on = on
    def set_radius(self, radius):
        self.__radius = radius
    def set_color(self, color):
        self.__color = color

    # String representation
    def __str__(self):
        if self.__on:
            return f"Fan is ON | Speed: {self.__speed}, Color: {self.__color}, Radius: {self.__radius}"
        else:
            return f"Fan is OFF | Color: {self.__color}, Radius: {self.__radius}"
# Create first fan
fan1 = Fan()
fan1.set_speed(Fan.FAST)
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.set_on(True)