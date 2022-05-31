#variable
calificacion = input("Introduce tu calificacion de la AZ-900: ")

calificacion = int(calificacion)

#calificacion < 700
if calificacion < 700 : 
    print("Por no estudiar") #menor a 700
elif calificacion == 700 :
    print("panzazooo")
elif calificacion > 1000:
    print("mentiroso")
else :
    print("Eres buenisimo") #mayor a 7000

edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes acompañado  de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero en el tiempo")
else :
    print("No mota")

#en python no hay switch

