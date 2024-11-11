class Vehicle:
    def __init__(self):
        self.vehicleType = input("Enter vehicle type: ")
    

class Automobile(Vehicle):
    
    def __init__(self):
        super().__init__()
        self.year = input("Enter the year of Vehicle: ")
        self.make = input("Enter make of vehicle: ")
        self.model = input("Enter model of vehicle: ")
        self.doors = input("Enter number of doors on vehicle(2 or 4): ")
        self.roof = input("Enter the type of roof on vehicle(solid or sun roof): ")

        print(f"Vehicle Type: {self.vehicleType}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


vehicle = Automobile()

