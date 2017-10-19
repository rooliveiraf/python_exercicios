valor=float(input("Valor da casa:"))
salário=float(input("Salário:"))
anos=int(input("Anos para quitar:"))
meses = anos * 12
prestacao = valor / meses
if prestacao > salário * 0.3:
    print("Negado")
else:
    print("Prestação: R$ %9.2f Empréstimo Concedido" % prestacao)
