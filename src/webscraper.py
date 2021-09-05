'''Linkedin Web Scraping Class'''
import numpy as np
import pandas as pd
import platform
import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SLEEP_TIME = 2

class WebScraper():
    '''
    Simple class to perform Web-Scraping on Linkedin.
    It takes as input an url and collect information
    about the jobs in the loaded webpage. It
    '''
    def __init__(self):
        self.OS = platform.system()
        self.wd = ""
        self.verbose = 1

    def remove_cookies(self):
        '''
        Remove the cookies from the webpage.
        This is actually not required, but I hate
        cookies.
        '''

        self.wd.find_element_by_xpath('/html/body/div[1]'
                                      '/div/section/div/div[2]/button[2]').click()

    def get_wd(self):
        '''
        Enable to load the correct webdriver given
        the operating system. Currently there is no
        option for Mac Systems, since I have none at
        home >:(

        Input:
            None

        Return:
            The correct webdriver
        '''
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        if self.OS == "Linux":
            self.wd = webdriver.Chrome('./driver/Linux_chromedriver',
                                       options=chrome_options)
        elif self.OS == "Windows":
            self.wd = webdriver.Chrome('./driver/Windows_chromedriver.exe',
                                       options=chrome_options)

    def load_jobs(self):
        '''
        Scrool for the full length of the page.
        Each loop check if the "Show more" button
        is enabled, and try to click it if possible.

        Input:
            wd : the webdriver

        returns:
            the full web page with all jobs loaded
        '''

        s = self.wd.find_element_by_css_selector('h1>span').get_attribute('innerText')
        jobs = int(re.sub(r'[^\w]', '', s))

        for _ in range(int(jobs/25)):
            self.wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(SLEEP_TIME)
            try:
                self.wd.find_element_by_xpath('//*[@id="main-content"]/section[2]/button').click()
            except:
                pass

        #Returns at top of the page
        self.wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        job_lists = self.wd.find_element_by_class_name('jobs-search__results-list')
        return job_lists.find_elements_by_tag_name('li')

    def collect_infos(self, job):
        '''
        Utility function to collect all the relevant info
        about a given job.

        Input:
            job : the job to analyze
            rec : variable to manage network lag spikes

        Returns:
            job_info : a dictionary containing all the
                       info about a job
        '''
        job_info = {
            'id' : job.id,
            'title' : job.find_element_by_css_selector('h3').get_attribute('innerText'),
            'company_name' : job.find_element_by_css_selector('h4').get_attribute('innerText'),
            'location' : job.find_element_by_css_selector('[class="job-search'+
                                '-card__location"]').get_attribute('innerText'),
            'date_posted' : job.find_element_by_css_selector('div>div>time').get_attribute('datetime'),
            'link' : job.find_element_by_css_selector('a').get_attribute('href'),
            'description' : job.find_element_by_xpath('/html/body/div[1]/div/section'+
                            '/div[2]/section[2]').get_attribute('innerText')
        }

        return job_info


    def scrape_linkedin(self, url):

        if self.verbose:
            print("Connecting to Linkedin")

        self.get_wd()
        self.wd.get(url)

        time.sleep(SLEEP_TIME)
        self.remove_cookies()
        jobs = self.load_jobs()

        if self.verbose:
            print("Collecting infos!")

        job_info = []
        for job in jobs:
            job.click()
            job_info.append(self.collect_infos(job))
            time.sleep(SLEEP_TIME)

        df = pd.DataFrame(job_info)












