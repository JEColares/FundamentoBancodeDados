from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime, timedelta

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

class vw_biblioteca_usuario(BaseModel):
    id_user: int
    nickname: str
    id_produto: int
    nome_produto: str
    tipo_produto: str
    tempo_jogado: Optional[timedelta] = None
    data_aqs: Optional[date] = None
    ultima_sessao: Optional[datetime] = None
    status_progresso: Optional[str] = None

class vw_receita_desenvolvedora(BaseModel):
    id_desenvolvedora: int
    razao_social: str
    qtd_produtos: Optional[int] = None
    receita_bruta: Optional[float] = None
    copias_vendidas: Optional[int] = None
    nota_media: Optional[float] = None
