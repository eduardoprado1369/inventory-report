from datetime import datetime


def calculate_oldest_date(product_list: list, field: str):
    data_mais_antiga = datetime.strptime('2000/01/01', '%Y-%m-%d')
    for data in product_list[field]:
        if datetime.strptime(data, '%Y-%m-%d') >\
                 datetime.strftime(data_mais_antiga, '%Y-%m-%d'):
            data_mais_antiga = datetime.strftime(data, '%Y-%m-%d')
    return data_mais_antiga
