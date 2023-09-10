# python-wistia-downloader
## About
Forked from a gist.
This repo is a fairly janky (but working) way of downloading videos hosted on the Wistia cloud platform.

No guarantee, no warranty yada yada.
## 3 Files
The method comes in 3 parts. There's no GUI. Always check over code yourself before running it!
### 1
First you run 1-video_ID_fetcher.py (all credits go to [@RhetTbull](https://github.com/RhetTbull) on this issue page:

https://github.com/abdlalisalmi/wistia-downloader/issues/6#issue-1368728326 .

You right click on the video player > 'Copy link and thumbnail' and keep doing this for all the videos you need.
### 2
Then you run 2-url_maker.py to take that list of video IDs and produce a .txt file of URLs that should end in .mp4

Credits to [@szepeviktor](https://gist.github.com/szepeviktor) and [@ddepaoli3](https://gist.github.com/ddepaoli3) on this gist for the method. I simply translated it into Python code: [https://gist.github.com/szepeviktor/2a8a3ce8b32e2a67ca416ffd077553c5](https://gist.github.com/szepeviktor/2a8a3ce8b32e2a67ca416ffd077553c5)
### 3
Then you run 3-wistia_downloader.py and it iterates through the urls downloading them while you sleep ;)

Careful with wistia_downloader as it has a single and batch option (so you can categorise groups of videos).


## Another Disclaimer
This may not work for you, and may stop working at some time in the future. At least you have some basic code and a starting point.

There's no quality choices, I assume you'll get the source (highest available) quality.
