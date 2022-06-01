import requests
from bs4 import BeautifulSoup
from topics import TopicsRepository
import tkinter as tk


class ListApp(tk.Tk):
    topics = TopicsRepository()
    MODES = [tk.SINGLE, tk.BROWSE, tk.MULTIPLE, tk.EXTENDED]

    def __init__(self):
        super().__init__()
        self.geometry('500x300')

        self.setTopicsChooserFrame()

    def setQuoteLabel(self):
        #TODO
        pass

    def setStartButtonLabel(self):
        #TODO
        pass

    def setTopicsChooserFrame(self):
        getTopicsFrame = tk.Frame(self)
        getTopicsFrame.size()

        scrollbar = tk.Scrollbar(getTopicsFrame)
        scrollbar.pack(side=tk.RIGHT,
                       fill=tk.Y)

        self.topicsList = tk.Listbox(getTopicsFrame,
                                     height=500,
                                     selectmode=tk.MULTIPLE,
                                     yscrollcommand=scrollbar.set,
                                     width=25)
        self.topicsList.insert(0, *sorted(self.topics.getTopicsName(), key=lambda x: x.lower()))

        eraseButton = tk.Button(getTopicsFrame,
                                text='Убрать выделение',
                                command=lambda: self.topicsList.selection_clear(0, tk.END))
        chooseAllButton = tk.Button(getTopicsFrame,
                                    text='Выделить всё',
                                    command=lambda: self.topicsList.selection_set(0, tk.END))

        chooseAllButton.pack(side=tk.BOTTOM)
        eraseButton.pack(side=tk.BOTTOM)
        getTopicsFrame.pack(ipady=200, side=tk.LEFT)
        self.topicsList.pack()


if __name__ == "__main__":
    app = ListApp()
    app.mainloop()
