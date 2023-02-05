from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.get_most_repeated_company import\
    calculate_quantity_of_products_by_company


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, product_list):
        first_string = super().generate(product_list)
        first_string += "\n"
        nomes_das_empresas = [e["nome_da_empresa"] for e in product_list]
        quantidade_por_empresa =\
            calculate_quantity_of_products_by_company(nomes_das_empresas)
        quantidade_por_empresa_sem_repetir = list()
        for empresa in quantidade_por_empresa:
            if empresa not in quantidade_por_empresa_sem_repetir:
                quantidade_por_empresa_sem_repetir.append(empresa)
        empresas_qtd_string = [
            f"- {empresa['nome']}: {empresa['qtd']}\n"
            for empresa in quantidade_por_empresa_sem_repetir
        ]
        produtos_estocados_por_empresa = "Produtos estocados por empresa:\n"
        final_string =\
            first_string + produtos_estocados_por_empresa
        for empresa in empresas_qtd_string:
            final_string += empresa
        print(final_string)
        return final_string
