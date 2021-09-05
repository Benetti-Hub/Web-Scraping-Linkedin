'''Linkedin Web Scraping Utility'''
import numpy as np
import pandas as pd
import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebScraper():
    '''
    Base class to perfrom web-scraping on linkedin
    '''
    def __init__(self):
        self.OS = platform.system()
        self.verbose = 1

    def connect_to_linkedin(self, url):

        if self.verbose:
            print("Connecting to Linkedin")

        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        wd = webdriver.Chrome(f'./driver/{self.OS}_chromedriver', options=chrome_options)
        wd.get(url)

        s = wd.find_element_by_css_selector('h1>span').get_attribute('innerText')








if __name__ == "__main__":

    url = "https://www.linkedin.com/jobs/search/?geoId=106693272&keywords=machine%20learning%20engineer&location=Switzerland"
    scraper = WebScraper()
    scraper.connect_to_linkedin(url)






