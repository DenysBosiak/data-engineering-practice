import os
import requests
from zipfile import ZipFile
import concurrent.futures


download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def main():
    # Create target folder if not exists
    targetFolder = 'downloads'


    if not os.path.exists(targetFolder):
        os.makedirs(targetFolder)


    # Retrieve URL contents
    def load_url(url, timeout=20):
        # Pass the url, filename & path
        response = requests.head(url=url)
        fileName = url.rsplit('/', 1)[1] 
        filePath = f"{targetFolder}/{fileName}"


        # Check status code  
        if response.status_code == 200:
            content = requests.get(url=url, allow_redirects=True, timeout=timeout)
            # Download file
            open(filePath, 'wb').write(content.content)
            print(fileName + ' was downloaded.')


            # Unzip file
            with ZipFile(file=filePath, mode='r') as zipFile:
                zipFile.extractall(path=targetFolder)


            # Delete zip-file
            os.remove(filePath)
        else:
            print(url + ' is not valid.')
    

    # Main processing URLs
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for url in download_uris:
            try:       
                # Load URL content
                executor.submit(load_url, url=url)
            except:
                print("Error with url.")


if __name__ == "__main__":
    main()
