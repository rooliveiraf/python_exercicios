primeiro = int(input("Insira aqui o primeiro número: "))
segundo = int(input("Insira aqui o segundo número: " ))

x = primeiro
resultado = 0

while x >= segundo:
    x = x - segundo
    resultado = resultado + 1
resto = x
print("%d / %d = %d . O resto é %d." % (primeiro, segundo, resultado, resto))
