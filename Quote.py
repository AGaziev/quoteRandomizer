import re

import bs4.element
from bs4.element import Tag
from bs4 import BeautifulSoup


class QuoteEntity:
    quoteInfo = {}

    def __init__(self, info: Tag):
        self.quoteInfo = {}
        quoteInfoHtml = info.find('div', class_='node__content').find_all('div',
                                                                          {'class': re.compile(r'field field-name-.+')},
                                                                          recursive=False)
        self.quoteInfo['Цитата'] = self.getMainTextField(quoteInfoHtml[0])
        self.getInfoFields(quoteInfoHtml[1:])

    def getInfoFields(self, html: bs4.element.ResultSet):
        for field in html:
            result: bs4.element.Tag = field.find('a')
            try:
                self.quoteInfo[result.get('title')] = result.text.strip()
            except:
                pass

    def getMainTextField(self, html: bs4.element.Tag):
        return html.text.strip()

    def __str__(self):
        text=''
        for key, v in self.quoteInfo.items():
            text+=f'{key}: {v}\n'
        return text
