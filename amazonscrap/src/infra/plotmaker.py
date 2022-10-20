import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from django.conf import settings
from time import sleep
from pandas.errors import EmptyDataError


def plotmaker():
    """
    Must try multiple times because heroku updates files based on github repository
    """
    path = "amazonscrap/"
    for x in range(0, 10):  # try 10 times
        try:
            plt.figure(figsize=(15, 15))
            csv = pd.read_csv("media/csvfile.csv", engine="python")
            csv["price"] = csv["price"].str.replace(".", "")
            csv["price"] = csv["price"].str.replace(",", ".")
            csv["price"] = csv["price"].str.replace('"', "")
            csv["price"] = csv["price"].astype(float)
            sns.displot(csv["price"], kde=False, bins=30)
            plt.savefig(os.path.join(path, "static/displot1.png"))
            plt.show()
        except BaseException as empty22:
            pass
        try:
            if empty22:
                sleep(1)
            else:
                break
        except:
            pass
