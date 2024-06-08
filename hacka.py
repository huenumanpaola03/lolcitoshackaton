import os
# Datos 
diccionario = {"alumno" : {"Usuario":"Alison", "Rut":321, "Contrasena":123, "Telefono":123456789},
            "administrador": {"adm":"Paola", "Rut":654, "Contrasena":456, "Telefono":987654321}}

def limpiar_consola():
    os.system("cls")
    
limpiar_consola()
opcion = input("Seleccione como quiere ingresar\n1: SOY ALUMNOS\n2: SOY ADMINISTRADOR\nIngrese una opción: ") 
rut = int(input("Ingrese su rut: "))
contrasena = int(input("Ingrese su contraseña: "))
if opcion == "1":
    if diccionario["alumno"]["Rut"] == rut and diccionario["alumno"]["Contrasena"] == contrasena:
        print(f"Acceso valido")       
    else:
        print("Rut o Contraseña invalida")
elif opcion == "2":
    if diccionario["administrador"]["Rut"] == rut and diccionario["administrador":]["Rut"] == contrasena:
        print(f"Acceso valido")       
    else:
        print("Rut o Contraseña invalida")
else:
    print("Opción invalida")

op_principal = input("OPCIONES:\n\n1: Search\n\n Datos:\n2: Perfil:\n\nReservas:\n3: Scooter\n4: Bicicletas\n5: Patinetas")
if op_principal == "2":
    if opcion == "1":
        print(f"Datos: {diccionario['alumno']}")
    elif opcion == "2":
        print(f"Datos: {diccionario['administrador']}")