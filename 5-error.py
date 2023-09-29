#El error es que se esta intentando realizar una operacion con diferentes tipos de datos, uno "int" y el otro "string"

#para evitar que el programa se bloquee, se usa manejo de excepciones

try:
    resultado = 15 + "20"
except TypeError as e:
    print("Error: se esta intentando sumar un numero con un texto.")
