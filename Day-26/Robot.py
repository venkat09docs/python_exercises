class Robot:
    """
    This class is the tempalte for the robot Object.
    """
    population = 0 # Class attribute to track the number of Robot
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Robot.population += 1

    def __del__(self):
        print(f'{self.name} is destroyed')

    def setEnergy(self, energy):
        self.energy = energy

    def __add__(self, other):
        if isinstance(other, Robot):
            return self.price + other.price
        return NotImplemented

    def __str__(self):
        return f'Robot Name: {self.name}, Price: {self.price}'





r1 = Robot("Robo1", 1000)
print(r1.__doc__)
r1.setEnergy(500)
print(f'Robot Name {r1.name} and Price {r1.price}')
print(getattr(r1, 'energy', 'Energy attribute not found'))  # Using getattr to safely access energy

print(r1.__dict__)

r2 = Robot("Robo2", 10000)
r2.setEnergy(5000)
print(f'Robot Name {r2.name} and Price {r2.price}')
print(r2.energy)

print(r2.__dict__)

r3 = Robot("Robo3", 100000)
print(f'Population of Robots: {Robot.population}')

# print(r1 > r2)
print(r1 + r2)
print(r1.__add__(r3))

print(str(r1))
print(str(r2))





