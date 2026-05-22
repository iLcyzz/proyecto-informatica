#Cristofer Choque
#Darian Rodriguez
#Mauricio Fernandez
#Jose Cabrera

#CASO:Gestion de inventario en una tienda de una tienda
#inicio
# DEFINICIÓN DE LA CLASE PRINCIPAL DEL PROGRAMA
class Libro:
     # Metodo constructor para inicializar los atributos del objeto libro
    def __init__(self, titulo, autor, anio, cantidad, precio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.cantidad = cantidad
        self.precio = precio
#Funciones 
def crear_inventario_ejemplo():
    # Inicializa una lista vacia para guardar objetos tipo Libro
    inventario = [] 
    # Creacion de 3 objetos individuales usando la clase Libro
    
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 5, 25000)
    libro2 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985, 3, 22000)
    libro3 = Libro("Rayuela", "Julio Cortázar", 1963, 2, 18900)
    
     # Agrega cada libro al final de la lista general
    inventario.append(libro1)
    inventario.append(libro2)
    inventario.append(libro3)

    # Devuelve la lista completada al programa principal
    return inventario
def mostrar_inventario(lista_libros):
     # Condicional para verificar si la lista no tiene elementos guardados  
    if len(lista_libros) == 0:
        print("El inventario esta vacio. No hay libros para mostrar.")
    else:
         # Imprime la cabecera en mayusculas
        print("INVENTARIO COMPLETO")
        # Ciclo para pasar por cada objeto libro dentro de la lista
        for libro in lista_libros:
            # Despliega los datos de forma ordenada separados por barras
            print(f"Titulo: {libro.titulo} | Autor: {libro.autor} | Año: {libro.anio} | Cantidad: {libro.cantidad} | Precio: ${libro.precio}")
def buscar_libro_por_titulo(lista_libros, titulo_buscar):
    # Variable de control tipo booleana para saber si se encontro el texto
    encontrado = False
    # Recorre todos los libros almacenados uno por uno
    for libro in lista_libros:
        # Convierte ambos textos a minusculas para hacer una comparacion justa
        if libro.titulo.lower() == titulo_buscar.lower():
            print("LIBRO ENCONTRADO")
            print(f"Titulo: {libro.titulo}")
            print(f"Autor: {libro.autor}")
            print(f"Año: {libro.anio}")
            print(f"Cantidad: {libro.cantidad}")
            print(f"Precio: ${libro.precio}")
            # Cambia el estado de la variable de control a Verdadero
            encontrado = True
    # Si al terminar el ciclo la variable sigue Falsa, el libro no existe        
    if encontrado == False:
        print(f"No se encontro ningun libro con el titulo: '{titulo_buscar}'")
def agregar_libro(lista_libros):
    print()
    print("AGREGAR NUEVO LIBRO")
    # Captura de datos ingresados desde el teclado por el usuario
    titulo = input("Titulo del libro: ")
    autor = input("Autor: ")
    anio = int(input("Año de publicacion: "))
    precio = float(input("Precio: "))
     # Validacion: Verifica que las cadenas de texto no esten vacias
    if titulo == "" or autor == "":
        print("Error: El titulo y el autor no pueden estar vacios.")
    elif anio < 1000 or anio > 2026 or precio < 0: 
        print("Error: Los datos numericos ingresados son invalidos.")
    else:
        encontrado = False
        for libro in lista_libros:
            if libro.titulo.lower() == titulo.lower():
                # Si existe, se incrementa su cantidad en 1 automáticamente
                libro.cantidad = libro.cantidad + 1
                encontrado = True
                print(f"El libro ya existia. Se incremento su cantidad disponible a: {libro.cantidad}")
        
        # Si es un libro nuevo, se agrega con cantidad inicial en 1
        if encontrado == False:
            nuevo_libro = Libro(titulo, autor, anio, 1, precio)
            lista_libros.append(nuevo_libro)
            print(f"Libro registrado exitosamente con cantidad inicial en 1.")
def calcular_estadisticas_matrices():
    print("INFORME MATEMÁTICO DE VENTAS (MATRICES)")
    matriz_ventas_reales = [
        [10, 15, 12],
        [8,  9,  11],
        [5,  6,  4]
    ]
    matriz_ventas_estimadas = []
    filas = 3
    columnas = 3
    print("Ingrese las ventas esperadas para el proximo trimestre:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f"Ventas estimadas Libro {i+1}, Mes {j+1}: ")))
        matriz_ventas_estimadas.append(fila)
    matriz_suma_total = []
    for i in range(filas):
        fila_s = []
        for j in range(columnas):
            # Suma de la celda de la matriz constante + la celda de la matriz variable
            fila_s.append(matriz_ventas_reales[i][j] + matriz_ventas_estimadas[i][j])
        matriz_suma_total.append(fila_s)
    print("\n[SALIDA MATRICIAL] Proyeccion Total de Ventas Acumuladas:")
    for i in matriz_suma_total:
        print(i)
#entrada 
c = "S"
inventario_general = crear_inventario_ejemplo()

#proceso
while c == "S" or c == "s":
    print("MENU PRINCIPAL - LIBRERIA NUEVO MUNDO")
    print("1. Mostrar inventario completo")
    print("2. Buscar libro por titulo")
    print("3. Agregar nuevo libro al inventario")
    print("4. Analizar estadisticas de ventas (Matrices)")
    print("5. Salir")
    
    opc = int(input("Ingrese su opcion: "))
    
    if opc == 1:
        mostrar_inventario(inventario_general)
    elif opc == 2:
        x = input("Ingrese el titulo del libro a buscar: ")
        buscar_libro_por_titulo(inventario_general, x)
    elif opc == 3:
        agregar_libro(inventario_general)
    elif opc == 4:
        calcular_estadisticas_matrices() 
    elif opc == 5:
        print("Saliendo del programa...")
        c = "N"
    else:
        print("La opcion es incorrecta")
        
    if opc != 5:
        c = input("Desea ejecutar de nuevo: [S] o [N]: ")

#salida
print("HASTA LUEGO")
#fin