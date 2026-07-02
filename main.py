from fastapi import FastAPI
from crud_user import router as usuario_router
from crud_desenvolvedora import router as desenvolvedora_router
from get_views import router as get_views_router

app = FastAPI(
    title="API Steel",
    version="1.0.0"
)


app.include_router(usuario_router, prefix="/usuario", tags = ["Usuarios"])
app.include_router(desenvolvedora_router, prefix="/desenvolvedora", tags = ["Desenvolvedoras"])
app.include_router(get_views_router, prefix="/views", tags = ["Views"])

