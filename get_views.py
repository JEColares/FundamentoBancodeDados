from fastapi import APIRouter,HTTPException
from db import get_connection
from models import vw_biblioteca_usuario, vw_receita_desenvolvedora

router = APIRouter()

# View 1: vw_biblioteca_usuario
@router.get("/biblioteca_usuario")
async def listar_usuarios():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM vw_biblioteca_usuario")
    rows = cur.fetchall()

    return [
        vw_biblioteca_usuario(
            id_user=d[0],
            nickname=d[1],
            id_produto=d[2],
            nome_produto=d[3],
            tipo_produto=d[4],
            tempo_jogado=d[5],
            data_aqs=d[6],
            ultima_sessao=d[7],
            status_progresso=d[8]
        ) for d in rows
    ]

# View 2: vw_receita_desenvolvedora
@router.get("/receita_desenvolvedora")
async def listar_receita_desenvolvedora():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM vw_receita_desenvolvedora")
    rows = cur.fetchall()

    return [
        vw_receita_desenvolvedora(
            id_desenvolvedora=d[0],
            razao_social=d[1],
            qtd_produtos=d[2],
            receita_bruta=d[3],
            copias_vendidas=d[4],
            nota_media=d[5]
        ) for d in rows
    ]