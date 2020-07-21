"""
Rackets - 5 rackets race in 60 seconds
input parameters for each rocket: acceleration  [range 1.0 - 2.0]
                                  mass          [range 300 - 999]
"""
import random
import math

time = 60

class Rocket:
    """
    Rocket class
    """
    def __init__(self, acceleration, mass):
        self.acceleration = acceleration
        self.mass = mass
        self.graph = ""
    def rocketStart(self):
        """
        Start movingup of rocket
        :return: distance (type int)
        """
        self.distance = self.acceleration * self.mass * time
        return self.distance
    def rocketGraph(self):
        """
        Print graphic progress for each rocket
        :return: string of # (type str)
        """
        for _ in range(math.floor(self.distance/1000,)):
            self.graph += "#"
        return self.graph

rockets = [Rocket((random.randrange(10, 20, 1)/10), random.randint(300, 999))
           for _ in range(5)]

for rocket in rockets:
    rocket.rocketStart()

winner_distance = 0
for num, rocket in enumerate (rockets):
    if rocket.distance > winner_distance:
        winner_distance = rocket.distance
        winner = num + 1
    print("Rocket {} [a={} m={} v.aver={}]:\t {} meters \t {}>>|ROCKET {} |>".format(num+1, rocket.acceleration,
                                                                                     rocket.mass,
                                                                                     round(rocket.distance/time, 2),
                                                                                     round(rocket.distance, 2),
                                                                                     rocket.rocketGraph(), num+1))

print("\nThe WINNER is: Rocket {}!".format(winner))