class Vehicle:
    def drive(self):
        print("the vehicle is moving")


class MotorVehicles(Vehicle):

    def __init__(self, wheels=2):
        self.wheels = wheels

    def drive(self):
        super().drive()
        print("This vehicle is moving")


class Bicycle(Vehicle):

    def __init__(self):
        super(Bicycle, self).__init__()

    def drive(self):
        super(Bicycle, self).drive()


class ElectroBike(MotorVehicles, Bicycle):

    def init(self):
        super(ElectroBike, self).__init__()
        print(f"It has {self.wheels} wheels")

    def drive(self):
        super(ElectroBike, self).drive()

    def ignition(self):
        self.active = False
        turn_ignition_key = str(input("Enter 'a' to start the car => "))
        if turn_ignition_key == "a":
            self.active = True
            print(self.active)
        else:
            self.active = False
            print("0")


print(ElectroBike.__mro__)
print(Bicycle.__mro__)
print(MotorVehicles.__mro__)
print(Vehicle.__mro__)
parent2 = Bicycle()
parent2.drive()
child = ElectroBike()
child.drive()
child.ignition()

# в классе ElectroBike сначала поиск ведется в первом объявленом
# классе(слева направо) - MotorVehicles, затем во втором - Bicycle. Класс
# Bicycle наследует класс Vehicle, таким образом при вызове метода child.drive()
# можно увидеть как метод переписанный в классе MotorVehicles, так и
# унаследованный без именнений классом Bicycle из класса  Vehicle метод drive.
