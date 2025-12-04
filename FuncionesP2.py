import numpy as np
import pandas as pd

# a)
def eliminaDecimales(df: pd.DataFrame, col: str) -> pd.DataFrame:
    out = df.copy()
    out[f"{col}_sin_decimales"] = np.trunc(out[col]).astype(int)
    return out

# b)
def calculaRatio(df: pd.DataFrame, col1: str, col2: str) -> pd.Series:
    ratio = df[col1] / df[col2]
    if (ratio > 1).any():
        raise ValueError("Ratio > 1 encontrado.")
    return ratio