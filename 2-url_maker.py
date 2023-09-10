import requests
import re
import json

INPUT_FILE = "video_ID.txt"
OUTPUT_FILE = "video_url.txt"

# Read the list of Video_IDs
video_ID = open(INPUT_FILE,'r').read().split('\n')

# Download the webpage
with open(OUTPUT_FILE, 'a') as f:
    for video in video_ID:
        url = f"http://fast.wistia.net/embed/iframe/{video}"
        response = requests.get(url)
        content = response.text

        # Extract the URL using regular expressions
        pattern = r'^\s*W\.iframeInit\((.+), {[^}]*}\);\s*$'
        match = re.search(pattern, content, re.MULTILINE)
        if match:
            json_str = match.group(1)
            data = json.loads(json_str)
            url = data["assets"][0]["url"]
            url = re.sub(r'\.bin$', '.mp4', url)
            # Append the fetched URL to the OUTPUT_FILE
            f.write(url + "\n")