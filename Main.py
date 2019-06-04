from Books import Books
from Coloring import Coloring
from Calendar import Calendar
from BookStore import BookStore


def main():
    bukva = BookStore()

    book1 = Books("Stephan King", 1, 5, 100.0, 200, "Fog",
                  18, "O'Relly", 6437484355314, "Nice book")

    coloring1 = Coloring(5, 25, 15, "Sun", 0, "Rainbow",
                         5634264385168, "Nice Coloring")

    calendar1 = Calendar(1, 10, 12, "2019", 7, "Cal",
                         7134264385168, "Nice Calendar")

    bukva.add_item(book1)
    bukva.add_item(coloring1)
    bukva.add_item(calendar1)

    for element in bukva.get_list_of_items():
        print("Bukva: " + element)


if __name__ == "__main__":
    main()
