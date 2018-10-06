import requests
import functools
import pandas as pd
import numpy as np
from io import StringIO 
import requests


def convert_time_to_int(time):
    seconds = 0
    hours = 0
    minutes = 0
    
    try:
        parts = time.split(":")    
        if len(parts) == 2:
            minutes, seconds = parts
        elif len(parts) == 3:
            hours, minutes, seconds = parts
            seconds = seconds[:2]
        else:
            return np.nan

        seconds = int(seconds)
        seconds += (int(hours) * 360) + (int(minutes) * 60)
        return seconds

    except: return np.nan

    
def diff_times(time1, time2):
    return convert_time_to_int(time2) - convert_time_to_int(time1)


def load_data():
    data = pd.read_csv("jupyterlab-ux-data.csv", header=1)
    data["Time on task"] = np.nan
    data["Start time"] = np.nan

    # Get time on task
    users = list(set(data["Code Name"]))

    # Convert start time.
    for i in data.index:
        data.loc[i, "Start time"] = convert_time_to_int(data.loc[i, "Time User Starts ST"])

    # Diff times.
    for user in users:
        df = data[data["Code Name"] == user]

        # Sort the dataframe
        sorted_index = np.argsort(df["Start time"].values)

        for i, idx in enumerate(sorted_index[:-1]):
            idx1 = df.index[sorted_index[i]]
            idx2 = df.index[sorted_index[i+1]]

            time1 = df.loc[idx1, "Start time"]
            time2 = df.loc[idx2, "Start time"]
            try:
                diff = time2 - time1
                data.loc[idx1, "Time on task"] = diff
            except: pass
        
    return data