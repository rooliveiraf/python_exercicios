km=int(input("Km percorridos:"))
dias=int(input("Dias com o carro:"))
preço_dia=60
preço_km=0.15
preço_a_pagar=km * preço_km + dias * preço_dia
print("Total a pagar: R$ %7.2f" % preço_a_pagar)
