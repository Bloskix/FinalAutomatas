#Listar las 5 canciones con mejor ratio
import pandas as pd

def best_ratio_songs():
    try:
        df = pd.read_excel(r"C:/Users/pablo/OneDrive/Escritorio/UM/Programacion I/Visua_Studio_Code/Python/Final_automatas/Listado temas 2023.xlsx")
        df["Ratio"] = (df["Likes"] / df["Views"])*100
        sorted_by = df.sort_values(by="Ratio", ascending=False)
        top_songs = sorted_by.head(5).reset_index(drop=True)
        top_songs["Ratio"] = top_songs["Ratio"].map("{:.2f}%".format)
        top_songs.index = top_songs.index + 1
        print(top_songs[['Title', "Ratio"]], )
    except Exception as e:
        print("Ocurrió un error:", str(e))

print("Las 5 canciones con mas ratio son:")
best_ratio_songs()