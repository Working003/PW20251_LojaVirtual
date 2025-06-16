from datetime import datetime
from typing import Optional
from data.database import obter_conexao
from sql.cliente_sql import *
from models.cliente import Cliente

def criar_tabela_clientes() -> bool:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(CREATE_TABLE_CLIENTE)        
        return (cursor.rowcount > 0)

def inserir_cliente(cliente: Cliente) -> Cliente:    
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(INSERT_CLIENTE, 
            (cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.data_nascimento))
        cliente.id = cursor.lastrowid
        return cliente

def atualizar_cliente(cliente: Cliente) -> bool:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(UPDATE_CLIENTE, 
            (cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.data_nascimento, cliente.id))    
        return (cursor.rowcount > 0)

def excluir_cliente(id: int) -> bool:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(DELETE_CLIENTE, (id,))
        return (cursor.rowcount > 0)    

def obter_cliente_por_id(id: int) -> Optional[Cliente]:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(GET_CLIENTE_BY_ID, (id,))
        resultado = cursor.fetchone()
        if resultado:
            return Cliente(
                id=resultado["id"],
                nome=resultado["nome"],
                cpf=resultado["cpf"],
                telefone=resultado["telefone"],
                email=resultado["email"],
                data_nascimento=datetime.strptime(resultado["data_nascimento"], "%Y-%m-%d").date())
    return None

def obter_cliente_por_email(email: str) -> Optional[Cliente]:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(GET_CLIENTE_BY_EMAIL, (email,))
        resultado = cursor.fetchone()
        if resultado:
            return Cliente(
                id=resultado["id"],
                nome=resultado["nome"],
                cpf=resultado["cpf"],
                telefone=resultado["telefone"],
                email=resultado["email"],
                data_nascimento=datetime.strptime(resultado["data_nascimento"], "%Y-%m-%d").date(),
                senha_hashed=resultado["senha_hashed"]
            )
    return None

def obter_clientes_por_pagina(numero_pagina: int, tamanho_pagina: int) -> list[Cliente]:
    with obter_conexao() as conexao:
        limite = tamanho_pagina
        offset = (numero_pagina - 1) * tamanho_pagina
        cursor = conexao.cursor()
        cursor.execute(GET_CLIENTES_BY_PAGE, (limite, offset))
        resultados = cursor.fetchall()
        return [Cliente(
            id=resultado["id"],
            nome=resultado["nome"],
            cpf=resultado["cpf"],
            telefone=resultado["telefone"],
            email=resultado["email"],
            data_nascimento=datetime.strptime(resultado["data_nascimento"], "%Y-%m-%d").date()
        ) for resultado in resultados]