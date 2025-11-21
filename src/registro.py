def registrar_cliente():
    nombre = input("Ingrese el nombre: ")
    while len(nombre) < 3 or not nombre.isalpha():
        print("El nombre debe tener al menos 3 letras y no puede contener números.")
        nombre = input("Ingrese el nombre: ")

    apellido = input("Ingrese el apellido: ")
    while len(apellido) < 3 or not apellido.isalpha():
        print("El apellido debe tener al menos 3 letras y no puede contener números.")
        apellido = input("Ingrese el apellido: ")

    documento = input("Ingrese el documento: ")
    while len(documento) < 3 or len(documento) > 15 or not documento.isdigit():
        print("El documento debe tener entre 3 y 15 dígitos y solo puede contener números.")
        documento = input("Ingrese el documento: ")

    print("Cliente registrado con éxito!")
    print(f"Nombre: {nombre} {apellido}")
    print(f"Documento: {documento}")
