#mostrar inventario completo
def mostrar_inventario(lista_libros):
    """
    Muestra todos los libros del inventario en pantalla.
    Si la lista está vacía, muestra un mensaje de advertencia.
    """
    # Verificar si la lista está vacía
    if len(lista_libros) == 0:
        print(" El inventario está vacío. No hay libros para mostrar.")
        return  # Salir de la función
    
    # Mostrar encabezado opcional
    print("\n INVENTARIO COMPLETO ")
    
    # Recorrer la lista y mostrar cada libro
    for libro in lista_libros:
        print(libro)  # Usa el método __str__ de la clase Libro

def buscar_libro_por_titulo(lista_libros, titulo_buscar):
    """
    Busca libros en el inventario por título.
    La búsqueda es parcial y no distingue mayúsculas/minúsculas.
    """
    titulo_buscar_bajo = titulo_buscar.lower()  # Normalizar para búsqueda
    encontrados = []  # Lista para almacenar coincidencias
    
    # Recorrer la lista y buscar coincidencias
    for libro in lista_libros:
        if titulo_buscar_bajo in libro.titulo.lower():
            encontrados.append(libro)
    
    # Mostrar resultados
    if len(encontrados) == 0:
        print(f" No se encontró ningún libro con el título: '{titulo_buscar}'")
    else:
        print(f"\n Se encontraron {len(encontrados)} libro(s) con el título: '{titulo_buscar}'")
        print()
        for libro in encontrados:
            print(libro)

#Agregar nuevo libro
def agregar_libro(lista_libros):
    """
    Permite al usuario ingresar los datos de un nuevo libro
    y lo añade al inventario.
    """
    print("\n AGREGAR NUEVO LIBRO ")
    
    # Solicitar datos al usuario
    titulo = input("Título del libro: ").strip()
    autor = input("Autor: ").strip()
    
    try:
        anio = int(input("Año de publicación: "))
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad disponible: "))
        
        # Validar datos básicos
        if titulo == "" or autor == "":
            print(" Error: El título y el autor no pueden estar vacíos.")
            return
        
        if anio < 1000 or anio > 2026:
            print(" Error: Año de publicación inválido.")
            return
        
        if precio < 0:
            print(" Error: El precio no puede ser negativo.")
            return
        
        if cantidad < 0:
            print(" Error: La cantidad no puede ser negativa.")
            return
        
        # Crear el nuevo libro
        nuevo_libro = Libro(titulo, autor, anio, cantidad, precio)
        lista_libros.append(nuevo_libro)
        
        print(f" Libro '{titulo}' agregado exitosamente al inventario.")
        
    except ValueError:
        print(" Error: Ingrese valores numéricos válidos para año, precio y cantidad.")
