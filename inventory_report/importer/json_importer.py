from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file_path: str):
        if not file_path.endswith('.json'):
            raise ValueError("Arquivo inválido")
        with open(file_path) as file:
            product_list = json.load(file)
        if type == "simples":
            report = SimpleReport.generate(product_list)
            return report
        return CompleteReport.generate(product_list)
