def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'student_name': 'Norlon Sibug',
        'id': 10312229,
        'pizza_toppings': [
            'Pepperoni',
            'Pineapple',
            'Shrimp'
        ],
        'movie_genres': [
            {
                'title': 'Black Hawk Down',
                'genre': 'Action'
            },
            {
                'title': 'Home Alone',
                'genre': 'Comedy'
            }
        ]
    }

    print(about_me)
    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {
        'title': 'Space Jam',
        'genre': 'Animation'
    }
    about_me['movie_genres'].append(new_movie)
    
    print_student_name_and_id(about_me)

    new_toppings = ['Bacon', 'Extra Cheese']
    add_pizza_toppings(about_me, new_toppings)
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me['movie_genres'])

# TODO: Step 4 - Function that prints student name and ID    
def print_student_name_and_id(about_me):
    student_name = about_me['student_name']
    student_id = about_me['id']
    print(f'My name is {student_name}. My student ID is {student_id}')
    return

# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, pizza_toppings):
    about_me['pizza_toppings'].extend(pizza_toppings)
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    for topping in about_me['pizza_toppings']:
        print(f' * {topping}')
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie['genre'] for movie in about_me['movie_genres']]
    print(", ".join(genres))
    return

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_genres):
    titles = [movie['title'] for movie in movie_genres]
    print(", ".join(titles))
    return

if __name__ == '__main__':
    main()
