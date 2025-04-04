'''
Problema: Crear un diccionario con algunos productos 
y permitir que el usuario agregue un nuevo producto con su precio.
'''
productos={
    "pera": 50,
    "manzana": 200,
    "guayaba":80
}
producto=input("Por favor ingrese el nombre")
precio=float(input("Por favor ingrese el precio"))

#productos[producto]=precio #Forma 1
productos.update({producto:precio, "limon":80})
print(productos)