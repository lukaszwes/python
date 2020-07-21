class User:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def inna_funkcja(self):
        print("hello world")
    def print_age(self):
        print("{} ma {} lat".format(self.name, self.age))


user1 = User("Sebastian", 24)
user2 = User("Miroslaw", 19)


user1.print_age()
user2.print_age()