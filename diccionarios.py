def run():
    mi_diccionario ={
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])
    poblacion_paises ={
        "Honduras": 9588000,
        "Brasil": 210145343,
        "Colombia": 50374424,
    }
    # print(poblacion_paises["Honduras"])
    # print(poblacion_paises["Brasil"])
    # print(poblacion_paises["Colombia"])
    # poblacion_paises.pop("Honduras")
    # print(poblacion_paises)
    # for pais in poblacion_paises.keys():
    #     print(pais)
    print(poblacion_paises.items())

if __name__ == "__main__":
    run()