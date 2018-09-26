import requests
import functools
import pandas as pd
import numpy as np
from io import StringIO 
import requests


def load_data():
    return pd.read_csv("../jupyterlab-ux-data.csv")

def reload_data():
    r = requests.get('https://docs.google.com/spreadsheet/ccc?key=1TCWnKucs25_rWrVVu3mwqbpsij-KOCGRbcOcTzxRmOM&output=csv')
    data = r.content
    df = pd.read_csv(StringIO(data.decode("utf-8")))
    df = cleaner(df)
    return df
    
    
def cleaner(df):
    
    target_encoding = dict(
        TE=("E", "T"),
        BE=("E", "B"),
        RE=("E", "R"),
        LE=("E", "L"),
        
        BL=("B", "L"),
        BR=("B", "R"),
        BT=("B", "T"),
        BB=("B", "B"),
        BC=("B", "C"),
        BTa=("B", "Ta"),
        
        GL=("G", "L"),
        GR=("G", "R"),
        GT=("G", "T"),
        GB=("G", "B"),
        GC=("G", "C"),
        GTa=("G", "Ta"),
        
        RL=("R", "L"),
        RR=("R", "R"),
        RT=("R", "T"),
        RB=("R", "B"),
        RC=("R", "C"),
        RTa=("R", "Ta")
    )
    
    # Add three new columns
    df["source"] = ""
    df["target"] = ""
    df["position"] = ""
    
    # Change ToT (Time on Task) to integers.
    for i in range(len(df)):
        time = df.loc[i,"ToT"]
        try:
            minutes, seconds = time.split(":")
            seconds = float(minutes) * 60 + float(seconds)
        except:
            seconds = np.nan
        df.loc[i,"ToT"] = seconds

        # Parse init action
        move = df.loc[i, "Init"]
        try:
            # Get source from 
            move = move.split(" to ")
            source = move[0]
            
            # Get Position
            endpoint = move[1][:-2] # Remove DZ.
            target, position = target_encoding[endpoint]
            
            df.loc[i, "source"] = source
            df.loc[i, "target"] = target
            df.loc[i, "position"] = position
            
        except:
            pass

    return df

