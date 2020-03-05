def insert_persona():
    nombre = input("Introduce un nombre")
    edad = input("Enter your Age")
    try:
        edad = int(edad)







    except ValueError:
        print("No.. input is not a number. It's a string")
