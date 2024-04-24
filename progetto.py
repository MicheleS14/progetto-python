import pandas as pd
import matplotlib.pyplot as plt
import os

#Costruiamo il percorso del csv da aprire
current_file = __file__
current_dir = os.path.dirname(current_file)
file_dir = os.path.join(current_dir + '\\datadump_s5-000.csv')

#Leggiamo il csv e creiamo un dataframe
dataset = pd.read_csv(file_dir, nrows = 100000)
df = pd.DataFrame(dataset)

#Creiamo 3 differenti dataframe per ogni modalità di gioco
df_SecArea = df[df["gamemode"] == "SECURE_AREA"]
df_Bomb = df[df["gamemode"] == "BOMB"]
df_Hostage = df[df["gamemode"] == "HOSTAGE"]

#Contiamo quante partite sono state giocate in ogni mappa per ogni modalità
df_Map_SecArea = df_SecArea.groupby("mapname")["gamemode"].count()
df_Map_Bomb = df_Bomb.groupby("mapname")["gamemode"].count()
df_Map_Hostage = df_Hostage.groupby("mapname")["gamemode"].count()

#print(f"\nModalita' Presidio:\n{df_Map_SecArea}\n\nModalita' Bomba:\n{df_Map_Bomb}\n\nModalita' Ostaggio:\n{df_Map_Hostage}")

df_Map_SecArea.plot.bar()
plt.show()
