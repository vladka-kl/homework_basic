class Book:
    """simplified book model"""

    def __init__(self, author, name, year_of_publishing, genre, *reviews):
        self.author = author
        self.name = name
        self.year_of_publishing = year_of_publishing
        self.genre = genre
        self.reviews = reviews

    def print_reviews(self):
       

    def __repr__(self):
        return "{}, {}, {}, {}".format(self.author, self.name,
                                       self.year_of_publishing, self.genre)

    def __str__(self):
        return "The author of the book '{}' is {}. " \
               "The year it was published: {}. " \
               "The genre: {}".format(self.name, self.author,
                                      self.year_of_publishing, self.genre)

    def __eq__(self, other):
        return self.author == other.author and \
               self.name == other.name and self.year_of_publishing == \
               other.year_of_publishing and self.genre == other.genre


book_1 = Book("Royte", "Garbage land", 2006, "non-fiction")
book_2 = Book("Andrukhovych", "Amadoka", 2020, "fiction")

is_eq = (book_1 == book_2)
print(is_eq)

print(book_1)


class Review:

    def __init__(self, user, quality, book, review):
        self.user = user
        self.quality = quality
        self._book = book
        self.review = review

    def __str__(self):
        return "User {} left a {} review about '{}' and says: {}".format \
            (self.user, self.quality, self._book, self.review)


review_1 = Review("true_environmentalist666", "positive", "Garbage land",
                  "It changed my life")
review_2 = Review("makeAmericaGREAT_111", "negative", "Garbage land",
                  "A bunch of bullshit")
review_3 = Review("ukrsoul", "positive", "Amadoka", "really enjoyed the plot")
