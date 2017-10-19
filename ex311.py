preço = float(input("Preço da mercadoria:"))
desconto = float(input("% de desconto:"))
valor_do_desconto = preço * desconto / 100
preço_a_pagar = preço - valor_do_desconto
print("Valor do desconto: %7.2f" % valor_do_desconto)
print("Preço a pagar: %7.2f" % preço_a_pagar)
