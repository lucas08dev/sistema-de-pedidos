# 📦 Sistema de Gerenciamento de Pedidos

Sistema desenvolvido em Python para cadastro de produtos, criação e processamento de pedidos e geração de relatórios de vendas.

## 📌 Sobre o Projeto

O objetivo deste projeto é simular um sistema simples de gerenciamento de pedidos utilizado por lojas e comércios para controlar produtos, estoque e vendas.

O sistema permite:

* Cadastrar produtos
* Listar produtos cadastrados
* Criar pedidos
* Processar pedidos pendentes
* Atualizar estoque automaticamente
* Gerar relatórios de vendas

---

## 🚀 Funcionalidades

### 1. Cadastro de Produtos

Permite cadastrar novos produtos informando:

* Nome do produto
* Preço
* Quantidade em estoque

Validações implementadas:

* O preço não pode ser negativo
* O estoque não pode ser negativo

---

### 2. Listagem de Produtos

Exibe todos os produtos cadastrados contendo:

* ID
* Nome
* Preço
* Quantidade em estoque

---

### 3. Criação de Pedidos

O usuário pode selecionar um produto e informar a quantidade desejada.

O sistema verifica:

* Existência do produto
* Quantidade válida
* Disponibilidade em estoque

Os pedidos são criados inicialmente com status:

```text
pendente
```

---

### 4. Processamento de Pedidos

Processa o primeiro pedido pendente encontrado.

Fluxo do processamento:

```text
Pendente → Processando → Concluído
```

Caso ocorra algum problema:

```text
Pendente → Processando → Cancelado
```

Situações de cancelamento:

* Produto inexistente
* Estoque insuficiente

Quando concluído:

* O estoque é atualizado automaticamente
* O pedido é marcado como concluído

---

### 5. Relatórios

O sistema gera informações importantes sobre as vendas:

* Valor total vendido
* Produto mais vendido
* Quantidade de pedidos cancelados
* Estoque atual de todos os produtos

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Estruturas de dados (listas e dicionários)
* Funções
* Estruturas condicionais
* Estruturas de repetição

---

## 📂 Estrutura do Sistema

```text
Sistema de Pedidos
│
├── Cadastro de Produto
├── Listagem de Produtos
├── Criação de Pedido
├── Processamento de Pedido
├── Relatórios
└── Encerramento do Sistema
```

---

## ▶️ Como Executar

1. Certifique-se de ter o Python 3 instalado.

2. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

3. Acesse a pasta do projeto:

```bash
cd seu-repositorio
```

4. Execute o programa:

```bash
python sistema_pedidos.py
```

---

## 💡 Exemplo de Uso

```text
=== Sistema de Pedidos ===

1. Cadastrar produto
2. Listar produtos
3. Criar pedido
4. Processar proximo pedido
5. Ver relatorios
6. Sair
```

---

## 📚 Conceitos Aplicados

Durante o desenvolvimento foram utilizados conceitos fundamentais de programação:

* Manipulação de listas
* Manipulação de dicionários
* Funções
* Validação de dados
* Controle de fluxo
* Simulação de fila de pedidos
* Controle de estoque

---

## 👨‍💻 Autor

Desenvolvido por Lucas Silva de Abreu como projeto de prática em Python para aprendizado de lógica de programação, estruturas de dados e desenvolvimento de sistemas de gerenciamento.
