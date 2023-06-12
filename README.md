# YT-AV-Downloader

This technique makes use of [yt-dlp](https://github.com/yt-dlp/yt-dlp). 

### Installation
<code>git clone https://github.com/ongsici/YT-AV-Downloader.git
conda create -n ytdownloader python=3.8 -y 
conda activate ytdownloader 
pip install -r requirements.txt </code>


### Data Format 
Youtube URL, start and end times should be included in the TXT file in the following format: \
(URL) (start time in hh:mm:ss) (end time in hh:mm:ss) \
Example: \
<code>https://www.youtube.com/watch?v=I_HxaUlUMTQ&t=1931s 00:32:00 00:32:08
  https://www.youtube.com/watch?v=I_HxaUlUMTQ&t=1931s 00:32:10 00:32:18 </code>

### Usage

1) Video Download: \
<code> python youtube_download.py -i youtube_example.txt -o LawrenceWong -t video </code>

2) Audio Download: \
<code> python youtube_download.py -i youtube_example.txt -o LawrenceWong -t audio </code>

