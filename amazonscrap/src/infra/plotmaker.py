import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def plotmaker():
    path = "amazonscrap/"

    plt.figure(figsize=(15, 15))
    csv = pd.read_csv(os.path.join(path, "csvfile.csv"))
    csv["price"] = csv["price"].str.replace(".", "")
    csv["price"] = csv["price"].str.replace(",", ".")
    csv["price"] = csv["price"].astype(float)
    sns.displot(csv["price"], kde=False, bins=30)
    plt.savefig(os.path.join(path, "static/displot4.png"))
    plt.show()
