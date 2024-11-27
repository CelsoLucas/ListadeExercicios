from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
        self.type_fuel = str(input("Fuel Type: "))
            
    def passenger_capacity(self):
        self.pass_cap = int(input("Passenger Capacity: "))