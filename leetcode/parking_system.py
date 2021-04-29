""" 
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:
    ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
    bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.
"""

# class ParkingSystem:

#     def __init__(self, big: int, medium: int, small: int):
#         self.big = big
#         self.medium = medium
#         self.small = small

#     def addCar(self, carType: int) -> bool:
#         if carType == 1 and self.big >= 1:
#             self.big -= 1
#             return True
#         elif carType == 2 and self.medium >= 1:
#             self.medium -= 1
#             return True
#         elif carType == 3 and self.small >= 1:
#             self.small -= 1
#             return True
#         else: 
#             return False

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big, medium, small]

    def add_car(self, car_type: int) -> bool:
        self.parking[car_type - 1] -= 1
        return self.parking[car_type -1] >= 0
