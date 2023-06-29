from Menu import file_name
import pandas as pd
import time

def submenu():
    print("1.Listar las 5 canciones con mas likes")
    print("2.Listar las 5 canciones con mas vistas")
    print("3.Listar las 5 canciones con mas comentarios")
    print("4.Volver al menú principal")

def read_option():
    option = input("Ingresa una opción: ")
    while not option.isdigit() or int(option) < 1 or int(option) > 4:
        option = input("Opción inválida. Ingresa una opción válida: ")
    return option

def more_something_songs(something):
    try:
        df = pd.read_excel(file_name)
        sorted_by = df.sort_values(by=something, ascending=False)
        top_songs = sorted_by.head(5).reset_index(drop=True)
        top_songs.index = top_songs.index + 1
        print(top_songs[['Title', something]])
    except Exception as e:
        print("Ocurrió un error:", str(e))

def run_option1():    
    while True:
        submenu()
        option = read_option()
        if option == "1":
            more_something_songs("Likes")
        elif option == "2":
            more_something_songs("Views")
        elif option == "3":
            more_something_songs("Comments")
        elif option == "4":
            pass
        