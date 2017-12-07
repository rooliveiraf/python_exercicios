valor_casa = float(input("Valor do imóvel a ser comprado: "))
salario = float(input("Salário do comprador: "))
anos = float(input("Anos para quitar o imóvel: "))

meses = anos * 12

prestacao = float((valor_casa / meses))

if prestacao > (0.3 * salario):
    print("Empréstimo negado! Risco de inadimplência dado a relação prestação/salário.")
    
else:
    print("Empréstimo concedido! O valor mensal da parcela é de R$ %6.2f." % (prestacao))
