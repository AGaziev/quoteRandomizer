import random
import asyncio
import tkinter as tk
import tkinter.ttk as ttk
from repositories.topics import TopicsRepository
from repositories.quotes import QuotesRepository


class ListApp(tk.Tk):
    topics = TopicsRepository()
    quotes = QuotesRepository()

    def __init__(self):
        super().__init__()
        self.geometry('500x600')

        self.setTopicsChooserFrame()
        self.setStartButtonLabel()
        self.setQuoteLabel()

    def genericQuote(self):
        box = []
        urlDict = self.topics.topicsNamesWithUrl
        for i, topic in enumerate([self.topicsList.get(idx) for idx in self.topicsList.curselection()]):
            topicUrl = urlDict[topic]
            test = self.quotes.getQuotesFromTopic(topicUrl)
            box.extend(test)
        self.quoteText.config(text=random.choice(box))

    def setQuoteLabel(self):
        self.quoteText = tk.Label(wraplength=300)
        self.quoteText.pack(fill=tk.X)

    def setStartButtonLabel(self):
        startButtonFrame = tk.Frame(self, borderwidth=6)

        self.startButton = tk.Button(startButtonFrame,
                                     text='СГЕНЕРИРОВАТЬ ЦИТАТУ',
                                     command=self.genericQuote)
        self.startButton.pack(side=tk.BOTTOM)
        startButtonFrame.pack(ipady=20)

    def setTopicsChooserFrame(self):
        getTopicsFrame = tk.Frame(self)

        scrollbar = tk.Scrollbar(getTopicsFrame)
        scrollbar.pack(side=tk.RIGHT,
                       fill=tk.Y)

        self.topicsList = tk.Listbox(getTopicsFrame,
                                     height=500,
                                     selectmode=tk.MULTIPLE,
                                     yscrollcommand=scrollbar.set,
                                     width=25)
        self.topicsList.insert(0,
                               *sorted(self.topics.getTopicsName(), key=lambda x: x.lower())
                               )

        eraseButton = tk.Button(getTopicsFrame,
                                text='Убрать выделение',
                                command=lambda: self.topicsList.selection_clear(0, tk.END))
        chooseAllButton = tk.Button(getTopicsFrame,
                                    text='Выделить всё',
                                    command=lambda: self.topicsList.selection_set(0, tk.END))

        chooseAllButton.pack(side=tk.BOTTOM)
        eraseButton.pack(side=tk.BOTTOM)
        getTopicsFrame.pack(side=tk.LEFT)
        self.topicsList.pack()


if __name__ == "__main__":
    app = ListApp()
    app.mainloop()
