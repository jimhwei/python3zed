class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics
    #this here creates the magic init function
    #without it the function would be empty, it's body of the class

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

hbd = ["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"]

happy_bday = Song(hbd)

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

ants = Song(["The ants go marching one by one",
                "hoorah",
                "hoorah"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

ants.sing_me_a_song()

'''without the dunders on the init function
class song will not take any objects'''
