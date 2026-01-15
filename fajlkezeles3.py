import os
import pandas as pd # pip install pandas
import numpy as np

FORRAS_PATH = os.path.join(os.path.dirname(__file__), "forras")
KIMENETEK_PATH = os.path.join(os.path.dirname(__file__), "kimenetek")

data = pd.read_csv(os.path.join(FORRAS_PATH, "library.csv"))
print(data.columns) # Oszlopok nevei
print(data)
data = data.drop(["Edition Statement", "Corporate Author", "Former owner", "Corporate Contributors"], axis=1)
data = data.drop(columns=["Engraver", "Issuance type", "Flickr URL", "Contributors"])
data = data[['Identifier', 'Place of Publication', 'Date of Publication', 'Publisher', 'Title', 'Author']]
print(data.columns)

# Alkalmas-e az Identifier oszlop azonosításra?
print(data["Identifier"].is_unique) # True -> Minden érték egyedi -> Alkalmas azonosításra
data = data.set_index("Identifier")
print(data.head())

print(data.loc[1143]) # 1143-as ID-jú könyv
print(data.iloc[1143]) # 1143. könyv (Ez egy másik könyv)
print(data.loc[1143, "Place of Publication"]) # London
print(data.iloc[1143, 0]) # Edinburgh

# Adatok zavarosak -> tisztítsuk le őket,
# Kezdjük a Date of Publication-nel
print(data["Date of Publication"].head(20))
year = data["Date of Publication"].str.extract(r"(\d{4})")
data["Date of Publication"] = year.astype("Int16")
print(data["Date of Publication"].mean())

# Hiányzó értékek kezelése:
print("NaN értékek száma (Date oszlop):", data["Date of Publication"].isnull().sum()) # 59
atlag = round(data["Date of Publication"].mean()) # 1859
data["Date of Publication"] = data["Date of Publication"].fillna(atlag)
print(data["Date of Publication"].head(10))
print("NaN értékek száma (Date oszlop):", data["Date of Publication"].isnull().sum()) # 59

# Jöhet a Place of Publication

print(data.value_counts("Place of Publication"))
places = data["Place of Publication"].str.replace(r"[\[\]]", "", regex=True)
places = places.str.split(r"[,;:]").str[0].str.strip()
data["Place of Publication"] = places
print(data.value_counts("Place of Publication"))

data.to_csv(os.path.join(KIMENETEK_PATH, "library_clean.csv"), columns=["Title", "Date of Publication", "Place of Publication"], index=True)