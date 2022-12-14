

import random

class Search:
    def __init__(self, buttons, search_list):
        self.popular_topic = ["International news", "National news", "Local news", "Politics", "Business", "Sports", "Science and technology", "Entertainment and celebrity news", "Health and wellness", "Environment and climate change", "Education", "Crime and justice", "Agriculture and rural issues", "Transportation", "Social issues", "Religion and spirituality", "Arts and culture", "Human interest stories", "Weather", "Economy", "Energy", "Food and drink", "Fashion and beauty", "Travel", "Real estate", "Consumer technology", "Media and journalism", "Animal rights and welfare", "Space and astronomy", "Military and defense"]
        self.buttons = buttons
        self.button_load()
        self.history_load(search_list)


    def button_load(self):
        random.shuffle(self.popular_topic)
        for btn in range(len(self.buttons)):
            self.buttons[btn].setText(self.popular_topic[btn])

    def history_load(self, list):
        with open('search_log.txt', 'r') as lst:
            file_read = [list.addItem(filter.replace('\n','')) for filter in lst.readlines()]


class HistorySearch:
    def add_search(self, search_text, search_list):
        with open('search_log.txt', 'a') as log:
            log.writelines(f'{search_text}\n')
            search_list.addItem(search_text)



