numerosValidos = [0, 2, 4, 6, 8]

def obtenerNumero():
    while True:
        try:
            numero = int(input("Ingrese un numero del 0 al 9: "))
            if numero in numerosValidos:
                return numero
            else:
                print("Numero no valido, intente nuevamente.")
        except ValueError:
            print("Debe ingresar caracteres numericos.")


numeroIngresado = obtenerNumero()

if numeroIngresado in numerosValidos:
    print(f"El numero {numeroIngresado} esta en la lista de numeros.")
else:
    print(f"El numero {numeroIngresado} no esta en la lista de numeros.")
