import json
import os
from models.produto import Produto

DATA_PATH = os.path.join("data", "produtos.json")


class ProdutoService:

    @staticmethod
    def get_all():
        if not os.path.exists(DATA_PATH):
            return []

        with open(DATA_PATH, "r") as f:
            data = json.load(f)

        return [Produto(**item) for item in data]

    @staticmethod
    def add_produto(produto: Produto):
        produtos = ProdutoService.get_all()
        produtos.append(produto)

        with open(DATA_PATH, "w") as f:
            json.dump([p.to_dict() for p in produtos], f, indent=4)

    @staticmethod
    def get_by_id(produto_id: int):
        produtos = ProdutoService.get_all()
        for p in produtos:
            if p.id == produto_id:
                return p
        return None

    @staticmethod
    def delete_produto(produto_id: int):
        produtos = ProdutoService.get_all()
        produtos = [p for p in produtos if p.id != produto_id]

        with open(DATA_PATH, "w") as f:
            json.dump([p.to_dict() for p in produtos], f, indent=4)
