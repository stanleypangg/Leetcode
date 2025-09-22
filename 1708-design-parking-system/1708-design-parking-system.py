class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.map = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        # carType in {1, 2, 3}
        # checks if there is a parking space of carType
        # a car can only park in parking space of its carTyype
        # if there is no space, return false, else park the car in that size space
        if self.map[carType] == 0:
            return False
        self.map[carType] -= 1
        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)