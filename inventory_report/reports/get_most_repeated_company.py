def get_most_repeated_company(product_list: list):
    empresa_que_mais_repete = {"nome_da_empresa": "none", "qtd": 0}
    nomes_de_todas_empresas = {nome for nome in product_list}
    qtd_de_produtos_por_empresa = dict()
    qtd_de_produtos_por_empresa.update(
            {"nome": nome for nome in nomes_de_todas_empresas},
            {"qtd": 0})
    for empresa in qtd_de_produtos_por_empresa:
        if empresa["qtd"] > empresa_que_mais_repete["qtd"]:
            empresa_que_mais_repete = empresa
    return empresa_que_mais_repete
