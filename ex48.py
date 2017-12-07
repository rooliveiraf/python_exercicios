a = int(input("Digite aqui número: "))
b = int(input("Digite aqui outro número: "))
operacao = input("Qual operação básica deseja realizar (+, -, *, /)? ")

if operacao == "+":
    calculo = a+b
elif operacao == "-":
    calculo = a-b
elif operacao == "*":
    calculo = a*b
elif operacao == "/":
    calculo = a/b
else:
    print("Operação inválida")
    resultado = 0

print("O resultado da operação solicitada é %d." % (calculo))
