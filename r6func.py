import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import scipy
import scipy.special
from math import sqrt

import scipy.stats

def played_Match_Maps(df : pd.DataFrame) -> pd.DataFrame:
    """Ritorna un dataframe con il numero di partite giocate per ogni mappa"""
    df_most_play = df.groupby("mapname")["matchid"].nunique()
    return df_most_play

def operator_Played (df : pd.DataFrame, map : str) -> pd.DataFrame:
    """Ritorna il numero di round totali in cui l'operatore e' stato giocato in una determinata mappa\nSe si verifica un errore ritorna False"""
    try:
        df_operator = df[df["mapname"] == map].groupby("operator")["operator"].count().to_frame("roundplayed")
    except:
        return False
    return df_operator

def show_Map_Played_Chart(df_Map_PC_Mode : pd.DataFrame, df_Map_PS4_Mode : pd.DataFrame, df_Map_XBOX_Mode : pd.DataFrame, gamemode : str) -> None:
    x = np.arange(16)
    heigth = 0.2

    plt.figure(figsize=(20,20))
    plt.barh(x - heigth, df_Map_PC_Mode, height=heigth, color="darkblue")
    plt.barh(x, df_Map_PS4_Mode, height=heigth, color="green")
    plt.barh(x + heigth, df_Map_XBOX_Mode, height=heigth, color="cyan")
    plt.yticks(x, df_Map_PC_Mode.index)
    plt.title(f"Numero partite per mappa in {gamemode}")
    plt.legend(["PC", "PS4", "XBOX"])
    plt.show()


def win_Rate (df : pd.DataFrame) -> pd.DataFrame:
    """Ritorna un dataframe con all'interno tutti gli operatori con il loro relativo Win Rate"""

    partite_vinte = df[df['haswon'] == True]
    return ((partite_vinte.groupby('operator').size().sort_index() / df.groupby('operator').size().sort_index() * 100) - 50).to_frame("winrate")
     

def pick_Rate (df : pd.DataFrame) -> pd.DataFrame:
    """Ritorna un dataframe con all'interno tutti gli operatori con il loro relativo Pick Rate"""
    
    numero_Round_Totali = df.groupby("matchid")["roundnumber"].max().sum()
    return pd.Series((df.groupby("operator").size().sort_index() / numero_Round_Totali) * 100).to_frame("pickrate")
    
def show_Operator_Pick_Win_Rate (df : pd.DataFrame):

    def add_image(ax, img_path, xy, zoom=0.15):
        img = plt.imread(img_path)
        imagebox = OffsetImage(img, zoom=zoom)
        ab = AnnotationBbox(imagebox, xy, frameon=False)
        ax.add_artist(ab)

    fig, ax = plt.subplots(figsize=(10, 6))

    for idx, row in df.iterrows():
        x, y = row['pickrate'], row['winrate']
        # Aggiungi l'immagine corrispondente all'operatore
        add_image(ax, row['badge'], (x, y))

        # Imposta i titoli e le etichette
        plt.title('Scatter Plot di Winrate vs Pickrate per Operatore')
        plt.xlabel('Pickrate')
        plt.ylabel('Winrate')
        plt.grid(True)
        ax.set_xlim(df['pickrate'].min() - 5, df['pickrate'].max() + 5)
        ax.set_ylim(df['winrate'].min() - 5, df['winrate'].max() + 5)
        plt.tight_layout()

    # Mostra lo scatter plot
    plt.show()

def kills_Mean_For_Round (df : pd.DataFrame, significance_Level : float) -> pd.DataFrame:
    df_Kills_Mean = df.groupby("operator")["nbkills"].mean().sort_index().to_frame("roundkillsmean")
    df_Std_Dev = df.groupby("operator")["nbkills"].std().sort_index().to_frame("stddev")
    df_Std_Err = df_Std_Dev["stddev"] / np.sqrt(df.groupby("operator")["nbkills"].count().sort_index())
    df_Intervall = scipy.stats.t.ppf(1 - (significance_Level / 2), df_Kills_Mean["roundkillsmean"].count()) * (df_Std_Dev["stddev"] / sqrt(df_Kills_Mean["roundkillsmean"].count()))
    return df_Kills_Mean.merge(df_Std_Err.to_frame("stderr"), left_index=True, right_index=True)

def prob_Doing_Kills_For_Rank (df : pd.DataFrame) -> pd.DataFrame:
    return df.groupby(["skillrank", "operator"])["nbkills"].mean()

def death_Probability (df : pd.DataFrame, nb_Rounds : int, total_Death : int):
    """Return the possibility of dying equal or less time the given value"""
    df_Death_Prob = df.groupby("operator")["isdead"].mean().sort_index().to_frame("deathprob")

    result = 0
    for x in range(total_Death + 1):
        result += scipy.special.binom(nb_Rounds, x) * (df_Death_Prob["deathprob"]**x) * ((1 - df_Death_Prob["deathprob"])**(nb_Rounds - x))
    
    return result * 100
   
    