import json

def crea_json(ruta):
    with open(ruta , "w") as documento:
        json.dump({}, documento, indent=4, sort_keys=True)
    documento.close()

def guarda_dato_json(ruta,clave,valor):
    try:
        historico = lee_json(ruta)
        historico[clave] = valor
        with open(ruta , "w") as documento:
            json.dump(historico, documento, indent=4, sort_keys=True)
        documento.close()
    except Exception as error:
        print(error)
        print("Fallo en guarda_dato_json()")
        

def extrae_dato_json(json_ruta, clave):
    try:
        historico = lee_json(json_ruta)
        return historico[clave]
    except Exception as error:
        print(error)
        print("Fallo en extrae_dato_json()")

def lee_json(ruta):
    try:
        with open(ruta, "r") as documento:
            historico = json.load(documento)
        documento.close()
        return historico
    except Exception as error:
        print(error)
        print("Fallo en lee_json()")

def agrega_dato(json_ruta, clave,valor):
    try:
        with open(json_ruta) as archivo:
            json_completo = json.load(archivo)
        
        json_completo[clave] = valor

        with open(json_ruta, 'w') as json_file:
            json.dump(json_completo, json_file, indent=4, sort_keys=True)
    except Exception as e:
        print(f"Fallo en agrega_dato()\n{e}")


def json_ordenado(diccionario):
    try:
        sorted_dict = {}
        sorted_tuples = sorted(diccionario.items(), key=lambda item: item[1],reverse=True)
        sorted_dict = {clave: valor for clave, valor in sorted_tuples}
        return sorted_dict
    except Exception as e:
        print(f"Fallo en json_ordenado()\n{e}")



if __name__ == '__main__':
    #agrega_dato("../src/config/tier_tag.json","pepinillo",3)
    pass