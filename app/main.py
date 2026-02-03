from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database, service

# Crea las tablas automáticamente al iniciar
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Persona CRUD FastAPI")

# Inyección de Dependencia para el Servicio
def get_persona_service(db: Session = Depends(database.get_db)):
    return service.PersonaService(db)

@app.get("/api/personas", response_model=List[schemas.Persona])
def read_personas(svc: service.PersonaService = Depends(get_persona_service)):
    return svc.get_all()

@app.post("/api/personas", response_model=schemas.Persona, status_code=201)
def create_persona(persona: schemas.PersonaCreate, svc: service.PersonaService = Depends(get_persona_service)):
    return svc.create(persona)

@app.get("/api/personas/{cedula}", response_model=schemas.Persona)
def read_persona(cedula: str, svc: service.PersonaService = Depends(get_persona_service)):
    persona = svc.get_by_cedula(cedula)
    if not persona:
        raise HTTPException(status_code=404, detail="Persona not found")
    return persona