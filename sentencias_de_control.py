x=520
y=60

'''
condicional if elif else
if then else

if <condición>:
    operación 1
    operación 2
    .
    .
    .
    operación n

'''
#caso 1
if x > y: #condición
    print("x es mayor a y") #operación


#caso 2 --->if else
if x < y:
    print("x es menor que y")
else:
    print("x es mayor que y")  


#caso 3 --->uso de if elif******* else
if x < y:
    print("x es menor que y")
elif x==y: #condición
    print("x es igual a y")
elif x/y==8: #condición
    print("x divido y es igual a 8")
else: #de lo contrario
    print("x es mayor que y")  

#variante 1
if x%2==0 and x>500: #múltiples condiciones a evaluar
    print("x es par y mayor que 500")


#caso de uso el login a una aplicación
usuario=input("Por favor ingrese su usuario: ")


# if usuario=="andres" and password=="1234":
#     print("usuario puede ingresar")
# else:
#     print("usuario o contraseña incorrectos")

if usuario=="andres":
    password=input("Por favor ingrese su password: ")
    if password=="1234":
        print("usuario puede ingresar")
    else:
        print("Contraseña incorrecta")
else:
    print("usuario incorrecto")
print("ejecución terminada")