from pydantic import BaseModel
from typing import Optional
from datetime import date


class usuario(BaseModel):
    id_user: int
    nome: str
    senha: str
    data_nascimento: Optional[date] = None
    email: str
    nickname: str

class usuarioUpdate(BaseModel):
    nome: Optional[str] = None
    senha: Optional[str] = None
    data_nascimento: Optional[date] = None
    email: Optional[str] = None
    nickname: Optional[str] = None



# Modelo
#class Departamento(BaseModel):
#    dnumero: int
#    dnome: str
#    cpf_gerente: None
#    data_inicio_gerente: None

#class DepartamentoUpdate():
#    dnome: str
#    cpf_gerente: Optional[str] = None
#    data_inicio_gerente: Optional[date] = None