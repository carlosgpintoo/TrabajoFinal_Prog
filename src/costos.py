precios = {
    'habitacion_individual': 100,
    'habitacion_pareja': 170,
    'habitacion_familia': 260,
    'comida': 30,
    'paseo': 90,
    'mascota': 60
}

def calcular_costos(tipo_habitacion, comida, paseo, cantidad_mascotas):
    
    if tipo_habitacion == "individual":
        costo_habitacion = precios['habitacion_individual']
    elif tipo_habitacion == "pareja":
        costo_habitacion = precios['habitacion_pareja']
    elif tipo_habitacion == "familia":
        costo_habitacion = precios['habitacion_familia']
    else:
        print("Tipo de habitación no válido.")
        return

    
    costo_comida = comida * precios['comida']
    costo_paseo = paseo * precios['paseo']
    costo_mascotas = cantidad_mascotas * precios['mascota']
    
    total = costo_habitacion + costo_comida + costo_paseo + costo_mascotas
    
    
    print(f"Costo total de la reserva: ${total}")
    print(f"Resuemn de la reserva: \n- Habitación: ${costo_habitacion} \n- Comidas: ${costo_comida} \n- Paseos: ${costo_paseo} \n- Mascotas: ${costo_mascotas}")


tipo_habitacion = input("Ingrese el tipo de habitación (individual, pareja, familia): ").lower()
comida = int(input("¿Cuántas comidas adicionales? "))
paseo = int(input("¿Cuántos paseos adicionales? "))
cantidad_mascotas = int(input("¿Cuántas mascotas? "))


calcular_costos(tipo_habitacion, comida, paseo, cantidad_mascotas)
