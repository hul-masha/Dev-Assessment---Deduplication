import pandas as pd
import re
from fuzzywuzzy import fuzz


def get_duplicates(file_name: str = "companies.csv"):
    df = pd.read_csv(file_name)
    df["name"] = ["".join([j for j in re.split('[?& /|,\.\-\'\"]', i.lower())]) for i in df["name"]]
    return find_duplicates(df)


def find_duplicates(df: pd.core.frame.DataFrame) -> list:
    duplicate_pairs = []
    for name_1_id, name_1 in zip(df["Id"], df["name"]):
        for name_2_id, name_2 in zip(df["Id"], df["name"]):
            if name_1_id != name_2_id and (name_2_id, name_1_id) not in duplicate_pairs:
                if name_1 == name_2:
                    duplicate_pairs.append((name_1_id, name_2_id))
                elif fuzz.ratio(name_2, name_1) > 85:
                    # print(name_1, name_2, name_1_id, name_2_id)
                    duplicate_pairs.append((name_1_id, name_2_id))
    return duplicate_pairs
