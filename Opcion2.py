from Menu import file_name
import pandas as pd

def best_ratio_songs():
    try:
        df = pd.read_excel(file_name)
        df["Ratio"] = (df["Likes"] / df["Views"])*100
        sorted_by = df.sort_values(by="Ratio", ascending=False)
        top_songs = sorted_by.head(5).reset_index(drop=True)
        top_songs["Ratio"] = top_songs["Ratio"].map("{:.2f}%".format)
        top_songs.index = top_songs.index + 1
        print(top_songs[['Title', "Ratio"]], )
    except Exception as e:
        print("Ocurrió un error:", str(e))

def run_option2():
    print("Las 5 canciones con mas ratio son:")
    best_ratio_songs()