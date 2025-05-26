CREATE_TABLE_ENDERECO = """
CREATE TABLE IF NOT EXISTS Endereco (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cep TEXT NOT NULL,
    logradouro TEXT NOT NULL,
    numero TEXT NOT NULL,
    complemento TEXT NOT NULL,
    bairro TEXT NOT NULL,
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL);
"""

INSERT_ENDERECO = """
INSERT INTO Endereco (cep, logradouro, numero, complemento, bairro, cidade, estado)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""

UPDATE_ENDERECO = """
UPDATE Endereco
SET cep = ?, logradouro = ?, numero = ?, complemento = ?, bairro = ?, cidade = ?, estado = ?
WHERE id = ?;
"""

DELETE_ENDERECO = """
DELETE FROM Endereco
WHERE id = ?;
"""

GET_ENDERECO_BY_ID = """
SELECT id, cep, logradouro, numero, complemento, bairro, cidade, estado
FROM Endereco
WHERE id = ?;
"""

GET_ENDERECOS_BY_PAGE = """
SELECT id, cep, logradouro, numero, complemento, bairro, cidade, estado
FROM Endereco
ORDER BY cep ASC
LIMIT ? OFFSET ?;
"""
