from reiniciar import reiniciar_votacion
votos_registrados = {}

conteo_opciones = {
    "Candidato A": 0,
    "Candidato B": 0,
    "Voto en Blanco": 0
}

def registrar_voto():
    print("\n--- REGISTRAR VOTO ---")
    documento = input("Ingrese su documento de identidad: ").strip()
    
    # Rama 1: Validar con diccionario que no vote 2 veces la misma persona
    if documento in votos_registrados:
        print("❌ Error: Esta persona ya registró su voto. ¡No se permite votar dos veces!")
        return
    
    print("\nOpciones disponibles para votar:")
    for opcion in conteo_opciones.keys():
        print(f"- {opcion}")
        
    voto = input("Escriba exactamente el nombre de su opción: ").strip()
    
    if voto in conteo_opciones:
        votos_registrados[documento] = voto
        conteo_opciones[voto] += 1
        print("✅ ¡Voto registrado exitosamente!")
    else:
        print("❌ Opción no válida. Inténtelo de nuevo.")

def ver_resultados():
    print("\n--- RESULTADOS DE LA VOTACIÓN ---")
    total_votos = len(votos_registrados)
    
    if total_votos == 0:
        print("Aún no hay votos registrados.")
        return
        
    print(f"Total de votos emitidos: {total_votos}\n")
    
    # Rama 2: Mostrar porcentajes además de los conteos
    for opcion, cantidad in conteo_opciones.items():
        porcentaje = (cantidad / total_votos) * 100
        print(f"🗳️ {opcion}: {cantidad} votos ({porcentaje:.2f}%)")
    ganador = max(conteo_opciones, key=conteo_opciones.get)
    print(f"\n🏆 Ganador de la votación: {ganador}")

def menu():
    while True:
        print("\n==============================")
        print("      SISTEMA DE VOTACIÓN     ")
        print("==============================")
        print("1. Registrar voto")
        print("2. Ver resultados")
        print("3. Reiniciar votación")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_voto()
        elif opcion == "2":
            ver_resultados()
        elif opcion == "3":
            reiniciar_votacion(votos_registrados, conteo_opciones)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
