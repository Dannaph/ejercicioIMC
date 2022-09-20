print("¡Hola! Vamos a calcular tu indice de masa muscular.")
nombre=input("Por favor, ingresa tu nombre: ")
print("Hola", nombre,)
peso = float(input("Por favor ingresa tu peso en kilogramos (x.x): "))
altura = float(input("Por favor ingresa tu altura en metros (x.x): "))
imc= peso/altura**2
print(nombre, "tu IMC es de" , imc, ". Gracias!")

