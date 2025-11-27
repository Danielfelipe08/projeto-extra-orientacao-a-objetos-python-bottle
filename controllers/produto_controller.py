from bottle import template, request, response



def init_controllers(app):

    @app.route('/produtos')
    def listar_produtos():
        from services.produto_service import ProdutoService
        produtos = ProdutoService.get_all()
        return template("produtos", title="Lista de Produtos", produtos=produtos)


    @app.route('/produtos/<id:int>')
    def detalhes_produto(id):
        from services.produto_service import ProdutoService
        produto = ProdutoService.get_by_id(id)
        if produto:
            return template("produto_detalhe", title="Detalhe do Produto", produto=produto)
        return "Produto não encontrado."

    @app.route('/produtos/add', method='POST')
    def adicionar_produto():
        from services.produto_service import ProdutoService
        from models.produto import Produto

        nome = request.forms.get('nome')
        preco = float(request.forms.get('preco', 0))

        produtos = ProdutoService.get_all()
        novo_id = len(produtos) + 1

        produto = Produto(id=novo_id, nome=nome, preco=preco)
        ProdutoService.add_produto(produto)

        response.status = 201
        return "Produto cadastrado com sucesso!"
