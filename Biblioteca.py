################Operaciones que hara nuestro codigo###########
#Agregar un libros
#Borrar libros
#Actualizar libros
#Ver libros
#Ver todos los libros
 
#creamos nuestro diccionario
class agenda (dict):
	#Funciones para nuestra agenda
	def agregar_libro():
		print ("* AGREGAR LIBRO *\n")
		nombre = input("Nombre del libro: ")
		#comprbamos si el libro ya existe
		if nombre.capitalize() in agenda:
			print ("¡¡¡¡ EL LIBRO YA EXITE !!!!")
			nombre = input("Nombre del libro: ")
			if nombre.capitalize() not in agenda:
				numero = input("Numero del libro: ")
				agenda[nombre.capitalize()]= numero
		else:
			numero = input("Nombre del autor: ")
			agenda[nombre.capitalize()]= numero
		print()
	
	def borrar_libro():
		print ("* BORRAR LIBRO *\n")
		nombre = input ("Nombre del libro que deseas borrar: ")
	#para prevenir un keyerror en caso que el libro no existe creamos un Try
		try:
			del agenda[nombre.capitalize()]
			print()
			print("----Registro eliminado----\n")
		except KeyError:
			print()
			print("El registro que estas intentando eliminar no existe \n")
	
	
	def actualizar_libro():
		print ("* ACTUALIZAR LIBRE *\n")
		nombre = input("Nombre del libro: ")
		#comprobamos si el libro que se desea actualizar existe en nuestro diccionario
		#si existe actualizamos el numero, si no existe mandamos el mensaje
		if nombre.capitalize() in agenda:
			#elimino el registro previo del libro a atualizar, una vez comprado que existe y pido
			del agenda[nombre.capitalize()]
			#pido los nuevos valores del libro
			nombre = input("Actualizar nombre del libro: ")
			numero = input("Actualizar nombre del autor: ")
			agenda[nombre.capitalize()] = numero
			print("----libro actualizado----\n")
		else:
			print("El registro que deseas actualizar no existe\n")
	
	
	def ver_libro():
		print ("* VER LIBRO *\n")
		nombre = input("Que libro deseas ver: ".capitalize())
		try:
			print(nombre.capitalize(), "-",agenda[nombre.capitalize()])
			print()
		except KeyError:
			print("El libro que deseas visualizar no existe\n")
	
	def listado_libros():
		print ("* LISTADO DE LIBROS *\n")
		#creamos un fin con un len, y comprobamos si el diccionario es == 0 entonces 
		#no hay nada que mostrar y desplegamos un mensaje
		if len(agenda) == 0:
			print("Tu agenda esta vacia\n")
		for key in agenda:
			print(key, "-",agenda[key])
		print()
	
	print("** Bienvenidos a tu libreria virtual **".upper())
	print()
	while True:
		try:
			print("1.- AGREGAR LIBROS")
			print("2.- VER LIBROS")
			print("3.- LISTADO DE LIBROS")
			print("4.- ACTUALIZAR LIBROS")
			print("5.- BORRAR LIBROS")
			print("6.- SALIR")
			print()
			opcion = int(input("Que accion deseas realizar? "))
			print()
		except ValueError:
			print("¡¡¡¡ FAVOR DE AGREGAR SOLO AUTORES !!!\n")
		else:
			if opcion < 0 or opcion > 6:
				print ("¡¡¡ NO ES UNA OPCION VALIDA !!!\n")
				continue
			if opcion == 1:
				agregar_libro()
			elif opcion == 2:
				ver_libro()
			elif opcion == 3:
				listado_libros()
			elif opcion == 4:
				actualizar_libro()
			elif opcion == 5:
				borrar_libro()
			else:
				break
	print("* GRACIAS POR UTILIZAR TU BIBLIOTECA VIRTUAL *")
	print("----------- HASTA LA PROXIMA ----------")
	print("* * * * * * * * * * * * * * * * * * * * *\n")
 
c=dict()
