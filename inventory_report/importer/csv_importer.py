from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(file_path: str):
        # print('entrou')
        if not file_path.endswith('.csv'):
            raise ValueError("Arquivo inválido")
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            product_list = list(reader)
        if type == "simples":
            print('simples')
            report = SimpleReport.generate(product_list)
            return report
        # report = CompleteReport.generate(product_list)
        print('completo')
        # print(report)
        return product_list
