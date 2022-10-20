from typing import Tuple
from collections import namedtuple
import requests
import sys

sys.path.append("amazonscrap/src")
sys.path.append("amazonscrap/src/data")
sys.path.append("amazonscrap/src/data/interfaces")
sys.path.append("amazonscrap/src/infra")
sys.path.append("amazonscrap/src/errors")
from amazonscrap.src.data.interfaces.get_url_interface import GetUrlInterface
from amazonscrap.src.errors.http_request_error import HttpRequestError
from django.conf import settings


class UrlToScrap(GetUrlInterface):
    """
    Class to scrap URL with requests and save to CSV
    """

    def fetch(self, url: str) -> Tuple[int, str]:
        """
        fetch url html and save in CSV
        Header to avoid 503 error
        :param - url: str URL
        :return - Tuple with status_code and html text
        """

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-language": "en-US,en;q=0.8",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        }

        response = requests.get(url, headers=headers)
        status_code = response.status_code
        tuple_response = namedtuple("data", "status_code response")

        if (status_code >= 200) and (status_code <= 299):

            with open(
                f"{settings.BASE_DIR}/amazonscrap/response2.html", "w", encoding="utf-8"
            ) as html_file:
                html_file.write(response.text)

            return tuple_response(status_code=status_code, response=response.text)
        else:
            return f"Error {status_code}"
