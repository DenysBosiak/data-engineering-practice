import requests


# Retrieve URL contents
def save_url_content(url, target_folder, timeout=20):
    # Pass the url, filename & path
    response = requests.head(url=url)
    file_name = url.rsplit('/', 1)[1] 
    file_path = f"{target_folder}/{file_name}"


    # Check status code  
    if response.status_code == 200:
        content = requests.get(url=url, allow_redirects=True, timeout=timeout)
        # Download file
        open(file_path, 'wb').write(content.content)
        print(file_name + ' was downloaded.')
        return file_path
    else:
        print(url + ' is not valid.')