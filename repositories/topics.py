import requests
from bs4 import BeautifulSoup
import logging


class TopicsRepository:
    urlOfTopics = 'https://citaty.info/topic'
    classTopicsDiv = 'taxonomy-term vocabulary-vocabulary-5'
    topicsNamesWithUrl = {}

    def __init__(self):
        self.response = requests.get(self.urlOfTopics)
        print('topics Initialized ')
        if self.response.status_code == 200:
            topics = self.getTopicsBySoup()
            self.fillTopicsInfo(topics)
        else:
            logging.error('ERROR WITH CONNECTING TO TOPICS URL')

    def getTopicsBySoup(self):
        soup = BeautifulSoup(self.response.text, 'html.parser')
        return soup.find_all('div', self.classTopicsDiv)

    def fillTopicsInfo(self, items):
        for item in items:
            topicRef = item.find_next('a')
            self.topicsNamesWithUrl[topicRef.text] = topicRef['href']

    def getTopicsName(self):
        return self.topicsNamesWithUrl.keys()
