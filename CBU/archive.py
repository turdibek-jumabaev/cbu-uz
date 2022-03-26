import requests
import datetime
from . import config


class Archive():
    """
    Malumotlar CBU.UZ dan olinadi
    https://cbu.uz/uz/arkhiv-kursov-valyut/json/
    """

    def __init__(self):
        pass

    def get_currency(self, currency, year: int = datetime.datetime.now().year, month: int = datetime.datetime.now().month, day: int = datetime.datetime.now().day):
        """
        currency - valyuta nomi (majburiy)
        year - yil,
        month - oy,
        day - kun
        """
        return requests.get(
            f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/{currency}/{year}-{month}-{day}").json()

    def get_last_all_currency(self):
        return requests.get(
            "https://cbu.uz/uz/arkhiv-kursov-valyut/json/").json()

    def get_all_currency_by_date(self, year: int = datetime.datetime.now().year, month: int = datetime.datetime.now().month, day: int = datetime.datetime.now().day):
        return requests.get(
            f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/all/{year}-{month}-{day}").json()

    def get_last_all_currency_xml(self):
        return requests.get(
            "https://cbu.uz/uz/arkhiv-kursov-valyut/xml/").text

    def get_all_currency_by_date_xml(self, year: int = datetime.datetime.now().year, month: int = datetime.datetime.now().month, day: int = datetime.datetime.now().day):
        return requests.get(
            f"https://cbu.uz/uz/arkhiv-kursov-valyut/xml/all/{year}-{month}-{day}").text

    def get_currency_xml(self, currency, year: int = datetime.datetime.now().year, month: int = datetime.datetime.now().month, day: int = datetime.datetime.now().day):
        return requests.get(
            f"https://cbu.uz/uz/arkhiv-kursov-valyut/xml/{currency}/{year}-{month}-{day}").text

    def help_xml(self):
        print(config.xml)

    def help_json(self):
        print(config.json)
