nombre = input ("¿Cuál es tu nomre?")
edad = int(input ("¿Cuál es tu edad?"))
if edad >= 18:
    print (f"{nombre}, eres mayor de edad, ya hay que empezar a cuidarse las rodillas!")
elif edad >= 13:
    print (f"{nombre}, eres un adolescente, quiza rebelde, pero disfruta tu juventud!")
else: 
    print (f"{nombre}, eres menor de edad, disfruta tu infancia ")
