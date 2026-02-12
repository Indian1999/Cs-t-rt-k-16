import os
import csv
import pandas as pd # pip install pandas (terminalba)
import matplotlib.pyplot as plt # pip install matplotlib

PATH_FORRAS = os.path.join(os.path.dirname(__file__), "forras")
PATH_KIMENETEK = os.path.join(os.path.dirname(__file__), "kimenetek")

def opcio1():
    matrix = []
    with open(os.path.join(PATH_FORRAS, "directory.csv"), "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split(",")
            matrix.append(line)
    print(matrix[3:8])

#opcio1()

def opcio2():
    matrix = []
    with open(os.path.join(PATH_FORRAS, "directory.csv"), "r", encoding="utf-8") as f:
        data = csv.reader(f, delimiter = ",")
        for row in data:
            matrix.append(row)
    print(matrix[65:68])

#opcio2()

def opcio3():
    data = pd.read_csv(os.path.join(PATH_FORRAS, "directory.csv"))
    return data

data = opcio3()
print(type(data)) # <class 'pandas.core.frame.DataFrame'>
#print(data)
#print(data["Longitude"])
data = data.set_index("Store Number")
print(data)
print(data.loc["17127-178586", "City"]) # Abu Dhabi
print(data.iloc[4, 4]) # Abu Dhabi

print(data.columns) 
    # Index(['Brand', 'Store Name', 'Ownership Type', 'Street Address', 'City',
    #   'State/Province', 'Country', 'Postcode', 'Phone Number', 'Timezone',
    #   'Longitude', 'Latitude'],
    #  dtype='object')

data = data[["Store Name", "Street Address", "City", "Country", "Postcode", "Longitude", "Latitude"]]
print(data)

#data = data.drop(["Store Name"], axis=1) # 1 az oszlop tengelyt jelente (0 a sor)
data = data.drop(["Store Name"], axis="columns") # EZ ugyan az mint az előző
print(data)

magyarok = data[data["Country"] == "HU"]
print(magyarok)

# Országonként hány starbucs van?
orszagonkent = data.groupby("Country").count().reset_index("Country")
orszagonkent = orszagonkent[["Country", "City"]]
orszagonkent.columns = ["Country", "Count"]
orszagonkent = orszagonkent.sort_values(by = "Count", ascending=False)
orszagonkent = orszagonkent[orszagonkent["Count"] >= 35]
print(orszagonkent)

def store_count_per_country_plot(df):
    plt.bar(df["Country"], df["Count"])
    plt.yscale("log")
    plt.xticks(rotation=90)
    plt.xlabel("Ország")
    plt.ylabel("Starbucks-ok száma")
    plt.title("Starbucks-ok száma országonként (min 35)")
    # (supported formats: eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff, webp)
    plt.savefig(os.path.join(PATH_KIMENETEK, "starbucks_orszagonkent.png"))
    plt.show()

store_count_per_country_plot(orszagonkent)