import random
import statistics
import matplotlib.pyplot as plt
import difflib

# === COLORS ===
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"


def print_menu():
    print(f"\n{CYAN}{BOLD}=== Movie Database ==={RESET}")
    print(f"{BLUE}1.{RESET} List Movies")
    print(f"{BLUE}2.{RESET} Add Movie")
    print(f"{BLUE}3.{RESET} Delete Movie")
    print(f"{BLUE}4.{RESET} Update Movie")
    print(f"{BLUE}5.{RESET} Stats")
    print(f"{BLUE}6.{RESET} Random Movie")
    print(f"{BLUE}7.{RESET} Search Movie")
    print(f"{BLUE}8.{RESET} Movies Sorted by Rating")
    print(f"{BLUE}9.{RESET} Exit")
    print(f"{BLUE}10.{RESET} Create Rating Histogram (Bonus)")


def pluralize(count, singular, plural=None):
    if count == 1:
        return f"{count} {singular}"
    return f"{count} {plural or singular + 's'}"


def list_movies(movies):
    count = len(movies)
    print(f"\n{MAGENTA}{pluralize(count, 'movie')} in total{RESET}")
    for title, rating in movies.items():
        print(f"{WHITE}{title}{RESET}: {YELLOW}{rating}{RESET}")


def add_movie(movies):
    title = input(f"{YELLOW}Enter movie name: {RESET}").strip()
    if not title:
        print(f"{RED}Movie name cannot be empty.{RESET}")
        return
    try:
        rating = float(input(f"{YELLOW}Enter rating (1-10): {RESET}").strip())
    except ValueError:
        print(f"{RED}Invalid rating. Expected a number.{RESET}")
        return
    movies[title] = rating
    print(f"{GREEN}Added/updated:{RESET} {title}: {rating}")


def delete_movie(movies):
    title = input(f"{YELLOW}Enter movie name to delete: {RESET}").strip()
    if title in movies:
        del movies[title]
        print(f"{GREEN}Deleted:{RESET} {title}")
    else:
        print(f"{RED}Error: Movie not found.{RESET}")


def update_movie(movies):
    title = input(f"{YELLOW}Enter movie name to update: {RESET}").strip()
    if title not in movies:
        print(f"{RED}Error: Movie not found.{RESET}")
        return
    try:
        rating = float(input(f"{YELLOW}Enter new rating (1-10): {RESET}").strip())
    except ValueError:
        print(f"{RED}Invalid rating. Expected a number.{RESET}")
        return
    movies[title] = rating
    print(f"{GREEN}Updated:{RESET} {title}: {rating}")


def movie_stats(movies):
    if not movies:
        print(f"{RED}No movies in database.{RESET}")
        return
    ratings = list(movies.values())
    avg = sum(ratings) / len(ratings)
    med = statistics.median(ratings)
    max_rating = max(ratings)
    min_rating = min(ratings)
    best = [title for title, r in movies.items() if r == max_rating]
    worst = [title for title, r in movies.items() if r == min_rating]

    print(f"\n{MAGENTA}{BOLD}=== Stats ==={RESET}")
    print(f"Average rating: {avg:.2f}")
    print(f"Median rating: {med:.2f}")
    print(f"{GREEN}Best movie(s):{RESET}")
    for b in best:
        print(f"  {b}: {max_rating}")
    print(f"{RED}Worst movie(s):{RESET}")
    for w in worst:
        print(f"  {w}: {min_rating}")


def random_movie(movies):
    if not movies:
        print(f"{RED}No movies in database.{RESET}")
        return
    title = random.choice(list(movies.keys()))
    print(f"{MAGENTA}Random pick:{RESET} {title}: {YELLOW}{movies[title]}{RESET}")


def search_movie(movies):
    query = input(f"{YELLOW}Enter part of movie name: {RESET}").strip()
    if not query:
        print(f"{RED}Search query cannot be empty.{RESET}")
        return

    query_lower = query.lower()
    found = [(t, r) for t, r in movies.items() if query_lower in t.lower()]

    if found:
        print(f"{GREEN}Matches found:{RESET}")
        for t, r in found:
            print(f"{t}, {r}")
        return

    # Fuzzy matching (bonus)
    titles = list(movies.keys())
    close_matches = difflib.get_close_matches(query, titles, n=3, cutoff=0.6)

    if close_matches:
        print(f'\n{RED}The movie "{query}" does not exist.{RESET}')
        print(f"{CYAN}Did you mean:{RESET}")
        for match in close_matches:
            print(f"- {match}")
    else:
        print(f'{RED}No matches or similar titles found for "{query}".{RESET}')


def movies_sorted_by_rating(movies):
    if not movies:
        print(f"{RED}No movies in database.{RESET}")
        return
    sorted_items = sorted(movies.items(), key=lambda x: (-x[1], x[0].lower()))
    print(f"{MAGENTA}{BOLD}Movies sorted by rating:{RESET}")
    for title, rating in sorted_items:
        print(f"{title}: {YELLOW}{rating}{RESET}")


def create_histogram(movies):
    if not movies:
        print(f"{RED}No movies in database.{RESET}")
        return
    filename = input(f"{YELLOW}Enter filename to save histogram (e.g. ratings_histogram.png): {RESET}").strip()
    if not filename:
        print(f"{RED}Filename cannot be empty.{RESET}")
        return

    ratings = list(movies.values())

    plt.figure(figsize=(8, 5))
    plt.hist(ratings, bins=10, range=(1, 10), edgecolor='black', color='skyblue')
    plt.title("Movie Ratings Histogram")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.savefig(filename)
    plt.close()
    print(f"{GREEN}Histogram saved to {filename}{RESET}")


def main():
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    while True:
        print_menu()
        choice = input(f"{YELLOW}Choose an option (1-10): {RESET}").strip()

        if choice == "1":
            list_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            update_movie(movies)
        elif choice == "5":
            movie_stats(movies)
        elif choice == "6":
            random_movie(movies)
        elif choice == "7":
            search_movie(movies)
        elif choice == "8":
            movies_sorted_by_rating(movies)
        elif choice == "9":
            print(f"{GREEN}Goodbye!{RESET}")
            break
        elif choice == "10":
            create_histogram(movies)
        else:
            print(f"{RED}Invalid option. Please choose a number between 1 and 10.{RESET}")


if __name__ == "__main__":
    main()