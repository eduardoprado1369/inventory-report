from inventory_report.reports.calculate_oldest_date\
     import calculate_oldest_date
from inventory_report.reports.get_most_repeated_company\
     import get_most_repeated_company


class SimpleReport:
    @staticmethod
    def generate(product_list):
        # print(type(product_list[0]["nome_da_empresa"]))
        data_mais_antiga = calculate_oldest_date(product_list,
                                                 "data_de_fabricacao")
        data_mais_recente = calculate_oldest_date(product_list,
                                                  "data_de_validade")
        empresa_que_mais_repete = get_most_repeated_company(product_list)
        final_string = (
                f"Data de fabricação mais antiga: {data_mais_antiga}\n"
                f"Data de validade mais próxima: {data_mais_recente}\n"
                f"Empresa com mais produtos: {empresa_que_mais_repete}"
            )
        return final_string
