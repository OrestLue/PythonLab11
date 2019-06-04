from Stuff import Stuff


class Books(Stuff):
    author = ""
    illustrations = False

    def __init__(self, author_obj, illustrations_obj, quantity, price,
                 number_of_pages, title, age, publishing_house, ean13,
                 description):
        self.author = author_obj
        self.illustrations = illustrations_obj
        self.quantity = quantity
        self.price = price
        self.number_of_pages = number_of_pages
        self.title = title
        self.age = age
        self.publishing_house = publishing_house
        self.ean13 = ean13
        self.description = description

    def get_author(self):
        return self.author

    def set_author(self, author_obj):
        self.author = author_obj

    def contain_illustration(self):
        return self.illustrations

    def set_illustrations(self, illustrations_obj):
        self.illustrations = illustrations_obj

    def get_kind_of_book(self):
        return self.kind_of_book

    def set_kind_of_book(self, kind_of_book_obj):
        self.kind_of_book = kind_of_book_obj
