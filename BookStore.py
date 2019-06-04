class BookStore:
    store = []

    def get_list(self):
        return self.store

    def add_item(self, item):
        self.store.append(item)

    @staticmethod
    def sort_by_name(lst, rev):
        lst.sort(key=lambda x: x.name, reverse=rev)

    def sort_by_name(self, rev):
        self.store.sort(key=lambda x: x.name, reverse=rev)

    @staticmethod
    def sort_by_age(lst, rev):
        lst.store.sort(key=lambda x: x.age, reverse=rev)

    def sort_by_age(self, rev):
        self.store.sort(key=lambda x: x.age, reverse=rev)

    def get_list_of_items(self):
        array = []
        for i in self.store:
            array.append(i.get_title())

        return array
