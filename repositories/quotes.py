import re

import requests
from bs4 import BeautifulSoup
from Quote import QuoteEntity


class QuotesRepository:
    quotesDivClass = 'field-item even last'

    def getQuotesFromTopic(self, topic):
        box=[]
        for page in range(5):
            page = 0
            response = requests.get(topic + f'?page={page}')
            if response.status_code == 200:
                quotesHtml = self.getQuotesFromPage(response)
                for item in quotesHtml:
                    box.append(QuoteEntity(item))
        return box


    def getQuoteInfoFromContent(self, quotes):
        quoteBox = []
        for quoteInfo in quotes:
            quoteBox.append(QuoteEntity(quoteInfo))
        return quoteBox

    def getQuotesFromPage(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find_all('div', {'class': re.compile(r'views-row views-row-.+')})
