% rebase('layout.tpl')

<h2>Lista de Produtos</h2>

<ul>
    % for p in produtos:
        <li>
            <a href="/produtos/{{p.id}}">{{p.nome}} - R$ {{p.preco}}</a>
        </li>
    % end
</ul>

<form action="/produtos/add" method="post">
    <input type="text" name="nome" placeholder="Nome do produto">
    <input type="number" step="0.01" name="preco" placeholder="Preço">
    <button type="submit">Adicionar</button>
</form>
