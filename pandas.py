import pandas as pd

data1 = {
    "name": ['sayan', 'roman', 'mallo'],
    "roll": [137, 165, 142],
    "marks": [20, 1, 18]
}

data2 = {
    "name": ['rohit', 'khatua', 'anirban'],
    "roll": [183, 163, 161],
    "marks": [10, 14, 187]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merge = pd.merge(df1, df2, on=["name", "roll", "marks"], how="outer")
print(merge)
