from dataclasses import dataclass


@dataclass
class Cliente:
    id: int
    nome: str
    cpf: str
    telefone: str
    email: str
    data_nascimento: datetime