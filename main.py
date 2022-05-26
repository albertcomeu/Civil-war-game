import os
from bs4 import BeautifulSoup
import tkinter as tk
from PIL import ImageTk, Image


class CivilGame:
    solution = {}
    event_list = []
    curr_event = 0

    def __init__(self, dir):
        self.f = open(dir, "r", encoding='utf-8')
        self.soup = BeautifulSoup(self.f.read(), 'lxml')
        self.f.close()
        self.init_event_list(self.soup.body)

    def init_event_list(self, soup):
        for i in soup.contents:
            self.event_list.append(i)
        print(self.event_list)

    def start_game(self, soup):
        for i in soup.contents:
            if i.name == "message":
                print(i.text)
                input()
                os.system("cls")
            if i.name == "event":
                print(i.message.text)
                alts = i.find_all("alt")
                for j in range(len(alts)):
                    print("\t" + str(j + 1) + ") " + alts[j].text)
                self.solution[i['num']] = input()
                os.system("cls")
            if i.name == "depend":
                if self.solution.get(i["ev"]) == i["val"]:
                    self.start_game(i)


class GameWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Civil war")
        self.window.geometry("1280x720")
        self.window.resizable(width=False, height=False)
        self.init_game_window()
        self.window.mainloop()

    def init_game_window(self):
        self.window.image = tk.PhotoImage(file="img/main_backgroud.png")
        bg_logo = tk.Label(self.window, image=self.window.image)
        bg_logo.place(relheight=1.0, relwidth=1.0)

        canvas = tk.Canvas(self.window, width=500, height=700)
        pilImage = Image.open("img/scr.png")
        image = ImageTk.PhotoImage(pilImage)
        imagesprite = canvas.create_image(50, 50, image=image)
        canvas.place(relheight=0.1, relwidth=0.1)


if __name__ == '__main__':
    windows = GameWindow()

