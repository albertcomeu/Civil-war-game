import os
from bs4 import BeautifulSoup

class civilGame:
    solution = {}

    def __init__(self, dir):
        self.f = open(dir, "r", encoding='utf-8')
        self.soup = BeautifulSoup(self.f.read(), 'lxml')
        os.system("cls")
        input("Press Enter to continue...")
        os.system("cls")
        self.start_game(self.soup.body)

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


if __name__ == '__main__':
    civilGame("story.txt")
