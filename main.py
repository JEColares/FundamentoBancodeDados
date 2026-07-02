from fastapi import FastAPI
from crud_user import router as usuario_router

app = FastAPI(
    title="API Steel",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "API Steel - Projeto de Banco de Dados (Rode /docs para acessar a documentação)"}

app.include_router(usuario_router, prefix="/usuario")