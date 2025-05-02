#elabora una funcion para imprimir los elementos de una lista 
##list lista[1,2,3,4,5,6,7,8,11]: # type: ignore
##a=lista
##print(a)##
def imprimir_lista(lista):
    for elemento in lista :
        print(elemento)
nombres=["jose","maria", "antonio","juan","alvin"]
imprimir_lista(nombres)       
#-------------------------------------
print("caso 2 si no hay elementos en la lisa")
#-------------------------------------
def imprimir_lista(lista):
    if not lista:
        print("no hay elementos en la lista ")
    else:
        for elemento in lista:
            print(elemento)
apellidos=[]#"perez","bellido","cespedes","calcaterra"]
imprimir_lista(apellidos)
