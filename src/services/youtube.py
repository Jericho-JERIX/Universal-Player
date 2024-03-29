import sys
from yt_dlp import YoutubeDL

def download_music(url, path="src/music", filename="downloaded_music"):

    URLS = url

    with YoutubeDL() as ydl:
        info_dict = ydl.extract_info(URLS, download=False)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get("title", None)
        # print(info_dict)
        print(f"[video_id]{video_id}[video_id]")
        print(f"[video_title]{video_title}[video_title]")
        # print(f"[video_title]{}[video_title]")

    if video_id is None:
        return
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'paths': {'home': '{}'.format(path)},
        'outtmpl': video_id,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio'
        }]
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)

if __name__ == '__main__':
    url = sys.argv[1]
    filename = sys.argv[2]
    download_music(url,'src/music',filename)

# Usage: python3 src/services/youtube.py <url> <filename>