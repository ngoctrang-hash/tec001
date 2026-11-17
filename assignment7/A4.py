import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
            
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        distance_traveled = self.current_speed * hours
        self.travelled_distance = self.travelled_distance + distance_traveled

cars_list = []

for i in range(1, 11):
    reg_num = "ABC-" + str(i)
    max_spd = random.randint(150, 200)
    new_car = Car(reg_num, max_spd)
    cars_list.append(new_car)

race_over = False

while race_over == False:
    for car in cars_list:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        
        if car.travelled_distance >= 10000:
            race_over = True

print("Registration", "Max Speed", "Current Speed", "Distance")

for car in cars_list:
    print(car.registration_number)
    print(car.maximum_speed)
    print(car.current_speed)
    print(car.travelled_distance)