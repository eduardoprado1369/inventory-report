from datetime import datetime
from inventory_report.reports.calculate_oldest_date\
     import calculate_oldest_date
from inventory_report.reports.get_most_repeated_company\
     import get_most_repeated_company


class SimpleReport:
    def __init__(self, product_list: list) -> None:
        self.data_mais_antiga = datetime.strftime('0000/00/01')
        self.data_mais_recente = datetime.strftime('0000/00/01')
        self.empresa_que_mais_repete = {"nome_da_empresa": "none", "qtd": 0}
        nomes_de_todas_empresas = {nome for nome in product_list}
        # for data in product_list["data_de_fabricacao"]:
        #     if datetime.strftime(data, '%Y-%m-%d') >\
        #          datetime.strftime(self.data_mais_antiga, '%Y-%m-%d'):
        #         self.data_mais_antiga = datetime.strftime(data, '%Y-%m-%d')
        # for data in product_list["data_de_validade"]:
        #     if datetime.strftime(data, '%Y-%m-%d') >\
        #          datetime.strftime(self.data_mais_recente, '%Y-%m-%d'):
        #         self.data_mais_recente = datetime.strftime(data, '%Y-%m-%d')
        qtd_de_produtos_por_empresa = dict()
        qtd_de_produtos_por_empresa.update(
            {"nome": nome for nome in nomes_de_todas_empresas},
            {"qtd": 0})
        for empresa in qtd_de_produtos_por_empresa:
            if empresa["qtd"] > self.empresa_que_mais_repete["qtd"]:
                self.empresa_que_mais_repete = empresa

    @classmethod
    def generate(self, product_list):
        data_mais_antiga = calculate_oldest_date(product_list,
                                                 "data_de_fabricacao")
        data_mais_recente = calculate_oldest_date(product_list,
                                                  "data_de_validade")
        empresa_que_mais_repete = get_most_repeated_company(product_list)
        response = f"""
        Data de fabricação mais antiga: \
        {data_mais_antiga}
        Data de validade mais próxima: \
        {data_mais_recente}
        Empresa com mais produtos: {empresa_que_mais_repete}
        """
        return response
