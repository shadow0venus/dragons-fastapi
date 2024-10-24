from creature import Creature

class Chimera(Creature):
    def __init__(self, name: str, element: str, power_base: int, number_of_heads: int):
        super().__init__(name, element, power_base)
        self.number_of_heads = number_of_heads

    def use_power(self) -> str:
        return f"{self.name} attacks with {self.number_of_heads} heads!"
