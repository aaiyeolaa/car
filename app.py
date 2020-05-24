from search import Search

searched_cars = dict()
USER_PROMPT = "Enter C to search for a car, or P to print available, S to show previous, and q to quit"


def menu():

    print_cars()
    options = input(USER_PROMPT)

    while options!='q':
        if options == 'c':
            create_a_search()
        elif options == 'p':
            print_cars()
        elif options == 's':
            view_previous_searches()
        options = input(USER_PROMPT)




def print_cars():
    for key, car in searched_cars.items():
        print('{}'.format(car))

def create_a_search():
    search_type = input("Enter search details:")
    searched_cars[search_type] = Search(search_type)

def view_previous_searches():
    search_type = input("Enter previous search:")
    print_cars(searched_cars[search_type])


