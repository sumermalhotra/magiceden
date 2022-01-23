import logging
from time import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class MagicEdenScraper:
    BASE_URL = "https://magiceden.io/marketplace"

    def __init__(self, timeout: int = 10, headless: bool = True):
        self.headless_toggle = headless
        self.timeout = timeout
        self.create_driver()
        
    def create_driver(self):
        options = Options()
        options.headless = self.headless_toggle
        options.add_argument('--log-level=3')
        self.driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(), options=options)

    def kill_driver(self):
        print('Killing driver now...')
        self.driver.quit()

    def get(self, collection: str, keyword: str):
        flag = True
        start_time = time()
        self.driver.get(f"{self.BASE_URL}/{collection}")
        while flag:
            try:
                html = self.driver.page_source
                soup = BeautifulSoup(html, features="html.parser")
                spans = soup.find_all('span')
                if len(spans) > 0:
                    for i, item in enumerate(spans): 
                        if item.text == keyword: break
                    fp = float(spans[i+1].text[:-2])
                    flag = False
                else:
                    raise Exception
            except Exception as e:
                if time() - start_time > self.timeout:
                    print(f"Browser did not respond within {self.timeout} seconds.")
                    fp = None
                    flag = False
        return fp

    def get_floor_price(self, collection: str) -> float:
        return self.get(
            collection, 
            'Floor Price')

    def get_total_volume(self, collection: str) -> float:
        return self.get(
            collection, 
            'Total Volume (ALL Time, ALL Marketplaces)')

    def get_avg_price(self, collection: str) -> float:
        return self.get(
            collection, 
            'Avg Sale Price (Last 24HR)')
