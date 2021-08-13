# movie description extension

class Movie:
    def __init__(self, lang, char, length):
        self.lang = lang
        self.length = length
        self. char = char

    @staticmethod
    def certify(length, char):
        if(length <= 240 and char >= 2):
            return (True)
        return (False)

    def run(self, status):
        print("This is a" + self.lang + "movie with" + str(self.num +
              " character, is" + str(self.length) + " minutes long,and is " + status + " . ")


movie=Movie(input(), int(input()), int(input()))
cert=None
if(Movie.certify(movie)):
    cert="Certified"
else:
    cert="not Certified"
movie.run(cert)
