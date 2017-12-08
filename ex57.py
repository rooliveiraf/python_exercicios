inicio = int(input("Digite aqui o início da tabuada: "))
fim = int(input("Digite aqui o fim da tabuada: "))
n = int(input("Tabuada de: "))

x = inicio
while x<= fim:
    print("%dx%d = %d" % (x, n, n*x))
    x = x + 1
