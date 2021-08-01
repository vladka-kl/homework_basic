from typing import List


class Book:
    """simplified book model"""

    def __init__(self, author, name, year_of_publishing, genre):
        self.author = author
        self.name = name
        self.year_of_publishing = year_of_publishing
        self.genre = genre
        self.reviews = []

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

    def review(self, user, quality, review):
        self.reviews.append(Review(user, quality, review))

    def info_book(self):
        for i in (self.author, self.name, self.year_of_publishing, self.genre):
            print(f"- {i}")
        for review in self.reviews:
            print(review)

class Review:
    """simplified review model"""

    def __init__(self, user, quality, review):
        self.user = user
        self.quality = quality
        self.review = review

    def __str__(self):
        return "REVIEW INFO \n user: {} \n pos/neg: '{}' \n review : {}".format \
            (self.user, self.quality, self.review)


if __name__ == '__main__':
    book_1 = Book("Royte", "Garbage land", 2006, "non-fiction")
    book_2 = Book("Andrukhovych", "Amadoka", 2020, "fiction")

    book_1.review("true_environmentalist666", "positive", "It changed my life")
    book_1.review("makeAmericaGREAT_111", "negative","A bunch of bullshit")
    book_2.review("ukrsoul", "positive", "really enjoyed the plot")

    is_eq = (book_1 == book_2)
    print(is_eq)
    book_1.info_book()

    book_2.info_book()

