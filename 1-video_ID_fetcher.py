# Source: https://github.com/abdlalisalmi/wistia-downloader/issues/6#issue-1368728326
# Credits: https://github.com/RhetTbull
# If you are the author of this code and believe I am misusing it, please get in touch.

import os.path
import re
import shutil
from time import sleep, time

import pyperclip

OUTPUT_FILE = "video_ID.txt"


if __name__ == "__main__":
    if os.path.exists(OUTPUT_FILE):
        # backup the file
        backup_file = f"video_ID_{int(time())}.txt"
        print(f"Backup up {OUTPUT_FILE} to {backup_file}")
        shutil.copy(OUTPUT_FILE, backup_file)

    count = 0
    first = True
    try:
        with open(OUTPUT_FILE, "w") as f:
            print("Paste link from video 'Copy link and thumbnail' here and hit Enter")
            print("Press ctrl+C when you are done")
            last_buffer = ""
            while True:
                buffer = pyperclip.paste()
                if buffer == last_buffer:
                    sleep(0.1)
                    continue
                last_buffer = buffer
                if match := re.search(r"wvideo=([\w]+)\"", buffer):
                    print(f"Found video ID: {match[1]}")
                    f.write(f"{match[1]}\n")
                    f.flush()
                    count += 1
                elif first:
                    first = False
                else:
                    print("Did not find a video ID")
    except KeyboardInterrupt:
        print(f"Found {count} video IDs and wrote them to {OUTPUT_FILE}")