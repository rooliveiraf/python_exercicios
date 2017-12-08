primeiro = int(input("Insira aqui o primeiro número: "))
segundo = int(input("Insira aqui o segundo número: " ))

x = 1
resultado = 0

while x <= segundo:
    resultado = resultado + primeiro
    x = x + 1

print("%dx%d = %d" % (primeiro, segundo, resultado))
