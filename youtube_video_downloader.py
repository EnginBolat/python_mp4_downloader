from __future__ import unicode_literals
import youtube_dl

youtube_dl_opts= {}

with youtube_dl.YoutubeDL(youtube_dl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=swDam6Hrsm8'])