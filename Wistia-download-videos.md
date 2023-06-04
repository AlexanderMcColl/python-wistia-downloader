# Download Wistia videos

1. right-click on the **playing** video, select Copy link
1. find Wistia video ID in the copied link e.g. `wvideo=tra6gsm6rl`
   - alternative: look for e.g. `hashedId=tra6gsm6rl` in the page source
1. load `http://fast.wistia.net/embed/iframe/` + video ID in your browser
1. look for `"type":"original"` in the page source and
   copy the URL from the next line
   e.g. `"url":"http://embed.wistia.com/deliveries/129720d1762175bcd8e06dcab926ec76ad38ff00.bin"`
   - alternative: look for `"type":"hd_mp4_video"`
1. download the video from the URL with `.mp4` extension instead of `.bin`
