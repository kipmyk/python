class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
        self.is_available = True

class MovieStore:
    def __init__(self):
        self.inventory = []

    def add_movie(self, movie):
        self.inventory.append(movie)

    def show_available_movies(self):
        available = [movie for movie in self.inventory if movie.is_available]
        for movie in available:
            print(f"Title: {movie.title}, Director: {movie.director}, Status: Available")

    def rent_movie(self, title):
        for movie in self.inventory:
            if movie.title == title and movie.is_available:
                movie.is_available = False
                print(f"You rented: {title}")
                return
        print(f"'{title}' is currently out of stock.")

    def return_movie(self, title):
        for movie in self.inventory:
            if movie.title == title and not movie.is_available:
                movie.is_available = True
                print(f"Returned: {title}")
                return
        print(f"No record of rental found for '{title}' or it's already returned.")

# Example usage
store = MovieStore()
store.add_movie(Movie("Inception", "Christopher Nolan"))
store.add_movie(Movie("The Matrix", "Wachowskis"))

print("Available movies:")
store.show_available_movies()

store.rent_movie("Inception")

print("\nAfter renting:")
store.show_available_movies()

store.return_movie("Inception")

print("\nAfter return:")
store.show_available_movies()
