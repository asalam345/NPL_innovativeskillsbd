from abc import ABC, abstractmethod

class Vehicle(ABC):  # Like an abstract class in C#
    @abstractmethod
    def start(self):
        pass
    
    def stop(self):  # Can have concrete implementation
        print("Stopping vehicle")

class Car(Vehicle):
    def start(self):  # Must implement abstract method
        print("Car starting")