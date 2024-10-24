from pydantic import BaseModel

# Definimos la clase Dragon
class Dragon(BaseModel):
    name: str
    element: str
    power_base: int
    fire_level: int

    # Método para describir el poder del dragón
    def use_power(self):
        return f"{self.name} uses {self.element} Power with base {self.power_base} and fire level {self.fire_level}!"

