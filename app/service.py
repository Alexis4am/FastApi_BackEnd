from sqlalchemy.orm import Session
from repository import PersonaRepository
import models, schemas

class PersonaService:
    def __init__(self, db: Session):
        self.repo = PersonaRepository(db)

    def get_all(self):
        return self.repo.find_all()

    def get_by_cedula(self, cedula: str):
        return self.repo.find_by_cedula(cedula)

    def create(self, persona_data: schemas.PersonaCreate):
        # Convierte el esquema (DTO) a Modelo de Base de Datos
        persona = models.Persona(**persona_data.model_dump())
        return self.repo.save(persona)