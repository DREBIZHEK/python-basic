from abc import ABC
import homework_02.exceptions


class Vehicle(ABC):
    weight = 2000
    started = False
    fuel = 100
    fuel_consumption = 10

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0 & (self.started == False):
            self.started = True
        else:
            if self.fuel <= 0:
                raise homework_02.exceptions.LowFuelError()

    def move(self, distance):
        if distance * self.fuel_consumption <= self.fuel:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise homework_02.exceptions.NotEnoughFuel
