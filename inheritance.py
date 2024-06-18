class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The engine of the {self.model} is starting."
    
    def stop_engine(self):
        return f"The engine of the {self.model} is stopping."
    
    def disply_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
    
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year) #Inheriting from Vehicle
        self.num_doors = num_doors
    
    def open_trunk(self):
        return f"The trunk of the {self.model} is open"
    
    # Overriding display_info method
    def display_info(self):
                return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Number of Doors: {self.num_doors}"
    
class Bicycle(Vehicle):
    def __init__(self, brand, model, year, type_bike):
        super().__init__(brand, model, year) # Inherited from vehicle
        self.type_bike = type_bike
    
    def ring_bell(self):
        return f"The bell of the {self.model} is ringing."
    
    # Overriding display_info method
    def display_info(self):
            return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Bike Type: {self.type_bike}"
    
car = Car("Toyota", "Corolla", 2021, 4)
bike = Bicycle("Giant", "Escape 3", 2022, "Road Bike")

print(car.start_engine())
print(bike.ring_bell())

print(car.display_info())
print(car.open_trunk())