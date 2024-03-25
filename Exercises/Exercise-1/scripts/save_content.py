import requests


def save_url_content(url, target_folder, timeout=20):
    '''
        Retrieve URL contents.
        Pass the url, filename & path.
    '''
    # Get HTTP headers information
    response = requests.head(url=url)
    # Form a file name by url and path to this file
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