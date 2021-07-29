class Car:
    """simplified car model"""

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return "The car info: {} {}, {}, {} color".format(self.brand,
                                                          self.model, self.year,
                                                          self.color)


car_1 = Car("toyota", "camry", 2020, "white")
car_2 = Car("bmw", "x5", 2019, "black")
car_3 = Car("tesla", "model s", 2021, "red")
print(car_3)


class Dealership(object):

    def __init__(self, list_of_cars=[]):
        self.list_of_cars = list_of_cars

    def sell_cars(self):
        print(f"The cars available for sale are: {self.list_of_cars}")
        selected_car = str(input("Please enter a name of the car: "))
        print(f"{selected_car} is yours now!")


cars = Dealership(["toyota", "tesla", "bmw"])
cars.sell_cars()

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
