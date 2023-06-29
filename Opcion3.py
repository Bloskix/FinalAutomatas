import pandas as pd
from Menu import file_name

def search_song(keyword):
    try:
        df = pd.read_excel(file_name)
        df_cleaned = df.dropna(subset=['Title']).astype(str)
        matching_songs = df_cleaned[df_cleaned['Title'].str.contains(keyword, case=False)]
        if len(matching_songs) > 0:
            print("Canciones encontradas:")
            print(matching_songs[['Title']])
        else:
            print("No se encontraron canciones que coincidan con la búsqueda.")
    except Exception as e:
        print("Ocurrió un error:", str(e))

def run_option3():
    keyword = input("Busca una canción: ")   
    search_song(keyword)



