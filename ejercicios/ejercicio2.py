'''
Problema: Escribe un programa que verifique si una palabra ingresada por el usuario está 
en la siguiente frase:
"Python es un lenguaje de programación poderoso".
'''
frase="Python es un lenguaje de programación poderoso"
palabra=input("ingrese la palabra a buscar en la frase")

#operador de contenido in
print(palabra in frase) #True o False
