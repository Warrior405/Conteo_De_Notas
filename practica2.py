nombre=input("ingrese su nombre: \n")
nota1=int(input("ingrese su nota #1: \n"))
nota2=int(input("ingrese su nota #2: \n"))
nota3=int(input("ingrese su nota #3: \n"))

notaf=(nota1+nota2+nota3)/3
print(f"su nota final fue de {notaf}")


if(notaf>=70):
    print(f"Felicidades {nombre}, aprobó el curso")

    
if(notaf>=60 and notaf<70):
    print(f"lamentamos informarle que debe realizar ampliación")


if(notaf<60):
    print(f"lamentamos informarle {nombre}, que usted no aprobó")