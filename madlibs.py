import requests

response = requests.get("http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=25")

class Mad_Libs:
    def __init__(self, response):
        self.response = response
        self.title = self.response.json()["title"]
        self.blanks = self.response.json()["blanks"]
        self.story = self.response.json()["value"]
        self.words = []
        self.result = ""

    def play(self):
        print(r"""
         __  __           _   _      _ _         
        |  \/  |         | | | |    (_) |        
        | \  / | __ _  __| | | |     _| |__  ___ 
        | |\/| |/ _` |/ _` | | |    | | '_ \/ __|
        | |  | | (_| | (_| | | |____| | |_) \__ \
        |_|  |_|\__,_|\__,_| |______|_|_.__/|___/
                                         
        Fill in the blanks with adjectives, nouns, colors, adjectives, and more.
        Once all of the blanks have been filled the finished story will be revealed.
        """)

        for blank in self.blanks:
            self.words.append(input(f"\n{blank} \n> "))

        for sentence in self.story:
            index = self.story.index(sentence)
            if index < len(self.words):
                self.result += f"{sentence}{self.words[index]}"
            elif sentence != 0:
                self.result += f"{sentence}"
        
        print(f"\n\n\n{self.title} \n================\n")
        print(self.story)

        return self.result


game = Mad_Libs(response)
print(game.play())
