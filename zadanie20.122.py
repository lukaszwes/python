"""
Rackets - 5 rackets race, random rockets move up during 10 tries
Each rocket has own speed, assigned randomly form range 1.0 to 2.0
"""
import random


class Rocket:
    def __init__(self, speed):
        self.current_position = 0
        self.speed = speed
    def moveUp(self):
        self.current_position += (1* self.speed)
        return self.current_position


rockets = [Rocket(random.randrange(10, 20, 1)/10)
           for _ in range(5)]

for _ in range(10):
    rockets[random.randint(0, 4)].moveUp()

for num, rocket in enumerate(rockets):
    print("Rocket {}:\t {} meters".format(num+1, round(rocket.current_position, 2)))



