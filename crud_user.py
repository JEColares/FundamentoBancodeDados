from fastapi import APIRouter, HTTPException
from db import get_connection
from models import usuario, usuarioUpdate
from typing import List, Optional


router = APIRouter()

@router.post("/usuario")
async def criar_usuario(user: usuario):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute (
            "INSERT INTO usuario (id_user, nome, senha, data_nascimento, email, nickname) VALUES(%s, %s, %s, %s, %s, %s)",
            (user.id_user, user.nome, user.senha, user.data_nascimento, user.email, user.nickname)
        )
        conn.commit()

    except Exception as e:
        conn.rollback()
        raise HTTPException(400, "Erro ao criar o usuario")
    
    finally:
        cur.close()
        conn.close()
        
    return {"msg": "Usuario criado com SUCESSO"}


@router.get("/usuario")
async def listar_usuarios():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id_user, nome, senha, data_nascimento, email, nickname FROM usuario")
    rows = cur.fetchall()

    return [
        usuario(
            id_user=d[0],
            nome=d[1],
            senha=d[2],
            data_nascimento=d[3],
            email=d[4],
            nickname=d[5]
        ) for d in rows
    ]

@router.get("/usuario/{id_user}")
async def buscar_usuario(id_user: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id_user, nome, senha, data_nascimento, email, nickname FROM usuario WHERE id_user=%s", (id_user,))
    row = cur.fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")

    return usuario(
        id_user=row[0],
        nome=row[1],
        senha=row[2],
        data_nascimento=row[3],
        email=row[4],
        nickname=row[5]
    )

@router.put("/usuario/{id_user}")
async def atualizar_usuario(id_user: int, user: usuarioUpdate):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "UPDATE usuario SET nome=%s, senha=%s, data_nascimento=%s, email=%s, nickname=%s WHERE id_user=%s",
            (user.nome, user.senha, user.data_nascimento, user.email, user.nickname, id_user)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Erro ao atualizar o usuario")
    finally:
        cur.close()
        conn.close()

    return {"msg": "Usuario atualizado com SUCESSO"}



@router.delete("/usuario/{id_user}")
async def deletar_usuario(id_user: int):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM usuario WHERE id_user=%s", (id_user,))
        
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Erro ao deletar o usuario")
    finally:
        cur.close()
        conn.close()

    return {"msg": "Usuario deletado com SUCESSO"}

