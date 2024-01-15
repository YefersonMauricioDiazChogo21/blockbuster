import json
# gen="generos.json"
peli="peliculas.json"
with open(peli,"r") as json_file:
    generos = json.loads(json_file.read())
peliculas={"blockbuster":{
        "peliculas":{
            "P01":{
                "id":"P01",
                "nombre":"",
                "duracion":"",
                "sinopsis":"",
                "generos":{
                    "G01":{
                        "id":"G01",
                        "nombre":""
                    }
                },
                "actores":{
                    "A01":{
                        "id":"A01",
                        "nombre":"",
                        "rol":""
                    }
                },
                "formato":{
                    "F01":{
                        "id":"F01",
                        "nombre":"",
                        "NroCopias":"",
                        "valorPrestamo":""
                },
                "F02":{
                    "id":"F02",
                    "nombre":"",
                    "NroCopias":"",
                    "valorPrestamo":""
                }
            }
       }
    }
}
}


with open(peli, "w+") as json_file:
    json_file.write(json.dumps(peliculas, indent=4))

# generos={
#     "G01":{
#         "id":"G01",
#         "nombre":""
#     }
# }
# gen="generos.json"
# with open(gen, "w") as json_file:
#     json_file.write(json.dumps(generos, indent=4))


actores={
    "A01":{
        "id":"A01",
        "nombre":"",
    }
}
act="actores.json"
with open(act,"r") as json_file:
    generos = json.loads(json_file.read())
with open(act, "w") as json_file:
    json_file.write(json.dumps(actores, indent=4))

formatos={
    "F01":{
        "id":"F01",
        "nombre":""
    }
}
fmt="formatos.json"
with open(act,"r") as json_file:
    generos = json.loads(json_file.read())
with open(fmt, "w") as json_file:
    json_file.write(json.dumps(formatos, indent=4))