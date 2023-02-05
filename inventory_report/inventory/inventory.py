from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def import_data(file_path: str, type: str):
        if file_path.endswith(".csv"):
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                product_list = list(reader)
        elif file_path.endswith(".json"):
            with open(file_path) as file:
                product_list = json.load(file)
        elif file_path.endswith(".xml"):
            with open(file_path) as file:
                xmlfile = file.read()
                product_list = xmltodict.parse(xmlfile)["dataset"]["record"]
                print(product_list)
        if type == "simples":
            report = SimpleReport.generate(product_list)
            return report
        report = CompleteReport.generate(product_list)
        return report
