import pandas as pd
import re
from fuzzywuzzy import fuzz


def data_normalization(file_name: str = "companies.csv") -> pd.core.frame.DataFrame:
    df = pd.read_csv(file_name)
    df["name"] = ["".join([j for j in re.split('[?& /|,\.\-\'\"]', i.lower())]) for i in df["name"]]
    return df


def find_duplicates(file_name: str = "companies.csv") -> list:
    df = data_normalization(file_name)
    s = []
    for i_id, i in zip(df["Id"], df["name"]):
        for j_jd, j in zip(df["Id"], df["name"]):
            if i_id != j_jd and (j_jd, i_id) not in s:
                if i == j:
                    s.append((i_id, j_jd))
                else:
                    if fuzz.ratio(j, i) > 85:
                        print(i, j, i_id, j_jd)
                        s.append((i_id, j_jd))
    print(len(s))
