def mostrar_lista(lista):
    if not lista:
        print("la lista esta basia")
    else:  
        for contenido in lista:
            print(contenido)
a=["maira","jose","alvin"]
mostrar_lista(a)
def eliminar_lista(lista):
    if not lista:
        print("no hay elemento por eliminar")
    else:
            lista.clear()
            print("se eliminaron los datos de la lista ")
eliminar_lista(a)