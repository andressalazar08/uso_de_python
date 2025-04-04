dia=input("Ingrese el día de la semana: ").lower()
match dia:
    case "sabado" | "domingo":
        print(f"{dia} es fin de semana")
    case "lunes":
        print(f"{dia} es el día más dificil")
    case "martes" | "miercoles" | "jueves":
        print("Es un día normal")
    case _:
        print("El texto no es un día de la semana")
