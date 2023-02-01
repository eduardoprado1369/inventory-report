def get_most_repeated_company(product_list: list):
    nomes_das_empresas = get_company_names(product_list)
    empresa_que_mais_repete = {"nome": "none", "qtd": 0}
    lista_de_empresas = \
        calculate_quantity_of_products_by_company(nomes_das_empresas)
    for empresa in lista_de_empresas:
        if empresa["qtd"] > empresa_que_mais_repete["qtd"]:
            empresa_que_mais_repete = empresa
    return empresa_que_mais_repete["nome"]


def get_company_names(product_list: list):
    nomes_de_todas_empresas = list()
    for produto in product_list:
        nomes_de_todas_empresas.append(produto["nome_da_empresa"])
    return nomes_de_todas_empresas


def calculate_quantity_of_products_by_company(nomes_das_empresas):
    lista_de_empresas = list()
    for nome in nomes_das_empresas:
        lista_de_empresas.append(
                {"nome": nome, "qtd": 0},
                )
    for nome in nomes_das_empresas:
        for empresa in lista_de_empresas:
            if nome == empresa["nome"]:
                empresa["qtd"] += 1
    return lista_de_empresas
