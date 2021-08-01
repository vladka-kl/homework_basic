class Dealership(object):

    def __init__(self):
        self.list_of_cars = []

    def car(self, brand, model, year, color):
        self.list_of_cars.append(Car(brand, model, year, color))

    def info_car(self):
        # for i in (self.brand, self.model, self.year,self.color):
        #     print(f"- {i}")
        for car in self.list_of_cars:
            print(car)

    # def info_car(self):
    #     """Return the dictionary"""
    #     car = {"the brand": self.brand, "the model": self.model, "year": self.year,
    #              "color": self.color}
    #     return car
    #
    # def list_of_cars_av(self):
    #     """Return list of cars available"""
    #     self.list_of_cars.append(car.info_cars())
    #
    # def sell_cars(self):
    #     for car in self.list_of_cars:
    #         print(car)
    #     print("Please enter the brand of the car for sale")
    #
    # #
    #
    # def cars(self):
    #     return self.list_of_cars.append(Car())
    #
    # def info_cars(self):
    #     for i in self.list_of_cars:
    #         print(i)

    # list_of_cars = []
    # for i in (self.brand,self.model, self.year,self.color):
    #       list_of_cars.append(i)
    #     return list_of_cars
    #
    #     print(f"The cars available for sale are: {self.list_of_cars}")
    #     selected_car = str(input("Please enter a name of the car: "))
    #     print(f"{selected_car} is yours now!")

class Car:
    """simplified car model"""

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.profile = {}

    def __str__(self):
        return "The car info: {} {}, {}, {} color".format(self.brand,\
                                    self.model, self.year,self.color)

    # def info_cars(self):
    #     """Return the dictionary"""
    #
    # car = {"the brand": self.brand, "the model": self.model, "year": self.year,
    #              "color": self.color}
    # return car



car_1 = Car("toyota", "camry", 2020, "white")
car_2 = Car("bmw", "x5", 2019, "black")
car_3 = Car("tesla", "model s", 2021, "red")


car_3.info_car()

# def main():
#     list_of_cars = []
#     list_of_cars.append(car_2.info_cars())
#     list_of_cars.append(car_1.info_cars())
#     list_of_cars.append(car_3.info_cars())
#     for i in list_of_cars:
#         print(f"- {i}")
#
# main()






# def sell_car():
#     list_of_cars = ["toyota", "bmw", "tesla"]
#     while True:
#         sold_cars = []
#         print("Please select a car from the list")
#         print(f"The cars available for sale are: {list_of_cars}")
#         print("(enter 'q' to quit")
#         selected_car = str(input("Please enter a name of the car: "))
#         if selected_car == "q":
#             break
#         elif selected_car == "toyota":
#             sold_car = list_of_cars.pop(0)
#             print(f"Toyota is yours!")
#             sold_cars.append(sold_car)
#         elif selected_car == "bmw":
#             sold_car1 = list_of_cars.pop(1)
#             print(f"BMW is yours!")
#             sold_cars.append(sold_car1)
#         elif selected_car == "tesla":
#             sold_car2 = list_of_cars.pop(2)
#             print(f"Tesla is yours!")
#             sold_cars.append(sold_car2)
#         else:
#             print("Error, try again")
#
