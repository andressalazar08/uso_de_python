'''
Operadores aritméticos
20 de marzo
 
'''

# #operador suma
# print(2+6)


# #operador resta
# print(8-4)

#operador multiplicación
x=4
y=6
# print(x*y) 

#operador división
z=12/4
# print(z)
# print(type(z)) #el resultado de la división siempre es flotante


#operador división piso(floor)
# print(10/3) #división tradicional
# print(10//3) #división piso
# print(14.5/3)
# print(14.5//3)
'''
la división piso siempre devuelve el entero más próximo hacia abajo
'''

#operador módulo
# print(20/3)
# print(20%3)


'''
Prueba realizar la división piso 8//-3 y 
compárala con la división tradicional 8/-3
'''


#operador potencia
# print(x**2)


'''
Operadores de comparación
Este tipo de operadores los usamos cuando deseamos comparar expresiones o
variables. Python evalúa si se cumple la comparación y 
nos devuelve (retorna) un valor True o False
'''

#es igual a
# print("enca"=="Enca")

# print(8==8)

# print(3==3.0000000000000000000000000000001)

#es diferente de
# print("palabra"!="Palabra")


'''
Operadores de asignación
'''
#Asignación de igualdad o definición
w=5

#Incremento
saldo=100
#saldo= saldo + 1
saldo+=8
print(saldo)

#Decrecimiento
saldo_b=200
#saldo= saldo + 1
saldo_b-=8
print(saldo_b)

'''
operadores lógicos
and: comprueba si todas las condiciones se cumplen, True , False de lo contrario
or: comprueba si alguna de las condiciones se cumple, True , False de lo contrario
not: negar el estado de una variable
'''
print(x==4 and y==6 )
print(x==5 or y==8 )

usuario_logueado=True
click_logout=True
print(not usuario_logueado)
