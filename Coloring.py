from Stuff import Stuff


class Coloring(Stuff):

    def __init__(self, quantity, price, number_of_pages, title,
                 age, publishing_house, ean13, description):
        self.quantity = quantity
        self.price = price
        self.number_of_pages = number_of_pages
        self.title = title
        self.age = age
        self.publishing_house = publishing_house
        self.ean13 = ean13
        self.description = description
