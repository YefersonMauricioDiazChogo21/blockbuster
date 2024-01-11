import json

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
peli="peliculas.json"
with open(peli) as json_file:
    json.dumps(peliculas, json_file, indent=4)

generos={
    "G01":{
        "id":"G01",
        "nombre":""
    }
}
gen="generos.json"
with open(gen) as json_file:
    json.dumps(generos, json_file, indent=4)


actores={
    "A01":{
        "id":"A01",
        "nombre":"",
    }
}
act="actores.json"
with open(act) as json_file:
    json.dumps(actores, json_file, indent=4)

formatos={
    "F01":{
        "id":"F01",
        "nombre":""
    }
}
fmt="formatos.json"
with open(fmt) as json_file:
    json.dumps(formatos, json_file, indent=4)