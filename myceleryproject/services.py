# myapp/services/scraper_service.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json

class ScraperService:
    def __init__(self, coin_name):
        self.coin_name = coin_name
        self.base_url = "https://coinmarketcap.com/currencies/"
        self.driver = None

    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode for faster execution
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def scrape_data(self):
        self.setup_driver()
        try:
            self.driver.get(f"{self.base_url}{self.coin_name}/")

            price_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'sc-d1ede7e3-0') and contains(@class, 'fsQm') and contains(@class, 'base-text')]"))
            )
            price = price_element.text

            price_change_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'sc-71024e3e-0') and contains(@class, 'sc-58c82cf9-1') and contains(@class, 'bgxfSG') and contains(@class, 'iPawMI')]"))
            )
            price_change = price_change_element.text.split()[0]

            market_cap_rank_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'text') and contains(@class, 'slider-value') and contains(@class, 'rank-value')]"))
            )
            market_cap_rank = market_cap_rank_element.text

            market_cap_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//dd[contains(@class, 'sc-d1ede7e3-0') and contains(@class, 'hPHvUM') and contains(@class, 'base-text')]"))
            )
            market_cap = market_cap_element.text.split()[-1]

            data = {
                "price": price,
                "price_change": price_change,
                "market_cap_rank": market_cap_rank,
                "market_cap": market_cap
            }

            return json.dumps(data, indent=2)
        finally:
            self.driver.quit()

# myapp/coinmarketcap.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json

# class CoinMarketCap:
#     def __init__(self, coin_name):
#         self.coin_name = coin_name
#         self.base_url = "https://coinmarketcap.com/currencies/"
#         self.driver = None

#     def setup_driver(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument('--headless')  # Run in headless mode for faster execution
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     def scrape_data(self):
#         self.setup_driver()
#         try:
#             self.driver.get(f"{self.base_url}{self.coin_name}/")

#             # Extract price
#             price_element = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'sc-d1ede7e3-0') and contains(@class, 'fsQm') and contains(@class, 'base-text')]"))
#             )
#             price = price_element.text

#             price_change_element = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'sc-71024e3e-0') and contains(@class, 'sc-58c82cf9-1') and contains(@class, 'bgxfSG') and contains(@class, 'iPawMI')]"))
#             )
#             price_change = price_change_element.text.split()[0]

#             market_cap_rank_element = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'text') and contains(@class, 'slider-value') and contains(@class, 'rank-value')]"))
#             )
#             market_cap_rank = market_cap_rank_element.text

#             market_cap_element = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//dd[contains(@class, 'sc-d1ede7e3-0') and contains(@class, 'hPHvUM') and contains(@class, 'base-text')]"))
#             )
#             market_cap = market_cap_element.text.split()[-1]

#             # data = {
#             #     "coin_name":self.coin_name,
#             #     "price": price,
#             #     "price_change": price_change,
#             #     "market_cap_rank": market_cap_rank,
#             #     "market_cap": market_cap
#             # }

#             data = {
#                 "coin": self.coin_name,
#                 "output": {
#                     "price": price,
#                     "price_change": price_change,
#                     "market_cap": market_cap,
#                     "market_cap_rank": market_cap_rank,
#                     "volume": 0,  # Replace with actual volume data
#                     "volume_rank": 0,  # Replace with actual volume rank data
#                     "volume_change": 0,  # Replace with actual volume change data
#                     "circulating_supply": 0,  # Replace with actual circulating supply data
#                     "total_supply": 0,  # Replace with actual total supply data
#                     "diluted_market_cap": 0,  # Replace with actual diluted market cap data
#                     "contracts": [  # Replace with actual contract data
#                         {
#                             "name": "solana",
#                             "address": "HLptm5e6rTgh4EKgDpYFrnRHbjpkMyVdEeREEa2G7rf9"
#                         }
#                     ],
#                     "official_links": [  # Replace with actual official links data
#                         {
#                             "name": "website",
#                             "link": "https://dukocoin.com"
#                         }
#                     ],
#                     "socials": [  # Replace with actual social media data
#                         {
#                             "name": "twitter",
#                             "url": "https://twitter.com/dukocoin"
#                         },
#                         {
#                             "name": "telegram",
#                             "url": "https://t.me/+jlScZmFrQ8g2MDg8"
#                         }
#                     ]
#                 }
#             }

#             return data
#         finally:
#             self.driver.quit()

#     def get_data_as_json(self):
#         data = self.scrape_data()
#         return json.dumps(data, indent=2)
    

import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

class CoinMarketCap:
    def __init__(self, coin_name):
        # Initialize the CoinMarketCapScraper object with the given coin name and base URL
        self.coin_name = coin_name
        self.base_url = "https://coinmarketcap.com/currencies/"
        self.driver = None

    def setup_driver(self):
        # Set up the Chrome WebDriver with headless mode enabled for faster execution
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def preprocess_stats(self, data):
        # Preprocess statistics data to extract numeric values and percentage change
        market_cap_parts = data['Market cap'].split('$')
        volume_parts = data['Volume (24h)'].split('$')
        data['market_cap'] = float(re.sub(r'[^\d.]', '', market_cap_parts[1]))
        data['Volume (24h)'] = float(re.sub(r'[^\d.]', '', volume_parts[1]))

        try:
            volume_change_percentage = float(data['Volume/Market cap (24h)'].split('%')[0])
        except ValueError:
            volume_change_percentage = 0.0  
        data['Volume change'] = volume_change_percentage

        return data


    def extract_statistics(self):
        # Extract statistics data from the webpage
        try:


            statistics_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='section-coin-stats']"))
            )

            data_points = statistics_section.find_elements(By.XPATH, ".//dl[@class='sc-d1ede7e3-0 bwRagp coin-metrics-table']/div")
            stats_data = {}
            for data_point in data_points:
                title_element = data_point.find_element(By.XPATH, ".//dt")
                value_element = data_point.find_element(By.XPATH, ".//dd")
                
                title = title_element.text.strip()
                value = value_element.text.strip()

                # Check if title exists before assigning value to stats_data
                if title:
                    stats_data[title] = value

            return stats_data
        except TimeoutException as e:
            print("TimeoutException:", e)
            return {}
        

    def extract_price_info(self):
        # Extract current price and price change from the webpage
        price_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'sc-d1ede7e3-0') and contains(@class, 'fsQm') and contains(@class, 'base-text')]"))
        )
        price = price_element.text

        price_change_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'sc-71024e3e-0') and contains(@class, 'sc-58c82cf9-1') and contains(@class, 'bgxfSG') and contains(@class, 'iPawMI')]"))
        )
        price_change = price_change_element.text.split()[0]  

        return price, price_change

    def extract_official_links(self):
        # Extract official website link from the webpage
        official_links_section = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-role='stats-block']//span[text()='Official links']/ancestor::div[@data-role='stats-block']"))
        )
        official_website_link = official_links_section.find_element(By.TAG_NAME, "a").get_attribute("href")

        return official_website_link

     # Extract contract name and address from the webpage
    def extract_contract_info(self):
        contracts_section = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-role='stats-block']//span[text()='Contracts']/ancestor::div[@data-role='stats-block']"))
        )
        contract_name_element = contracts_section.find_element(By.CLASS_NAME, "chain-name")
        contract_name = contract_name_element.find_element(By.TAG_NAME, "span").text.strip()
        contract_address = contract_name_element.get_attribute("href")

        return contract_name, contract_address

    def scrape_social_media(self):
        # Scrape social media links from the webpage
        socials_section = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-role='stats-block']//span[text()='Socials']/ancestor::div[@data-role='stats-block']"))
        )

        social_media_data = {}
        social_links = socials_section.find_elements(By.TAG_NAME, "a")
        for link in social_links:
            social_media_name = link.text.strip()
            social_media_url = link.get_attribute("href")
            if "twitter.com" in social_media_url:
                social_media_data["Twitter"] = social_media_url
            elif "t.me" in social_media_url:
                social_media_data["Telegram"] = social_media_url

        return social_media_data

    def scrape_data(self):
        # Main method to scrape all data from the webpage
        self.setup_driver()
        try:
            self.driver.get(f"{self.base_url}{self.coin_name}/")

            stats_data = self.extract_statistics()
            stats_data = self.preprocess_stats(stats_data)
            
            price, price_change = self.extract_price_info()

            official_website_link = self.extract_official_links()

            contract_name, contract_address = self.extract_contract_info()

            social_media_data = self.scrape_social_media()

            data = {
                "coin": self.coin_name,
                "output": {
                    "price": price,
                    "price_change": price_change,
                    "market_cap": stats_data['Market cap'],
                    "volume": stats_data['Volume (24h)'],
                    "volume_change": stats_data['Volume change'],
                    "circulating_supply": stats_data['Circulating supply'],
                    "total_supply": stats_data['Total supply'],
                    "diluted_market_cap": stats_data['Fully diluted market cap'],
                    "contracts": [{
                        "name": contract_name,
                        "address": contract_address
                    }],
                    "official_links": [{
                        "name": "website",
                        "link": official_website_link
                    }],
                    "socials": social_media_data
                }
            }

            
            return data

        finally:
            self.driver.quit()

    def get_data_as_json(self):
        data = self.scrape_data()
        return json.dumps(data, indent=2)



