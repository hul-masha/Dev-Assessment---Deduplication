import pandas as pd
import re

df = pd.read_csv("companies.csv", index_col='Id')
df["name"] = ["".join([j for j in re.split('[?& ,\.\-\'\"]', i.lower())]) for i in df["name"]]


# df["short_name"]=["".join([j for j in i.lower().split()]) for i in df["short_name"]]
# print(df["name"])
def find_duplicates(df):
    s = []
    for i_id, i in zip(df.index, df["name"]):
        for j_jd, j in zip(df.index, df["name"]):
            if i_id != j_jd and (j_jd, i_id) not in s:
                if i == j:
                    print(i, j, i_id, j_jd)
                    s.append((i_id, j_jd))
                elif len(i) >= len(j) and j in i:
                    print(i, j, i_id, j_jd)
                    s.append((i_id, j_jd))
                elif len(i) < len(j) and i in j:  # j.find(i,0, len(j)//2)!=-1
                    print(i, j, i_id, j_jd)
                    s.append((i_id, j_jd))

    print(len(s))


find_duplicates(df)
# print(df.duplicated("name"))
# print(df[df.duplicated(keep=False)])
