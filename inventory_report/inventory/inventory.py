from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @staticmethod
    def import_data(file_path: str, type: str):
        # print(file_path)
        if file_path.endswith(".csv"):
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                product_list = list(reader)
                print(product_list[0]["nome_da_empresa"])
        elif file_path.endswith(".json"):
            with open(file_path) as file:
                product_list = json.load(file)
                print(product_list)
        if type == "simples":
            report = SimpleReport.generate(product_list)
            # print(report)
            return report
        if type == "completo":
            report = CompleteReport.generate(product_list)
            # print(report)
            return report
