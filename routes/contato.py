from fastapi import APIRouter, HTTPException
from config.db import conn
from models.contato import Contato
from schemas.contato import ContatoBase
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

contato = APIRouter()


@contato.get(
    "/contatos",
    tags=["contatos"],
    response_model=List[ContatoBase],
    description="Get a list of all users",
)
def get_contatos():
    return conn.execute(Contato.select()).fetchall()


@contato.get(
    "/contatos/{id}",
    tags=["contatos"],
    response_model=ContatoBase,
    description="Get a single user by Id",
)
def get_contato(id: int):
    db_contato = conn.execute(Contato.select().where(Contato.c.id == id)).first()
    if db_contato is None:
        raise HTTPException(status_code=404, detail="contato not found")
    return db_contato


@contato.post("/", tags=["contatos"], response_model=ContatoBase, description="Create a new user")
def create_contato(contato: ContatoBase):
    novo_contato = {"nome": contato.nome,
                    "sobrenome": contato.sobrenome,
                    "numerodetelefone": contato.numerodetelefone,
                    "email": contato.email}
    db_contato = conn.execute(Contato.select().where(Contato.c.numerodetelefone == contato.numerodetelefone)).first()
    if db_contato:
        raise HTTPException(status_code=400, detail="Numero de telefone esta já registrado")
    result = conn.execute(Contato.insert().values(novo_contato))
    return conn.execute(Contato.select().where(Contato.c.id == result.lastrowid)).first()



@contato.put("/contato/{id}", tags=["contatos"], response_model=ContatoBase, description="Update a User by Id")
def update_contato(contato: ContatoBase, id: int):
    conn.execute(
        Contato.update()
            .values(nome=contato.nome,
                    sobrenome=contato.sobrenome,
                    numerodetelefone=contato.numerodetelefone,
                    email=contato.email)
            .where(Contato.c.id == id)
    )
    return conn.execute(Contato.select().where(Contato.c.id == id)).first()


@contato.delete("/{id}", tags=["contatos"], status_code=HTTP_204_NO_CONTENT)
def delete_user(id: int):
    conn.execute(Contato.delete().where(Contato.c.id == id))
    return conn.execute(Contato.select().where(Contato.c.id == id)).first()
