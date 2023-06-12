'''Les presento la tarea: crear un sistema para una veterinaria. Acá están los pasos a seguir:
Primero, necesitan crear una mascota. Pidan al usuario que ingrese los datos necesarios, como el nombre, la raza, etc. ¡Asegúrate de capturar toda la información importante!
Una vez que hayan creado la mascota, deberán agregarla a nuestra lista de mascotas en el sistema. Esto nos permitirá realizar un seguimiento de todas las mascotas que atendemos en la veterinaria.
Por último, es momento de mostrar todas las mascotas que tenemos en nuestro sistema. De esta forma, podremos verificar que todas las mascotas han sido correctamente agregadas y visualizar la información de cada una.
Tienes dos opciones para realizar esta tarea:

a) Puedes escribir los métodos necesarios directamente en el programa principal. Es una forma sencilla de organizar tu código y realizar las acciones requeridas.

b) También puedes crear una clase llamada "Sistema" que contenga los métodos necesarios para crear, agregar y mostrar mascotas. Esta opción te permitirá estructurar mejor tu código y aprovechar los beneficios de la programación orientada a objetos.

¡Ahora es tu turno! Elige la opción que te resulte más cómoda y manos a la obra. Si tienen alguna duda, no dudes en consultar. ¡Éxitos!'''

class Sistema:
    id = 0

    def __init__(self, tipo_animal, nombre, edad, peso, comentarios):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.comentario = comentarios
        self.animal = tipo_animal
        Sistema.id += 1
        self.id = Sistema.id

lista=[]
opcion = 0
i = 0
def menu_principal():
    print("Bienvenido al Veterinario X - Ingrese alguna de las siguientes opciones: ")
    print("Opción 1: Agregar mascota")
    print("Opción 2: Consultar todas las mascotas del sistema")
    print("Opción 3: Consulta de mascotas por ID")
    print("Opción 4: Salir del sistema")

def texto_mascota():
    print(f'ID:{lista[i].id} - {lista[i].nombre} es un {lista[i].animal}, tiene {lista[i].edad} años y pesa {lista[i].peso} kg. {lista[i].comentario}.')
    
    
k=0
while k == 0:
    menu_principal()  
    opcion = int(input("Escriba una opción: ")) 
    if opcion == 1:
        animal = input("Ingrese qué animal es su mascota: ")
        name = input("Ingrese el nombre de su mascota: ")
        edad = int(input("Ingrese la edad de su mascota: "))
        peso= int(input("Ingrese el peso de su mascota en kilogramos: "))
        comment= int(input("¿Quiere agregar un comentario? (1 = si/ 2=no): "))
        if comment == 1:
            comentario = input("Agregue su comentario ")
            mascota = Sistema(animal,name,edad,peso,comentario)
            lista.append(mascota)
            texto_mascota()
            print("Gracias para usar nuestro servicio")
            print()
        elif comment == 2:
            comentario = "Sin comentarios"
            mascota = Sistema(animal,name,edad,peso,comentario)
            lista.append(mascota)
            texto_mascota()
            print("Gracias para usar nuestro servicio")
            print()
    elif opcion == 2:
        for i in range(len(lista)):
            texto_mascota()
            print()
            i +=1
    elif opcion == 3: 
        mascota_id = int(input("¿Cuál es el id de su mascota? ")) - 1
        print(f'ID:{lista[mascota_id].id} - {lista[mascota_id].nombre} es un {lista[mascota_id].animal}, tiene {lista[mascota_id].edad} y pesa {lista[mascota_id].peso} kg. {lista[mascota_id].comentario}.')
        print()
    elif opcion == 4: 
        print("Gracias por usar nuestros servicios")
        print()
        exit()
    else: 
        print("Opción inválida")











        
    
