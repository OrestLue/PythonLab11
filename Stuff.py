class Stuff:
    quantity = 0
    price = 0.0
    number_of_pages = 0
    title = ""
    publishing_house = ""
    ean13 = 0
    age = 0
    description = ""

    class Stuff:
        def __init__(self, quantity_obj, price_obj, number_of_pages_obj, title_obj,
                     publishing_house_obj, ean13_obj, age_obj, description_obj):
            self.quantity = quantity_obj
            self.price = price_obj
            self.numberOfPages = number_of_pages_obj
            self.title = title_obj
            self.publishingHouse = publishing_house_obj
            self.ean13 = ean13_obj
            self.age = age_obj
            self.description = description_obj

    def get_title(self):
        return self.title

    def set_title(self, title_obj):
        self.title = title_obj
