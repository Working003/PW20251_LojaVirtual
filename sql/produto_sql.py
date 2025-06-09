CREATE_TABLE_PRODUTO = """
CREATE TABLE IF NOT EXISTS Produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL,
    imagem TEXT NOT NULL
);
"""

INSERT_PRODUTO = """
INSERT INTO Produto (nome, descricao, preco, estoque, imagem) 
VALUES (?, ?, ?, ?, ?);
"""

UPDATE_PRODUTO = """
UPDATE Produto 
SET nome = ?, descricao = ?, preco = ?, estoque = ?, imagem = ?
WHERE id = ?;
"""

DELETE_PRODUTO = """
DELETE FROM Produto 
WHERE id = ?;
"""

GET_PRODUTO_BY_ID = """
SELECT id, nome, descricao, preco, estoque, imagem
FROM Produto
WHERE id = ?;
"""

GET_PRODUTOS_BY_PAGE = """
SELECT id, nome, descricao, preco, estoque, imagem
FROM Produto 
ORDER BY nome ASC
LIMIT ? OFFSET ?;
"""