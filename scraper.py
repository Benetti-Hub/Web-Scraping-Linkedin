'''Core script for scrape Linkedin Job pages'''
import fileinput
import multiprocessing
from webscraper import WebScraper

def collect_jobs(url):
    '''
    Collect information about the jobs in the
    page. For more info check the WebScraper
    class.
    '''
    scraper = WebScraper()
    scraper.scrape_linkedin(url)

    print("Collected infos!")

def get_urls():
    '''
    Read the urls in the links.txt file and
    parse it as a list
    '''
    with fileinput.input(files=('links.txt')) as f:
        urls = []
        for line in f:
            if len(line)>1:
                urls.append(line)

    return urls

if __name__ == "__main__":

    urls = get_urls()
    #Go parallel!
    pool_obj = multiprocessing.Pool()
    pool_obj.map(collect_jobs, urls)
