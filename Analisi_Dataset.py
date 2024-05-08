import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import scipy
import r6func

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
df_Map_PC_Presidio = r6func.played_Match_Maps(df_PC_Presidio)
df_Map_PC_Bomba = r6func.played_Match_Maps(df_PC_Bomba)
df_Map_PC_Ostaggio = r6func.played_Match_Maps(df_PC_Ostaggio)

#PS4
df_Map_PS4_Presidio = r6func.played_Match_Maps(df_PS4_Presidio)
df_Map_PS4_Bomba = r6func.played_Match_Maps(df_PS4_Bomba)
df_Map_PS4_Ostaggio = r6func.played_Match_Maps(df_PS4_Ostaggio)

#XBOX
df_Map_XBOX_Presidio = r6func.played_Match_Maps(df_XBOX_Presidio)
df_Map_XBOX_Bomba = r6func.played_Match_Maps(df_XBOX_Bomba)
df_Map_XBOX_Ostaggio = r6func.played_Match_Maps(df_XBOX_Ostaggio)

#print(f"\nModalita' Presidio:\n{df_Map_SecArea}\n\nModalita' Bomba:\n{df_Map_Bomb}\n\nModalita' Ostaggio:\n{df_Map_Hostage}")

"""#Grafico partite Presidio
Func.show_Map_Played_Chart(df_Map_PC_Presidio, df_Map_PS4_Presidio, df_Map_XBOX_Presidio, "Presidio")

#Grafico partite Bomba
Func.show_Map_Played_Chart(df_Map_PC_Bomba, df_Map_PS4_Bomba, df_Map_XBOX_Bomba, "Bomba")

#Grafico partite Ostaggio
Func.show_Map_Played_Chart(df_Map_PC_Ostaggio, df_Map_PS4_Ostaggio, df_Map_XBOX_Ostaggio, "Ostaggio")

df_Match = r6func.played_Match_Maps(df)

for map in df["mapname"].unique():
    print(f"\nMappa: {map}\nOperatore + giocato: {r6func.operator_Played(df, map).idxmax()}\nOperatore meno giocato: {r6func.operator_Played(df, map).idxmin()}")


df_Win_Rate = r6func.win_Rate(df)
print(df_Win_Rate)

df_Pick_Rate = r6func.pick_Rate(df)
print(df_Pick_Rate)

df_Win_And_Pick_Rate = df_Win_Rate.merge(df_Pick_Rate, left_index=True, right_index=True)
df_Badge = pd.DataFrame({"operator" : ["BOPE-CAPITAO", "BOPE-CAVEIRA", "G.E.O.-JACKAL", "G.E.O.-MIRA", "GIGN-DOC", "GIGN-MONTAGNE", "GIGN-RESERVE", "GIGN-ROOK", "GIGN-TWITCH"," GSG9-BANDIT", "GSG9-BLITZ", "GSG9-IQ", "GSG9-JAGER", "GSG9-RESERVE", "JTF2-BUCK", "JTF2-FROST", "NAVYSEAL-BLACKBEARD", "NAVYSEAL-VALKYRIE", "SAS-MUTE", "SAS-RESERVE", "SAS-SLEDGE", "SAS-SMOKE", "SAS-THATCHER", "SAT-ECHO", "SAT-HIBANA", "SPETSNAZ-FUZE", "SPETSNAZ-GLAZ", "SPETSNAZ-KAPKAN", "SPETSNAZ-RESERVE", "SPETSNAZ-TACHANKA", "SWAT-ASH", "SWAT-CASTLE", "SWAT-PULSE", "SWAT-RESERVE", "SWAT-THERMITE"],
         "badge" : [os.path.join(current_dir + "\\Badge\\BADGE_Capitao.png"), os.path.join(current_dir + "\\Badge\\BADGE_Caveira.png"), os.path.join(current_dir + "\\Badge\\BADGE_Jackal.png"), os.path.join(current_dir + "\\Badge\\BADGE_Mira.png"), os.path.join(current_dir + "\\Badge\\BADGE_Doc.png"), os.path.join(current_dir + "\\Badge\\BADGE_Montagne.png"), os.path.join(current_dir + "\\Badge\\BADGE_Reserve.png"), os.path.join(current_dir + "\\Badge\\BADGE_Rook.png"), os.path.join(current_dir + "\\Badge\\BADGE_Twitch.png"), os.path.join(current_dir + "\\Badge\\BADGE_Bandit.png"), os.path.join(current_dir + "\\Badge\\BADGE_Blitz.png"), os.path.join(current_dir + "\\Badge\\BADGE_IQ.png"), os.path.join(current_dir + "\\Badge\\BADGE_Jager.png"), os.path.join(current_dir + "\\Badge\\BADGE_Reserve.png"), os.path.join(current_dir + "\\Badge\\BADGE_Buck.png"), os.path.join(current_dir + "\\Badge\\BADGE_Frost.png"), os.path.join(current_dir + "\\Badge\\BADGE_Blackbeard.png"), os.path.join(current_dir + "\\Badge\\BADGE_Valkyrie.png"), os.path.join(current_dir + "\\Badge\\BADGE_Mute.png"), os.path.join(current_dir + "\\Badge\\BADGE_Reserve.png"), os.path.join(current_dir + "\\Badge\\BADGE_Sledge.png"), os.path.join(current_dir + "\\Badge\\BADGE_Smoke.png"), os.path.join(current_dir + "\\Badge\\BADGE_Thatcher.png"), os.path.join(current_dir + "\\Badge\\BADGE_Echo.png"), os.path.join(current_dir + "\\Badge\\BADGE_Hibana.png"), os.path.join(current_dir + "\\Badge\\BADGE_Fuze.png"), os.path.join(current_dir + "\\Badge\\BADGE_Glaz.png"), os.path.join(current_dir + "\\Badge\\BADGE_Kapkan.png"), os.path.join(current_dir + "\\Badge\\BADGE_Reserve.png"), os.path.join(current_dir + "\\Badge\\BADGE_Tachanka.png"), os.path.join(current_dir + "\\Badge\\BADGE_Ash.png"), os.path.join(current_dir + "\\Badge\\BADGE_Castle.png"), os.path.join(current_dir + "\\Badge\\BADGE_Pulse.png"), os.path.join(current_dir + "\\Badge\\BADGE_Reserve.png"), os.path.join(current_dir + "\\Badge\\BADGE_Thermite.png")
]}).set_index("operator")

df_Win_And_Pick_Rate_Badge = df_Win_And_Pick_Rate.merge(df_Badge, left_index=True, right_index=True)

print(df_Win_And_Pick_Rate_Badge)

r6func.show_Operator_Pick_Win_Rate(df_Win_And_Pick_Rate_Badge)

####.to_excel(current_dir + "\\File Risultato.xlsx")
"""

print(r6func.death_Probability(df, 5, 3))
#print(df["matchid"].nunique())