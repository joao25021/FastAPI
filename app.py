from fastapi import FastAPI
from routes.contato import contato
from config.openapi import tags_metadata
from mangum import Mangum

app = FastAPI(
    title="Users API",
    description="Uma FastAPI com python e mysql",
    openapi_tags=tags_metadata,
)

app.include_router(contato)

handler = Mangum(app=app)


