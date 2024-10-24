from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Simulamos una base de datos en memoria
creatures = []

# Modelos Pydantic para validar los datos de entrada
class CreatureRequest(BaseModel):
    name: str
    element: str
    power_base: int
    fire_level: int

class Creature(BaseModel):
    name: str
    element: str
    power_base: int
    fire_level: int

# Servicio para gestionar criaturas
class CreatureService:
    def __init__(self):
        self.creatures = []

    def register_creature(self, creature: CreatureRequest):
        new_creature = Creature(
            name=creature.name,
            element=creature.element,
            power_base=creature.power_base,
            fire_level=creature.fire_level
        )
        self.creatures.append(new_creature)
        return new_creature

    def list_creatures(self) -> List[str]:
        return [creature.name for creature in self.creatures]

    def invoke_power(self, name: str) -> str:
        for creature in self.creatures:
            if creature.name == name:
                return f"{creature.name} uses {creature.element} Power (Base: {creature.power_base}, Fire Level: {creature.fire_level})"
        raise HTTPException(status_code=404, detail="Creature not found")

# Instancia del servicio
creature_service = CreatureService()

# 1. Registrar una criatura
@app.post("/creatures")
def register_creature(creature: CreatureRequest):
    created_creature = creature_service.register_creature(creature)
    return {"message": f"Creature {created_creature.name} registered successfully"}

# 2. Listar todas las criaturas registradas
@app.get("/creatures")
def get_all_creatures():
    return creature_service.list_creatures()

# 3. Invocar el poder de una criatura
@app.get("/creatures/{name}/power")
def get_creature_power(name: str):
    return {"message": creature_service.invoke_power(name)}




