import json
import requests
from tkinter import *
import os
from palette import Palette

class DisplayBoard(Tk):
    
    def __init__(self, bw=6, pw=40):
        super().__init__()
        self.path = './color_palettes/'
        self.current_file = 0
        self.board_width = bw
        self.COLORS_FROM = bw ** 2
        self.COLORS_TO = (bw ** 2) * 2

        self.colors = None
        self.load()

        self.title("Color Picker")
        self.config(width=1000, height=1000, bg='black')
        self.palettes = []

        i = PhotoImage(width=1, height=1)
        butt = Button(text="↻", image=i, compound='center')
        butt.configure(fg='white', bg='black', font=('Arial', 20, 'bold'),
                       command=self.refresh, width=pw, height=pw)
        butt.grid_configure(padx=5, pady=5, row=0, column=self.board_width)

        row = 0
        col = 0
        for color in self.colors[0:bw ** 2]:
            p = Palette(color['code'], pw)
            p.grid_configure(ipadx=5, ipady=5, padx=5, pady=5)
            p.grid_configure(row=row, column=col)
            self.palettes.append(p)
            if row == self.board_width - 1:
                row = 0
                col += 1
            else:
                row += 1

        self.mainloop()

    def download_from_URL(self):
        """loads palettes.json with 4 rounds of random colors"""
        url = 'https://colorhunt.co/php/feed.php'
        body = {
            'step': 0,
            'sort': 'random',
            'tags': ''
        }
        header = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        text = []
        for _ in range(4):
            response = requests.post(url=url, headers=header, data=body)
            response.raise_for_status()
            text += response.json()
    
    
        for item in text:
            del item['likes']
            del item['date']
            c = item['code']
            colors = []
            x = int(len(c) / 4)
            start = 0
            for _ in range(4):
                s = c[start:start + x]
                color = "#" + s.upper()
                colors.append(color)
                start += x
    
            item['code'] = colors

        with open(file=self.path + f'palette_{self.current_file}.json', mode='w') as file:
            json.dump(text, fp=file, indent=2)

    def load(self):
        if os.path.isfile(self.path + f'palette_{self.current_file}.json'):
            with open(file=self.path + f'palette_{self.current_file}.json', mode='r', encoding='utf-8') as file:
                self.current_file += 1
                self.colors = json.load(file)
        else:
            self.download_from_URL()
            self.load()

    def refresh(self):
        self.COLORS_FROM += self.board_width ** 2
        self.COLORS_TO += self.board_width ** 2

        if self.COLORS_FROM > len(self.colors):
            self.COLORS_TO = self.board_width ** 2
            self.COLORS_FROM = 0
            self.load()

        if self.COLORS_TO > len(self.colors):
            self.COLORS_TO = len(self.colors)

        for p in self.palettes:
            p.delete("all")
    
        row = 0
        col = 0
        index = 0
        for color in self.colors[self.COLORS_FROM: self.COLORS_TO]:
            self.palettes[index].set_colors(color['code'])
            index += 1
            if row == self.board_width - 1:
                row = 0
                col += 1
            else:
                row += 1


    
    

    

    
    





