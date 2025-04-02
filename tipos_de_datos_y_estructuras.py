'''
TIPOS DE DATOS
strings: Cadenas de texto <class 'str'>
'''
dato="Enca24"
dato_2='Enca24'

#print(type(dato))
#print(type(dato_2))

#Concatenación de strings
texto_1="Programa "
texto_2="Desarrollador junior"

enunciado=texto_1 + texto_2
#print(enunciado)

#Indexación de strings
#La indexación se refiere a acceder a un elemento de una cadena en una posición
nombre="Andres Felipe"
 #      012345
#print(nombre[0])
'''
Python es un lenguaje indexado en cero
'''
#print(nombre[5])
#print(nombre[15])
#print(nombre[-3])

#Slicing de cadenas (porción de la cadena) [:]
# print(nombre[0:3]) #Esta forma de porcionar no incluye el extremo derecho
# print(nombre[2:4])
#print(nombre[0:-5])
nombre="Andres F e  l i p  e"
    #           -6 -5  -4 -3 -2  -1
    
'''
Tipos de datos numéricos
<class 'int'> : se refiere a números enteros
<class 'float'> : se refiere a numeros flotantes que contienen decimales
'''
x=5
#print(type(x))
y=5.0
#print(type(y))

'''
Datos Boolean
1,0 ó Falso / verdadero
<class 'bool'>
True
False
'''
asistencia=False
# print(type(asistencia))
# print(not asistencia)

''''
TIPOS DE ESTRUCTURAS Y MÉTODOS
sets:  se definen en python  con {,,,,,}
tuplas: se definen en python  con (,,,,,)
listas: se definen en python  con [,,,,]
diccionarios:se definen en python  con {'clave':'valor','clave_2':'valor_2',,}
'''

#Sets o conjuntos
'''
se utilizan para almacenar información cuando no interesa el orden ni la posición
no permite valores duplicados
<class 'set'>
'''
conjunto_1={"a", "b", "c","c"}
conjunto_2={"d", "e", "f"}

#print(type(conjunto_1))
#print(conjunto_1)

'''
Los métodos indican las cosas que podemos hacer con los objetos
'''
#Métodos de los conjuntos
conjunto_1.add("h")
#print(conjunto_1)

conjunto_2.remove("f")
#print(conjunto_2)

conjunto_3=conjunto_1.union(conjunto_2)
#print(conjunto_3)

#aplicar un método
conjunto_2.update(conjunto_1)
#print(conjunto_2)

conjunto_2.clear()
#print(conjunto_2)


'''
TUPLAS
<class 'tuple'>
Son estructuras en python más rigidas,
son inmutables,
almacenan distintos tipos de datos
las tuplas tienen posición
()
'''
tupla_1=(1,1,1,1,1,1,1,1,"b", True)
#print(type(tupla_1))
#print(tupla_1.count("b"))

#print(tupla_1.index("b"))


'''
Uso de listas
[]
'''

mi_lista=[9,5,8,15,True]
print(mi_lista)
print(len(mi_lista)) #Función de python len
mi_lista.append(False) #Aplicando un método a la lista
print(mi_lista)
print(sum(mi_lista)) #función de python sum

'''
Uso de diccionarios
{clave:valor,clave:valor,clave:valor,clave:valor,....}
'''
estudiantes={"Andres": {"edad":25,"Ciudad origen":"Cali"}, "Jose":22, "Diana":26}
print(estudiantes.keys())
print(estudiantes.values())
print(estudiantes.pop("Diana")) #imprime el resultado de aplicar el método pop
print(estudiantes)
