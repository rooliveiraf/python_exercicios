a = int(input("Insira aqui o primeiro número: "))
b = int(input("Insira aqui o segundo número: "))
c = int(input("Insira aqui o terceiro número: "))

if a > b > c:
    print("%d é o maior número dentre os digitados." % (a))

if a > c > b:
    print("%d é o maior número dentre os digitados." % (a))

if b > a > c:
    print("%d é o maior número dentre os digitados." % (b))

if b > c > a:
    print("%d é o maior número dentre os digitados." % (b))

if c > a > b:
    print("%d é o maior número dentre os digitados." % (c))

if c > b > a:
    print("%d é o maior número dentre os digitados." % (c))

if a < b < c:
    print("%d é o menor número dentre os digitados." % (a))

if a < c < b:
    print("%d é o menor número dentre os digitados." % (a))

if b < a < c:
    print("%d é o menor número dentre os digitados." % (b))

if b < c < a:
    print("%d é o menor número dentre os digitados." % (b))

if c < a < b:
    print("%d é o menor número dentre os digitados." % (c))

if c < b < a:
    print("%d é o menor número dentre os digitados." % (c))
