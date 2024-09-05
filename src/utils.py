import re
import pandas as pd
import os
from datetime import datetime

def read_files(path: str) -> pd.DataFrame:
    """
        Read all csv files in the given path and return a single DataFrame
    """
    arr_dfs = []
    for file in os.listdir(path):
        if file.endswith('.csv'):
            
            pattern = r"\d{4}-\d{2}"
            match = re.search(pattern, file)
            if match:
                date_str = match.group(0)
                year, month = map(int, date_str.split('-'))
                ref_date = datetime(year, month, 1)
                
                df = pd.read_csv(path + '/' + file)
                df['ref_date'] = ref_date
                arr_dfs.append(df)

            else:
                print("No date found: ", file)
    
    if len(arr_dfs):
        return pd.concat(arr_dfs)
    else:
        return None