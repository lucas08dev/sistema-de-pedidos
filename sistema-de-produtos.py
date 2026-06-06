produtos = []
pedidos = []


def cadastro_de_produto():
    print("=== Cadastro de Produto ===")

    nome_do_produto = input("Nome do produto: ")
    preco = float(input("Preco: "))
    estoque = int(input("Estoque: "))

    if preco < 0:
        print("O preco nao pode ser negativo.")
        return

    if estoque < 0:
        print("O estoque nao pode ser negativo.")
        return

    produto = {
        "id": len(produtos) + 1,
        "nome": nome_do_produto,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)

    print("Produto cadastrado com sucesso!")


def listar_produtos():
    print("=== Lista de Produtos ===")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print("ID:", produto["id"])
        print("Nome:", produto["nome"])
        print("Preco: R$", produto["preco"])
        print("Estoque:", produto["estoque"])
        print()


def criar_pedido():
    print("=== Criar Pedido ===")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    listar_produtos()

    produto_id = int(input("Digite o ID do produto: "))
    quantidade = int(input("Digite a quantidade: "))

    if quantidade <= 0:
        print("A quantidade precisa ser maior que zero.")
        return

    produto_encontrado = None

    for produto in produtos:
        if produto["id"] == produto_id:
            produto_encontrado = produto
            break

    if produto_encontrado == None:
        print("Produto nao encontrado.")
        return

    if quantidade > produto_encontrado["estoque"]:
        print("Estoque insuficiente.")
        return

    pedido = {
        "id": len(pedidos) + 1,
        "produto_id": produto_encontrado["id"],
        "produto_nome": produto_encontrado["nome"],
        "quantidade": quantidade,
        "total": produto_encontrado["preco"] * quantidade,
        "status": "pendente"
    }

    pedidos.append(pedido)

    print("Pedido criado com sucesso!")
    print("Status: pendente")


def processamento_pedido():
    print("=== Processamento de Pedido ===")

    pedido_encontrado = None

    for pedido in pedidos:
        if pedido["status"] == "pendente":
            pedido_encontrado = pedido
            break

    if pedido_encontrado == None:
        print("Nenhum pedido pendente.")
        return

    print("Processando pedido #", pedido_encontrado["id"])
    pedido_encontrado["status"] = "processando"

    produto_encontrado = None

    for produto in produtos:
        if produto["id"] == pedido_encontrado["produto_id"]:
            produto_encontrado = produto
            break

    if produto_encontrado == None:
        pedido_encontrado["status"] = "cancelado"
        print("Produto nao encontrado. Pedido cancelado.")
        return

    if pedido_encontrado["quantidade"] > produto_encontrado["estoque"]:
        pedido_encontrado["status"] = "cancelado"
        print("Estoque insuficiente. Pedido cancelado.")
        return

    produto_encontrado["estoque"] -= pedido_encontrado["quantidade"]
    pedido_encontrado["status"] = "concluido"

    print("Pedido concluido com sucesso!")


def relatorio():
    print("=== Relatorios ===")

    total_vendido = 0
    pedidos_cancelados = 0
    vendas_por_produto = {}

    for pedido in pedidos:
        if pedido["status"] == "concluido":
            total_vendido += pedido["total"]

            nome = pedido["produto_nome"]
            quantidade = pedido["quantidade"]

            if nome not in vendas_por_produto:
                vendas_por_produto[nome] = 0

            vendas_por_produto[nome] += quantidade

        if pedido["status"] == "cancelado":
            pedidos_cancelados += 1

    produto_mais_vendido = None
    maior_quantidade = 0

    for nome in vendas_por_produto:
        if vendas_por_produto[nome] > maior_quantidade:
            maior_quantidade = vendas_por_produto[nome]
            produto_mais_vendido = nome

    print("Total vendido: R$", total_vendido)

    if produto_mais_vendido == None:
        print("Produto mais vendido: nenhum")
    else:
        print("Produto mais vendido:", produto_mais_vendido)

    print("Pedidos cancelados:", pedidos_cancelados)
    print("=== Estoque Atual ===")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(produto["nome"], "-", produto["estoque"], "unidades")


opcao = 0

while opcao != 6:
    print()
    print("=== Sistema de Pedidos ===")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Criar pedido")
    print("4. Processar proximo pedido")
    print("5. Ver relatorios")
    print("6. Sair")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        cadastro_de_produto()

    elif opcao == 2:
        listar_produtos()

    elif opcao == 3:
        criar_pedido()

    elif opcao == 4:
        processamento_pedido()

    elif opcao == 5:
        relatorio()

    elif opcao == 6:
        print("Saindo do sistema...")

    else:
        print("Opcao invalida.")