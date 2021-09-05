'''Linkedin Web Scraping Class'''
import numpy as np
import pandas as pd
import platform
import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebScraper():
    '''
    Base class to perfrom web-scraping on linkedin
    '''
    def __init__(self):
        self.OS = platform.system()
        self.verbose = 1

    def remove_cookies(self, wd):
        wd.find_element_by_xpath('/html/body/div[1]/div/section/div/div[2]/button[2]').click()

    def get_wd(self):

        '''
        Load the correct webdriver given the OS
        '''
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        if self.OS == "Linux":
            wd = webdriver.Chrome('./driver/Linux_chromedriver', options=chrome_options)
        elif self.OS == "Windows":
            wd = webdriver.Chrome('./driver/Windows_chromedriver.exe', options=chrome_options)

        return wd

    def connect_to_linkedin(self, url):

        if self.verbose:
            print("Connecting to Linkedin")

        wd = self.get_wd()
        wd.get(url)

        time.sleep(3)
        self.remove_cookies(wd)

        s = wd.find_element_by_css_selector('h1>span').get_attribute('innerText')
        jobs = int(re.sub(r'[^\w]', '', s))
        i = 2
        while i <= int(jobs/25)+1:
            wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            i = i + 1
            time.sleep(3)
            try:
                wd.find_element_by_xpath('//*[@id="main-content"]/section[2]/button').click()
            except:
                pass








if __name__ == "__main__":

    url = "https://www.linkedin.com/jobs/search/?geoId=106693272&keywords=machine%20learning%20engineer&location=Switzerland"
    scraper = WebScraper()
    scraper.connect_to_linkedin(url)






