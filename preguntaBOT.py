import tratarJS as js


def pregunta(pregunta):
    concepto = _mayorAfinidad(pregunta)
    definiciones = js.extrae_dato_json('definiciones.json',concepto)
    definicion_buena = salto_de_linea(definiciones)
    return [concepto,definicion_buena]

def _mayorAfinidad(pregunta):
    # Podría ser utilizada la "Distancia de levenshtein" para encontrar mayor afinidad
    palabrasObviadas = ["si","con","para","a","el","la","los","las","lo","los","es","un","que","te","me"]
    palabrasPregunta = pregunta.lower()
    definiciones = js.lee_json('definiciones.json')
    masAfinidad = {}
    palabrasMatch = []

    for definicion in definiciones:
        masAfinidad[definicion] = 0
        for palabraDefinicion in definiciones[definicion][0].lower().split():
            for palabraPregunta in palabrasPregunta.split():
                if(palabraDefinicion == palabraPregunta and palabraPregunta not in palabrasObviadas):
                    palabrasMatch.append(palabraDefinicion)
                    masAfinidad[definicion] += 1
                    
    #print(masAfinidad)
    max_key = max(masAfinidad, key=masAfinidad.get)
    
    if(len(palabrasMatch) != 0):
        print('Palabras match: ' + ", ".join(palabrasMatch)+".")

    return max_key

def salto_de_linea(definicion):
    contador = 0
    definicion_buena = ""
    for i in definicion[0]:
        if(contador > 77):
            if (i == " "):
                definicion_buena = definicion_buena + "\n"
            else:
                print("letra: " + i)
                print("definicion: "+ definicion_buena)
                definicion_buena = definicion_buena + "-"
                definicion_buena = definicion_buena + "\n"
            
            contador = 0
        contador += 1
        definicion_buena = definicion_buena + i
    return definicion_buena


if __name__ == '__main__':
    respuesta = pregunta('php')
    print(respuesta[0])
    print(respuesta)