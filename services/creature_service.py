class CreatureService:
    def __init__(self):
        self.creatures = []

    def register_creature(self, creature):
        self.creatures.append(creature)

    def get_power_by_name(self, name: str):
        for creature in self.creatures:
            if creature.name == name:
                return creature.use_power()
        return None

    def list_creatures(self):
        return [creature.name for creature in self.creatures]








































