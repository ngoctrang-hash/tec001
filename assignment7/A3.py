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

car = Car("ABC-123", 142)
car.travelled_distance = 2000
car.current_speed = 60
car.drive(1.5)
print(car.travelled_distance)