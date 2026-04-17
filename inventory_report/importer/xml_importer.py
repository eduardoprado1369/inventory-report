from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(file_path: str):
        if not file_path.endswith('.xml'):
            raise ValueError("Arquivo inválido")
        with open(file_path) as file:
            xmlfile = file.read()
            product_list = xmltodict.parse(xmlfile)["dataset"]["record"]
        if type == "simples":
            report = SimpleReport.generate(product_list)
            return report
        # return CompleteReport.generate(product_list)
        return product_list
