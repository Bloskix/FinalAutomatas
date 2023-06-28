import pandas as pd

def top_10_most_viewed():
    try:
        df = pd.read_excel(r"C:/Users/pablo/OneDrive/Escritorio/UM/Programacion I/Visua_Studio_Code/Python/Final_automatas/Listado temas 2023.xlsx") 
        artists_views = df.groupby('Artist')['Views'].sum().reset_index()
        top_10_artist = artists_views.sort_values('Views', ascending=False).head(10)
        for index, row in top_10_artist.iterrows():
            print(f"Artista: {row['Artist']}, Reproducciones: {row['Views']}")

    except Exception as e:
        print("Ocurrió un error:", str(e))
    
print("Top 10 artistas con más reproducciones:")
top_10_most_viewed()