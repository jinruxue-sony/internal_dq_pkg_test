import pandas as pd

def check_unique(df, col):
    if len(set(df[col])) == len(df[col]):
        return True
    else:
        return False