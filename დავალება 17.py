# დავალება 1
class Car1:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(f"ბრენდი: {self.brand}, მოდელი: {self.model}, წელი: {self.year}")


# დავალება 2
class Car2:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def age_of_car(self):
        from datetime import datetime
        return datetime.now().year - self.year

    def car_info(self):
        print(f"ბრენდი: {self.brand}, მოდელი: {self.model}, წელი: {self.year}, ასაკი: {self.age_of_car()} წლის")


# დავალება 3
class ElectricCar(Car2):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"ელემენტის ხანგრძლივობა შეადგენს {self.battery_life} საათს.")


# დავალება 4
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
        print(f"ბრენდი: {self.brand}, მოდელი: {self.model}, წელი: {self.year}, ასაკი: {self.age_of_car()} წლის")


# დავალება 5
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
        print(f"ბრენდი: {self.brand}, მოდელი: {self.model}, წელი: {self.year}, ასაკი: {self.age_of_car()} წლის")

    @classmethod
    def total_cars(cls):
        print(f"მანქანების მთლიანი რაოდენობა: {cls.number_of_cars}")
        