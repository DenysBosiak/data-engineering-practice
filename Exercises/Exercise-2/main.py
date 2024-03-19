import requests
import pandas as pd
from bs4 import BeautifulSoup


def main():
    # your code here
    URL = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
    SEARCH_DATE = '2024-01-19 10:45'
    

    response = requests.get(url=URL)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find('table')

    
    def preparing_url(download_url: list):
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['td', 'th'])
            if SEARCH_DATE in [ele.text.strip() for ele in cols]:    
                url_prep = f"{URL}" + row.find('a').get('href')
                download_url.append(url_prep)
        
    
    download_url = []
    preparing_url(download_url)
    print(download_url)

if __name__ == "__main__":
    main()
