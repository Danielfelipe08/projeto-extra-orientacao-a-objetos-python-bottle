class Produto:
    def __init__(self, id: int, nome: str, preco: float):
        self.id = id
        self.nome = nome
        self.preco = preco

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco
        }
