from .user_controller import UserController
from .produto_controller import init_controllers as init_produto_controllers

def init_controllers(app):
    # Inicializar rotas de usuário
    UserController(app)

    # Inicializar rotas de produto
    init_produto_controllers(app)
