# calculadora  solo suma
primero = int(input('ingresa el primer numero: '))
segundo = int(input('ingresa el segundo numero: '))
signo = input("ingresa operacion: ")

if signo == "+":
    resultado = (primero + segundo)
    print("El resultado de la suma es : ", resultado)

if signo == "-":
    resultado = (primero - segundo)
    print("El resultado de la resta es : ", resultado)

if signo == "*":
    resultado = (primero * segundo)
    print("El resultado de la multiplicacion es : ", resultado)

if signo == "/":
    resultado = (primero / segundo)
    print("El resultado de la division es : ", resultado)

else:
    print("El simbolo ingresado no es valido")
