# Create a Python class representing a car with methods for accelerating and braking.

class Car:
    speed = 0

    def __init__(self, brand, model, production_year):
        self.brand = brand
        self.model = model
        self.production_year = production_year

    def accelerate(self, add_speed):
        self.speed += add_speed

    def brake(self, drop_speed):
        self.speed -= drop_speed


car_1 = Car("Brand1", "Model1", 2020)

car_1.accelerate(50)
print(car_1.speed)
car_1.accelerate(10)
print(car_1.speed)
car_1.brake(30)
print(car_1.speed)
