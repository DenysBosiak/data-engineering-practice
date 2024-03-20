import requests
import pandas as pd
from bs4 import BeautifulSoup
import glob


def main():
    URL = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
    SEARCH_DATE = '2024-01-19 10:45'
    FILE_FOLDER = './downloads/'

    
    def preparing_url(download_url: list):
        # Make request to web page
        response = requests.get(url=URL)
        # Parse response content by BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        # Find table object in a parsed content
        table = soup.find('table')

        # Iterate through each row and extract values
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['td', 'th'])
            # Find file by search date and add its url at list
            if SEARCH_DATE in [ele.text.strip() for ele in cols]:    
                url_prep = f"{URL}" + row.find('a').get('href')
                download_url.append(url_prep)
        

    def load_file(url: str, timeout: int = 20):
        # Get HTTP headers information
        response = requests.head(url=url)
        # Form a file name by url and path to this file
        file_name = url.rsplit('/', 1)[1]
        file_path = f"{FILE_FOLDER}{file_name}"

        # Check url state code
        if response.status_code == 200:
            # Download content into file
            content = requests.get(url=url, allow_redirects=True, timeout=timeout)
            open(file_path, 'wb').write(content.content)
            print(file_name + ' was downloaded.')


    def calculation(dfs: list):
        # List all csv files in a directory
        files = glob.glob(f"{FILE_FOLDER}*.csv")
        # Read each file into a separate dataframe
        for file in files:
            df = pd.read_csv(file, low_memory=False)
            # Convert HourlyDryBulbTemperature into float format
            df['HourlyDryBulbTemperature'] = df['HourlyDryBulbTemperature'].astype('Float64')
            max_temperature = df['HourlyDryBulbTemperature'].max()
            # Add max value into our main list
            dfs.append(max_temperature)


    download_url = []
    dfs = []

    # Get data about urls
    preparing_url(download_url)
        
    # Save files localy
    for url in download_url:
        load_file(url=url)

    # Prepare aggregating data
    calculation(dfs)
        
    # Print highest value by HourlyDryBulbTemperature
    print(max(dfs))


if __name__ == "__main__":
    main()
