
import json
from datetime import datetime
import requests
from threading import *
from PyQt5.QtGui import QIcon
import webbrowser

class HomeNews:
    req = requests.Session()
    news_link_load = {}

    def thread(self, list_widget, widget, gui):
        news_load = Thread(target=self.add_news, args=(list_widget, widget, gui))
        news_load.start()

    def add_news(self, list_widget, widget, gui):

        #start = datetime.now()

        api_key = '4dbc17e007ab436fb66416009dfb59a8'
        news_call = json.loads(requests.get(f'https://newsapi.org/v2/everything?q=everything&language=en&apiKey={api_key}').text)
        title_count = len(news_call['articles'])

        for i in range(title_count - 1):
            news_item = widget.QListWidgetItem(list_widget)
            icon = gui.QIcon()

            url = news_call['articles'][i]['url']
            image = news_call['articles'][i]['urlToImage']
            title = news_call['articles'][i]['title']


            HomeNews.news_link_load[title] = url

            try:
                link_requests = HomeNews.req.get(image)
                pic = gui.QPixmap()
                pic.loadFromData(link_requests.content)

                icon = gui.QIcon(pic)
                icon.addPixmap(gui.QPixmap(pic), gui.QIcon.Normal, gui.QIcon.Off)

                news_item.setText(title)
                news_item.setIcon(icon)

            except:
                icon.addPixmap(gui.QPixmap('icons/no_img.png'), gui.QIcon.Normal, gui.QIcon.Off)
                news_item.setText(title)
                news_item.setIcon(icon)

    def news_load_url(self, title):
        return webbrowser.open(HomeNews.news_link_load[title])
