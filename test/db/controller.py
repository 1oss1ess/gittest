from model import Person
import view


def showAll():
    people_in_db = Person.getAll()

    return view.showAllView(people_in_db)


def start():
    view.startView()
    input_query = input()
    if input_query == 'y':
        return showAll()
    else:
        return view.endView()


if __name__ == "__main__":
    start()
