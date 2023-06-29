import os, time
import Opcion1, Opcion2, Opcion3, Opcion4, Opcion5, Opcion6

def menu():
    os.system('cls')
    print("Selecciona una opción")
    print("1.Listar las 5 canciones con mas likes, vistas y comentarios")
    print("2.Listar 5 canciones con mas ratio en porcentaje")
    print("3.Buscar una canción")
    print("4.Agregar una nueva cancion")
    print("5.Listar las 10 canciones mas largas")
    print("6.Listar los 10 artistas con mas reproducciones")
    
def read_option():
    option = input("Ingresa una opción: ")
    while not option.isdigit() or int(option) < 1 or int(option) > 6:
        option = input("Opción inválida. Ingresa una opción válida: ")
    return option

def action(option):
    if option == "1":
        print("Elejiste la opción 1")
        time.sleep(2)
        Opcion1.run_option1()
    elif option == "2":
        print("Elejiste la opción 2")
        time.sleep(2)
        Opcion2.run_option2()
    elif option == "3":
        print("Elejiste la opción 3")
        time.sleep(2)   
        Opcion3.run_option3()
    elif option == "4":
        print("Elejiste la opción 4")
        time.sleep(2)
        Opcion4.run_option4()
    elif option == "5":
        print("Elejiste la opción 5")
        time.sleep(2)
        Opcion5.run_option5()
    elif option == "6":
        print("Elejiste la opción 6")
        time.sleep(2)
        Opcion6.run_option6()
    elif option == "7":
        print("Cerrando programa...")
        pass

while True:
    menu()
    option = read_option()
    action(option)
    break




