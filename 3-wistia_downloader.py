import requests
import shutil

# SINGLE / BATCH Switch
batch = False

if batch:
    # BATCH OPTION
    # Let's you prefix videos with a category (the .txt filename).
    # Specify the list of .txt files with urls to download.
    # These must refer to .txt files in the folder where this is run (exclude the .txt file extension here).
    INPUT_FILE = ['rabbits', 'dogs', 'level_1', 'level_2', 'bonus_episodes']
else:
    # SINGLE FILE OPTION
    # include the file extension and path if file is not in this directory.
    INPUT_FILE = "list/video_url.txt"


# Downloading function
def download_file(url, prefix):
    if batch:
        local_filename = prefix + " - " + url.split('/')[-1]
    else:
        local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename


# Process the files and urls to download them
if batch:
    for file in INPUT_FILE:
        # Read the URLs from the file
        with open(f"{file}.txt", "r") as f:
            urls = f.read().splitlines()
        # Download the content of each URL
            for url in urls:
                download_file(url, file)
else:
    with open(f"{INPUT_FILE}.txt", "r") as f:
            urls = f.read().splitlines()
        # Download the content of each URL
            for url in urls:
                download_file(url, 'dummy')