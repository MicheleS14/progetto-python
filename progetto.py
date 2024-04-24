import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import Func

#Costruiamo il percorso del csv da aprire
current_file = __file__
current_dir = os.path.dirname(current_file)
file_dir = os.path.join(current_dir + '\\datadump_s5-000.csv')

#Leggiamo il csv e creiamo un dataframe
dataset = pd.read_csv(file_dir, nrows = 100000)
#dataset = pd.read_csv(file_dir)
df = pd.DataFrame(dataset)

#Creiamo 3 differenti dataframe per ogni piattaforma
df_PC = df[df["platform"] == "PC"]
df_PS4 = df[df["platform"] == "PS4"]
df_XBOX = df[df["platform"] == "XONE"]

# Conteggio delle occorrenze per ogni piattaforma
pc_count = len(df_PC)
ps4_count = len(df_ps4)
xbox_count = len(df_xbox)

# Etichette e dati per il grafico a torta
labels = ['PC', 'PS4', 'XBOX']
sizes = [pc_count, ps4_count, xbox_count]

# Creazione del grafico a torta
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Per fare in modo che il grafico a torta sia circolare
plt.title('Numero giocatori per piattaforma', fontsize=16, fontweight='bold')
plt.show()

#Suddividiamo le modalità per ogni piattaforma

#PC
df_PC_Presidio = df_PC[df_PC["gamemode"] == "SECURE_AREA"]
df_PC_Bomba = df_PC[df_PC["gamemode"] == "BOMB"]
df_PC_Ostaggio = df_PC[df_PC["gamemode"] == "HOSTAGE"]

#PS4
df_PS4_Presidio = df_PS4[df_PS4["gamemode"] == "SECURE_AREA"]
df_PS4_Bomba = df_PS4[df_PS4["gamemode"] == "BOMB"]
df_PS4_Ostaggio = df_PS4[df_PS4["gamemode"] == "HOSTAGE"]

#XBOX
df_XBOX_Presidio = df_XBOX[df_XBOX["gamemode"] == "SECURE_AREA"]
df_XBOX_Bomba = df_XBOX[df_XBOX["gamemode"] == "BOMB"]
df_XBOX_Ostaggio = df_XBOX[df_XBOX["gamemode"] == "HOSTAGE"]



#Contiamo quante partite sono state giocate in ogni mappa per ogni modalità

#PC
df_Map_PC_Presidio = df_PC_Presidio.groupby("mapname")["gamemode"].count()
df_Map_PC_Bomba = df_PC_Bomba.groupby("mapname")["gamemode"].count()
df_Map_PC_Ostaggio = df_PC_Ostaggio.groupby("mapname")["gamemode"].count()

#PS4
df_Map_PS4_Presidio = df_PS4_Presidio.groupby("mapname")["gamemode"].count()
df_Map_PS4_Bomba = df_PS4_Bomba.groupby("mapname")["gamemode"].count()
df_Map_PS4_Ostaggio = df_PS4_Ostaggio.groupby("mapname")["gamemode"].count()

#XBOX
df_Map_XBOX_Presidio = df_XBOX_Presidio.groupby("mapname")["gamemode"].count()
df_Map_XBOX_Bomba = df_XBOX_Bomba.groupby("mapname")["gamemode"].count()
df_Map_XBOX_Ostaggio = df_XBOX_Ostaggio.groupby("mapname")["gamemode"].count()

#print(f"\nModalita' Presidio:\n{df_Map_SecArea}\n\nModalita' Bomba:\n{df_Map_Bomb}\n\nModalita' Ostaggio:\n{df_Map_Hostage}")

#Grafico partite Presidio
x = np.arange(16)
heigth = 0.2
plt.figure(figsize=(20,20))
plt.barh(x - heigth, df_Map_PC_Presidio, height=heigth, color="darkblue")
plt.barh(x, df_Map_PS4_Presidio, height=heigth, color="green")
plt.barh(x + heigth, df_Map_XBOX_Presidio, height=heigth, color="cyan")
plt.yticks(x, df_Map_PC_Ostaggio.index)
plt.title("Numero partite per mappa in ostaggio")
plt.legend(["PC", "PS4", "XBOX"])
plt.show()

#Grafico partite Bomba
x = np.arange(16)
heigth = 0.2
plt.figure(figsize=(20,20))
plt.barh(x - heigth, df_Map_PC_Bomba, height=heigth, color="darkblue")
plt.barh(x, df_Map_PS4_Bomba, height=heigth, color="green")
plt.barh(x + heigth, df_Map_XBOX_Bomba, height=heigth, color="cyan")
plt.yticks(x, df_Map_PC_Ostaggio.index)
plt.title("Numero partite per mappa in Bomba")
plt.legend(["PC", "PS4", "XBOX"])
plt.show()


#Grafico partite Ostaggio
x = np.arange(16)
heigth = 0.2
plt.figure(figsize=(20,20))
plt.barh(x - heigth, df_Map_PC_Ostaggio, height=heigth, color="darkblue")
plt.barh(x, df_Map_PS4_Ostaggio, height=heigth, color="green")
plt.barh(x + heigth, df_Map_XBOX_Ostaggio, height=heigth, color="cyan")
plt.yticks(x, df_Map_PC_Ostaggio.index)
plt.title("Numero partite per mappa in ostaggio")
plt.legend(["PC", "PS4", "XBOX"])
plt.show()

df_Match = Func.played_Match_Map(df)
print(df_Match.idxmax())
