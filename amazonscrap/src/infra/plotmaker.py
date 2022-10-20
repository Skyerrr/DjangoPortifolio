import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plotmaker():
    plt.figure(figsize=(15, 15))
    csv = pd.read_csv("csvfile.csv")
    csv["price"] = csv["price"].str.replace(".", "")
    csv["price"] = csv["price"].str.replace(",", ".")
    csv["price"] = csv["price"].astype(float)
    sns.displot(csv["price"], kde=False, bins=30)
    plt.savefig("amazonscrap/static/displot2.png")
    plt.show()
