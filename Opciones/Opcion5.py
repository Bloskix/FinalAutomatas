import pandas as pd

def top_10_largest_songs():
    try:
        df = pd.read_excel(r"DATA_FRAME") 
        df_sorted = df.sort_values(by='Duration_ms', ascending=False)
        largest_songs = df_sorted.head(10)
        for index, row in largest_songs.iterrows():
            Duration_ms = row['Duration_ms']
            mins = int(Duration_ms // 60000)
            secs = int(Duration_ms % 60000) // 1000
            time = '{:02d}:{:02d}'.format(mins, secs)
            print(f"{row['Title']} - {time}")

    except Exception as e:
        print("Ocurrió un error:", str(e))

print("Las 10 canciones mas largas son:")
top_10_largest_songs()