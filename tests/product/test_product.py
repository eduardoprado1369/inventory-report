from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(1, 'iPhone', 'Apple', '31/01/2023', '31/01/2033',
                      '5398684', 'Armazenar com cuidado')
    assert(type(product.id)) == int
    assert(type(product.nome_do_produto)) == str
    assert(type(product.nome_da_empresa)) == str
    assert(type(product.data_de_fabricacao)) == str
    assert(type(product.data_de_validade)) == str
    assert(type(product.numero_de_serie)) == str
    assert(type(product.instrucoes_de_armazenamento)) == str
    assert(product.id) == 1
    assert(product.nome_do_produto) == 'iPhone'
    assert(product.nome_da_empresa) == 'Apple'
    assert(product.data_de_fabricacao) == '31/01/2023'
    assert(product.data_de_validade) == '31/01/2033'
    assert(product.numero_de_serie) == '5398684'
    assert(product.instrucoes_de_armazenamento) == 'Armazenar com cuidado'
