import sys

sys.path.append("amazonscrap/src")
sys.path.append("amazonscrap/src/data")
sys.path.append("amazonscrap/src/data/interfaces")
sys.path.append("amazonscrap/src/infra")
sys.path.append("amazonscrap/src/errors")
from amazonscrap.src.infra.html_filter import IphoneHtmlFilter
from amazonscrap.src.infra.plotmaker import plotmaker

"""
Scrap from Amazon
Str: change SEARCH_PARAMETER with your selected product to be scrapped and return a csv file
"""

# if __name__ == "__main__":


def run_scrap(scrapname):
    SEARCH_PARAMETER = "iphone"

    scrapper = IphoneHtmlFilter()

    scrapper.run_from_url(f"https://www.amazon.com.br/s?k={scrapname}", f"csvfile.csv")
    plotmaker()
    # scrapper.run_from_html_file("response2.html", CSV_FILE_NAME)
