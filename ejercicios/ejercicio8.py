'''Problema: Solicitar al usuario dos conjuntos de números y luego mostrar:

    La unión de ambos conjuntos.

    La intersección de ambos conjuntos'''

# entrada1="8 9" #input("Ingrese los números del primer conjunto")
# print(map(int,entrada1)) # 8 9
# print(map(int,entrada1.split())) # 8,9
# print(set(map(int,entrada1.split()))) #{8,9}
conjunto1=set(map(int,input("Ingrese los números del primer conjunto").split()))
conjunto2=set(map(int,input("Ingrese los números del primer conjunto").split()))
union=conjunto1 | conjunto2
interseccion= conjunto1.intersection(conjunto2)
print(conjunto1, conjunto2, union, interseccion)