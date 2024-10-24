class Creature:
    def __init__(self, name: str, power: str, base):
        self.name = name
        self.power = power

    def use_power(self):
        return f"{self.name} uses {self.power}"
