usuariosInfo = []

def ingresarInfoUsuario():
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    direccion = input("Ingrese la direccion: ")
    telefono = input("Ingrese el telefono: ")

    usuario = {
        'Nombre': nombre,
        'Edad': edad,
        'Dirección': direccion,
        'Teléfono': telefono
    }

    usuariosInfo.append(usuario)

while True:
    ingresarInfoUsuario()
    continuar = input("Ingresar otro usuario? ´s´ o ´n´: ").lower()
    if continuar != 's':
        break

for i, usuario in enumerate(usuariosInfo, 1):
    print(f"Información del Usuario {i}:")
    for clave, valor in usuario.items():
        print(f"{clave}: {valor}")
    print()