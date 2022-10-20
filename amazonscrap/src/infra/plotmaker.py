import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from django.conf import settings


def plotmaker():
    path = "amazonscrap/"
    with open("text.txt", "w", encoding="utf-8") as html_file:
        pass

    plt.figure(figsize=(15, 15))
    csv = pd.read_csv("media/csvfile.csv", engine="python")
    csv["price"] = csv["price"].str.replace(".", "")
    csv["price"] = csv["price"].str.replace(",", ".")
    csv["price"] = csv["price"].str.replace('"', "")
    csv["price"] = csv["price"].astype(float)
    sns.displot(csv["price"], kde=False, bins=30)
    plt.savefig(os.path.join(path, "static/displot1.png"))
    plt.show()
