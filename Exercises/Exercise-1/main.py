import os
import requests
from zipfile import ZipFile
import concurrent.futures
from scripts.save_content import save_url_content


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
    TARGET_FOLDER = 'downloads'

    if not os.path.exists(TARGET_FOLDER):
        os.makedirs(TARGET_FOLDER)


    # Retrieve URL contents
    def load_url(url, timeout=20):
        try:
            # Pass url & path. Save url content into file.
            file_path = save_url_content(url=url, target_folder=TARGET_FOLDER)
        
            # Unzip file
            with ZipFile(file=file_path, mode='r') as zipFile:
                zipFile.extractall(path=TARGET_FOLDER)

            # Delete zip-file
            os.remove(file_path)
        except:
            print('Error occured: URL=' + url)


    # Main processing URLs
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for url in download_uris:
            try:       
                # Load URL content with parallel task
                executor.submit(load_url, url=url)
            except:
                print("Error with url.")


if __name__ == "__main__":
    main()
