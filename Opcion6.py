import pandas as pd

file_name = r"Listado temas 2023.xlsx"

def top_10_most_viewed():
    try:
        df = pd.read_excel(file_name) 
        artists_views = df.groupby('Artist')['Views'].sum().reset_index()
        top_10_artist = artists_views.sort_values('Views', ascending=False).head(10)
        for index, row in top_10_artist.iterrows():
            print(f"Artista: {row['Artist']}, Reproducciones: {row['Views']}")

    except Exception as e:
        print("Ocurrió un error:", str(e))

def run_option6():    
    print("Top 10 artistas con más reproducciones:")
    top_10_most_viewed()