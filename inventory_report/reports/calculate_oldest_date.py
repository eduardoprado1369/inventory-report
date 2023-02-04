from datetime import datetime


def calculate_oldest_date(product_list: list, field: str):
    print(field)
    data_mais_antiga = datetime.strptime(product_list[0][field], '%Y-%m-%d')
    # print(type(data_mais_antiga))
    for data in product_list:
        if datetime.strptime(data[field], '%Y-%m-%d') <\
                 data_mais_antiga:
            data_mais_antiga = datetime.strptime(data[field], '%Y-%m-%d')
    return datetime.strftime(data_mais_antiga, '%Y-%m-%d')
