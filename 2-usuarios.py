usuarios = {"Marcela", "David", "Elvira", "Juan", "Marcos"}

administradores = {"Juan", "Marcela"}

administradores.discard("Juan")

administradores.add("Marcos")

for usuario in usuarios:
    if usuario in administradores:
        print(f"{usuario} es administrador/a")
    else:
        print(f"{usuario} no es administrador/a")
