from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.get_most_repeated_company import\
    calculate_quantity_of_products_by_company


class CompleteReport(SimpleReport):
    # def __init__(self):
    #     super().__init__()

    @classmethod
    def generate(cls, product_list):
        first_string = super().generate(product_list)
        first_string += "\n"
        nomes_das_empresas = [e["nome_da_empresa"] for e in product_list]
        # print(product_list[0]['nome_da_empresa'])
        quantidade_por_empresa =\
            calculate_quantity_of_products_by_company(nomes_das_empresas)
        empresas_qtd_string = [
            f"- {empresa['nome']}: {empresa['qtd']}\n"
            for empresa in quantidade_por_empresa
        ]
        produtos_estocados_por_empresa = "Produtos estocados por empresa:\n"
        # print(first_string)
        # print(empresas_qtd_string)
        final_string =\
            first_string + produtos_estocados_por_empresa
        print(final_string)
        for empresa in empresas_qtd_string:
            final_string += empresa
        return final_string
