def reiniciar_votacion(votos, historial):
    with open("historial.txt", "a") as archivo:
        archivo.write("Historial de votacion:\n")
        archivo.write(str(historial) + "\n")

    votos.clear()

    print("La votacion ha sido reiniciada.")