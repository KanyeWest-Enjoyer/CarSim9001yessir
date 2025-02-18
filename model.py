from random import randint

class Car(object):
    pass

class Wheel(object):

    def __init__(self):
        self.orientation = randint(0, 360)

    def rotate(self, revolutions):
        degreesOfRotation = 360 * revolutions
        self.orientation = (self.orientation + degreesOfRotation) % 360


class Engine(object):
    pass

class Gearbox(object):

    def __init__(self):
        self.currentGear = 0
        self.clutchEngaged = False
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]
        self.wheels = {}
        for newWheel in ['frontLeft', 'frontRight', 'rearLeft', 'rearRight']:
            self.wheels[newWheel] = Wheel()

    def shiftUp(self):
        if self.currentGear < len(self.gears) - 1 and not self.clutchEngaged:
            self.currentGear += 1

    def shiftDown(self):
        if self.currentGear != 0 and not self.clutchEngaged:
            self.currentGear -= 1

    def rotate(self, revolutions):
        newRevs = revolutions * self.gears[self.currentGear]
        for wheel in self.wheels:
            self.wheels[wheel].rotate(newRevs)

class Tank(object):
    def __init__(self):
        self.capacity = 100
        self.contents = 100

    def remove(self, amount):
        self.contents -= amount
        if self.contents < 0:
            self.contents = 0

    def refuel(self):
        self.contents = self.capacity

