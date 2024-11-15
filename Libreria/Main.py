#Defino el menu ppal y lo meto en una función
def main():
    while True:
        try:
    
            opcion = int(input("\n1. Gestión Libros\n2. Gestión usuarios\n3. Registrar devolución\n4. Listados de préstamo\n5. Potencia\n6. Salir del programa\nElige una opción:"))
            if(opcion > 6 or opcion < 0):  
                print("Elige una opción entre las disponibles, solo entre 1,2,3,4,5,6")
            elif(opcion==1):
                        print(1)
            elif(opcion==2):
                        print(1)
            elif(opcion==3):
                        print(1)
            elif(opcion==4):
                        print(1)
            elif(opcion==5):
                        print(1)
            elif(opcion==6):
                        print("salir del programa")
                        break
 
        except ValueError:
            print("Error: Por favor, introduce un número válido.")
#En caso de importar este archivo, no se ejecuta El menú, me aseguro que solo se ejecute si estoy ejecutando este archivo en concreto         
if __name__== "__main__":
    main()
    