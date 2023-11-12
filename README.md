# Challenge API

[![Python](https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=flat&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)

Acesse em: https://amcom-project.onrender.com/api/

## Sobre o projeto

Esta é uma API REST utilizada para registrar vendas e calcular a comissão dos vendedores com base nas vendas feitas em dado período e nos percentuais de comissão cadastrados nos produtos vendidos.

Para o desenvolvimento dessa aplicação foram utilizadas as seguintes tecnologias:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)

## Funcionalidades
- Permite cadastrar produtos com código de barras, valor unitário, descrição e percentual de comissão.
- Permite cadastrar clientes e vendedores com nome, e-mail e telefone.
- Permite o registrar vendas com código de vendedor, id do cliente e uma lista de produtos com seus respectivos ids e quantidades.
- Permite configurar os dias da semana com seus respectivos percentuais mínimos e máximos de comissão.
- Permite editar produtos, clientes, vendedores e vendas.
- Permite deletar produtos, clientes, vendedores e vendas.
- Permite listar produtos, clientes, vendedores e vendas, calculando o total da venda, o total de itens e o total de comissões sobre os itens vendidos.
- Permite obter uma lista de vendedores com o valor total de comissões a ser pago a cada um pelas vendas no período especificado.

## Como utilizar

1. Baixe a versão 3.10 do Python

2. Clone este repositório

```
git clone https://github.com/LorraneAlkimim/challenge-api.git
```

3. Crie e ative o ambiente virtual

```
python -m venv venv

source env/bin/activate
```

4. Instale as dependências

```
pip install -r requirements.txt
```

5. Aplique as migrações

```
python manage.py migrate
```

6. Crie um super usuário

```
python manage.py createsuperuser
```

7. Execute a aplicação

```
python manage.py runserver
```

## Implementações futuras

- Cadastro de usuários
- Sistema de login com níveis de permissões
- Adicionar filtros na listagem de venda
- Exportação de relatório de vendas e comissões
