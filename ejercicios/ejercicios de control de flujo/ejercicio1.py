'''
Crear una lista de palabras predefinida y pedir al 
usuario una palabra. Indicar si está en la lista o no.
'''
mi_lista=["Enero","Febrero","Marzo"]
consulta=input("ingrese el mes a buscar")

if consulta in mi_lista:
    print("la palabra se encuentra en la lista")

if mi_lista.count(consulta)>0:
    print("la palabra se encuentra en la lista")

    