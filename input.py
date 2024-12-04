## Activity 1 :
# Base class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"Device Info: {self.brand} {self.model}"

# Derived class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  
        self.storage = storage
        self.battery = battery
        self._secret_feature = "Hidden Camera Mode"  

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def show_secret_feature(self):  
        return f"The secret feature is: {self._secret_feature}"

# Testing the class
smartphone = Smartphone("Apple", "iPhone 14", "256GB", "18 hours")
print(smartphone.info())
smartphone.call("123-456-7890")
smartphone.browse("www.openai.com")
print(smartphone.show_secret_feature())

## Activity 2
class Vehicle:
    def move(self):
        pass  

# Derived class: Car
class Car(Vehicle):
    def move(self):
        print("Driving ")

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ")

# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ")

# Function to demonstrate polymorphism
def demonstrate_movement(vehicle):
    vehicle.move()

# Testing polymorphism
car = Car()
plane = Plane()
boat = Boat()

demonstrate_movement(car)
demonstrate_movement(plane)
demonstrate_movement(boat)

