CREATE_TABLE_CLIENTE = """
CREATE TABLE IF NOT EXISTS Cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL unique,
    email TEXT NOT NULL unique,
    telefone TEXT NOT NULL unique,
    data_nascimento TEXT NOT NULL,
);
"""
INSERT_CLIENTE = """
INSERT INTO Cliente (nome, cpf, email, telefone, data_nascimento)
VALUES (?, ?, ?, ?, ?);
"""
UPDATE_CLIENTE = """
UPDATE Cliente
SET nome = ?, cpf = ?, email = ?, telefone = ?, data_nascimento = ?
WHERE id = ?;
"""
DELETE_CLIENTE = """
DELETE FROM Cliente
WHERE id = ?;
"""
GET_CLIENTE_BY_ID = """
SELECT id, nome, cpf, email, telefone, data_nascimento
FROM Cliente
WHERE id = ?;
"""
GET_CLIENTE_BY_PAGE = """
SELECT id, nome, cpf, email, telefone, data_nascimento
FROM Cliente
ORDER BY nome ASC
LIMIT ? OFFSET ?;
"""