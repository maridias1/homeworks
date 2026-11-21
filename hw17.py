# Task 1
class Car1:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


# Task 2
class Car2:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def age_of_car(self):
        from datetime import datetime
        return datetime.now().year - self.year

    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Age: {self.age_of_car()} years")


# Task 3
class ElectricCar(Car2):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"Battery life is {self.battery_life} hours.")


# Task 4
class Car4:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car4.number_of_cars += 1

    def age_of_car(self):
        from datetime import datetime
        return datetime.now().year - self.year

    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Age: {self.age_of_car()} years")


# Task 5
class Car5:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car5.number_of_cars += 1

    def age_of_car(self):
        from datetime import datetime
        return datetime.now().year - self.year

    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Age: {self.age_of_car()} years")

    @classmethod
    def total_cars(cls):
        print(f"Total number of cars: {cls.number_of_cars}")
