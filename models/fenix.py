from creature import Creature

class Fenix(Creature):
    def __init__(self, name: str, element: str, power_base: int, rebirth_count: int):
        super().__init__(name, element, power_base)
        self.rebirth_count = rebirth_count

    def use_power(self) -> str:
        return f"{self.name} rises from the ashes, reborn {self.rebirth_count} times!"
