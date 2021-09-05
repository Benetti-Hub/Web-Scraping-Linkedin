# Job-Scraping-Linkedin

Collection of scripts to perfrom the Web-Scraping of Jobs from Linkedin. It automatically analyze all the links in the link.txt file (in parallel) and collect the relevant informations in the data folder. One can then use NLP to extract relevant information from the collected data (for example, in Zurich one might want to avoid jobs listing in German and focus only on English ones).

## Installation:

Run the following command lines for the installation

'''
git clone git@github.com:Benetti-Hub/Web-Scraping-Linkedin.git
'''
'cd Web-Scraping-Linkedin'
'pip install -r requirements.txt'

## Usage:

Copy the link from a job search from Linkedin, make sure that the correct filters are selected before copying it!
Paste the link in the links.txt file, and then run:

'python scraper.py'






