class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")  # Set the vehicle_type to "car"
        self.year = year
        self.make = make 
        self.model = model
        self.doors = doors
        self.roofType = roof 

vehicle_type = input("Enter the type of vehicle: ")
year = input("Enter the year of your vehicle: ")
make = input("Enter the make of your vehicle: ")
model = input("Enter the model of your vehicle: ")
doors = int(input("Enter the number of doors of your vehicle: "))  # Convert input to integer
roofType = input("Enter the roof type of your vehicle: ")

# Create an instance of the Automobile class
car = Automobile(year, make, model, doors, roofType)

# Display the information
print("Vehicle Type:", vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("Roof Type:", car.roofType)
