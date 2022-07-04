# pafy-youtube-downloader
V1 of my youtube downloader script (deprecated)

Used pafy to download youtube videos, with internal editable variables to control: file path, urls to download, and whether to download video or just audio.
had to change a line in the pafy source to work after youtube disabled dislike count: in pafy changed `backend_youtube_dl.py` line 54 to `self._dislikes = self._ydl_info.get('dislike_count',0)`

downloads are slow for videos and does not support playlists, thus moved onto later versions of my youtube download script.
