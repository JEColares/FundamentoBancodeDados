from fastapi import APIRouter,HTTPException
from db import get_connection
from models import DesenvolvedorUpdate,Desenvolvedora
from typing import List, Optional

router =  APIRouter()

@router.post("/")
async def criar_desenvolvedora(des: Desenvolvedora):
    conn = get_connection()
    cur = conn.cursor()

    try:
        query = """
            INSERT INTO Desenvolvedora (id_desenvolvedora, comissao_plat, razao_social, cnpj) 
            VALUES (%s, %s, %s, %s)
        """
        valores = (des.id_desenvolvedora, des.comissao_plat, des.razao_social, des.cnpj)
        
        cur.execute(query, valores)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(400,f"Erro ao criar Desenvolvedora {e}")
    
    finally:
        cur.close()
        conn.close()
    return {"msg": "Desenvolvedora criada com sucesso"}

@router.get("/{id_desenvolvedora}")
async def listar_desenvolvedoras_by_id(id_desenvolvedora:int):
    conn = get_connection()
    cur = conn.cursor()

    try:

        query = "SELECT id_desenvolvedora, comissao_plat, razao_social, cnpj FROM desenvolvedora WHERE id_desenvolvedora = %s"
    
        cur.execute(query, (id_desenvolvedora,))
        d = cur.fetchone()
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {e}")
    finally:
        cur.close()
        conn.close()
    if d:
        return Desenvolvedora(
                id_desenvolvedora=d[0],
                comissao_plat=d[1],
                razao_social=d[2],
                cnpj=d[3]
            )
    raise HTTPException(404,"Desenvolvedora não encontrada")
    
@router.get("/")
async def listar_desenvolvedoras():
    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT id_desenvolvedora, comissao_plat,razao_social,cnpj FROM Desenvolvedora
    """
    cur.execute(query)
    conn.commit()

    rows = cur.fetchall()

    cur.close()
    conn.close()
    return [
        Desenvolvedora(
            id_desenvolvedora=d[0],
            comissao_plat=d[1],
            razao_social=d[2],
            cnpj=d[3]
        )for d in rows
    ]
@router.put("/{id_desenvolvedora}")
async def atualizar_desenvolvedora(id_desenvolvedora: int, des: DesenvolvedorUpdate):
    # Garanta que o nome do modelo está como DesenvolvedorUpdate (conforme seu import no topo do arquivo)
    conn = get_connection()
    cur = conn.cursor()

    try:
        # Corrigido: adicionado o nome da tabela (desenvolvedor) e os campos corretos
        query = """
            UPDATE desenvolvedora 
            SET comissao_plat=%s, razao_social=%s, cnpj=%s 
            WHERE id_desenvolvedora=%s
        """
        valores = (des.comissao_plat, des.razao_social, des.cnpj, id_desenvolvedora)
        
        cur.execute(query, valores)
        conn.commit()
        
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar a Desenvolvedora: {e}")
    finally:
        cur.close()
        conn.close()

    return {"msg": "Desenvolvedora atualizada com SUCESSO"}


@router.delete("/{id_desenvolvedora}")
async def deletar_desenvolvedora(id_desenvolvedora: int):
    conn = get_connection()
    cur = conn.cursor()

    try:
        # Atualizado para deletar da tabela desenvolvedor usando o ID correto
        query = "DELETE FROM desenvolvedora WHERE id_desenvolvedora=%s"
        cur.execute(query, (id_desenvolvedora,))
        conn.commit()
        
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao deletar a Desenvolvedora: {e}")
    finally:
        cur.close()
        conn.close()

    return {"msg": "Desenvolvedora deletada com SUCESSO"}
