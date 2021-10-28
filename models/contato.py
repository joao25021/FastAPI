from sqlalchemy import Column, Integer, String, Table
from config.db import meta, engine

Contato = Table(
    "contatos",
    meta,
    Column("id", Integer, primary_key=True),
    Column("nome", String(25)),
    Column("sobrenome", String(25)),
    Column("numerodetelefone", Integer, unique=True),
    Column("email", String(50), unique=True),
)


meta.create_all(engine)
