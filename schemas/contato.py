from typing import Optional
from pydantic import BaseModel


class ContatoBase(BaseModel):
    id: Optional[int]
    numerodetelefone: int
    nome: str
    sobrenome: str
    email: str
