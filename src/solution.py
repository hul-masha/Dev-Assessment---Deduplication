import pandas as pd
import re
from fuzzywuzzy import fuzz


def get_duplicates(file_name: str = "companies.csv"):
    df = pd.read_csv(file_name)
    df["name"] = ["".join([j for j in re.split(
        ' |-|&|\?\|/|,|\||:|\\|\'|\"|\(|\)|\\xad|\*|constructioncorp|management|group|.com|'
        '\.|llc|inc|school|coffee|services|solutions|productions|information|communications|associates|'
        'corporation|software|international|performance|training|mortgage|systems|partners|collegeoffurthereducation|'
        'technologies|entertainment|logistics|properties|media|capital|projects|brothers',
        i.lower())]) for i in df["name"]]
    return find_duplicates(df)


def find_duplicates(df: pd.core.frame.DataFrame) -> list:
    duplicate_pairs = []
    for name_1_id, name_1 in zip(df["Id"], df["name"]):
        for name_2_id, name_2 in zip(df["Id"], df["name"]):
            if name_1_id != name_2_id and {name_1_id: name_1, name_2_id: name_2} not in duplicate_pairs:
                if name_1 == name_2:
                    duplicate_pairs.append({name_1_id: name_1, name_2_id: name_2})
                    break
                elif fuzz.ratio(name_2, name_1) > 85:
                    duplicate_pairs.append({name_1_id: name_1, name_2_id: name_2})
                    break
        df = df.query(f"Id not in [{name_1_id}]")
    return duplicate_pairs
