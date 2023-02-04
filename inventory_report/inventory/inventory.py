from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(file_path: str, type: str):
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            product_list = list(reader)
        if type == "simples":
            return SimpleReport.generate(product_list)
        if type == "completo":
            return CompleteReport.generate(product_list)
