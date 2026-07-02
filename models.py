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

class Desenvolvedora(BaseModel):
    id_desenvolvedora : int
    comissao_plat : Optional[str] = None
    razao_social : str
    cnpj:str
    
class DesenvolvedorUpdate(BaseModel):
    comissao_plat : Optional[str] = None
    razao_social: str
    cnpj:str
