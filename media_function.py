

import webbrowser

class MediaChannels:

    media_url = [
        'https://www.youtube.com/@ABCNews/videos',
        'https://www.youtube.com/@CBSNews/videos',
        'https://www.youtube.com/@FoxNews/videos',
        'https://www.youtube.com/@msnbc/videos',
        'https://www.youtube.com/@BBCNews/videos',
        'https://www.youtube.com/@SkyNews/videos',
        'https://www.youtube.com/@CNN/videos',
        'https://www.youtube.com/@euronews/videos',
        'https://www.youtube.com/@AlArabiya/videos',
        'https://www.youtube.com/@aljazeeraenglish/videos',
        'https://www.youtube.com/@markets/videos',
        'https://www.youtube.com/@nytimes/videos'
    ]


    def media_link_open(self, media):
        return webbrowser.open(MediaChannels.media_url[media])
