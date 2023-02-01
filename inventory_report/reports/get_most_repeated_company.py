def get_most_repeated_company(product_list: list):
    empresa_que_mais_repete = {"nome": "none", "qtd": 0}
    nomes_de_todas_empresas = list()
    for produto in product_list:
        # print(produto["nome_da_empresa"])
        nomes_de_todas_empresas.append(produto["nome_da_empresa"])
    # print('chegou')
    print(nomes_de_todas_empresas)
    # qtd_de_produtos_por_empresa = dict()
    lista_de_empresas = list()
    for nome in nomes_de_todas_empresas:
        lista_de_empresas.append(
                {"nome": nome, "qtd": 0},
                )
    for nome in nomes_de_todas_empresas:
        for empresa in lista_de_empresas:
            if nome == empresa["nome"]:
                empresa["qtd"] += 1
    for empresa in lista_de_empresas:
        if empresa["qtd"] > empresa_que_mais_repete["qtd"]:
            empresa_que_mais_repete = empresa
    return empresa_que_mais_repete["nome"]
