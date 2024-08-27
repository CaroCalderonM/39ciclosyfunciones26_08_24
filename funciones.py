# Tienen la palabra reservada def

#Ejemplo 1: Esta es una función básica que no retorna valor

def saludar(): #no recibe parámetros
    print("Hola mundo") #no retorna
#se ejecutará todas estas veces
saludar()
saludar()
saludar()
saludar()
saludar()


#Ejemplo 2:  Esta función sí recibe parámetros
def saludar(saludo):
    print(saludo)

saludar("Hola mundo")
saludar("Hola Carolina")
saludar("hola Carlos")


#Para que una función sea reutilizable, debería teder a retornar algo

def saludar(saludo):
    return f"¡{saludo}!"

saludo = saludar("Hola Carolina")
print(saludo)

























