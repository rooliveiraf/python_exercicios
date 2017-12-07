salario = float(input("Insira aqui o salário a receber o aumento (R$): "))

if salario > 1250:
    aumento = salario * 0.15
    total = salario + aumento

    print("O aumento do seu salário será de R$ %5.2f." % (aumento))
    print("O valor final do seu salário será de R$ %5.2f." % (total))

if salario <= 1250:
    aumento = salario * 0.15
    total = salario + aumento

    print("O aumento do seu salário será de R$ %5.2f." % (aumento))
    print("O valor final do seu salário será de R$ %5.2f." % (total))
