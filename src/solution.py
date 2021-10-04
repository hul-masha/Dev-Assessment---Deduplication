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
    duplicate_pairs, real_duplicate = [], {}
    for row in df[df.duplicated(subset=['name'], keep=False)].itertuples():
        if row.name not in real_duplicate:
            real_duplicate[row.name] = []
        real_duplicate[row.name].append(row.Id)
    duplicate_pairs.append(real_duplicate)
    df = df.drop_duplicates(subset=['name'], keep=False)
    for name_1_id, name_1 in zip(df["Id"], df["name"]):
        for name_2_id, name_2 in zip(df["Id"], df["name"]):
            if name_1_id != name_2_id and fuzz.ratio(name_2, name_1) > 85:
                duplicate_pairs.append({name_1: name_1_id, name_2: name_2_id})
                break
        df = df.query(f"Id not in [{name_1_id}]")
    return duplicate_pairs
