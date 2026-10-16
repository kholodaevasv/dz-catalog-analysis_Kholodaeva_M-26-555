import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    """Возвращает среднюю оценку по каталогу, округленную до одного знака"""
    total = 0.0
    if len(movies) == 0:
        return total

    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """
    Возвращает кортеж (самый старый фильм в годах, самый новый фильм в годах,
    среднее), где среднее округлено вверх до целого с помощью math.ceil
    """
    if len(movies) == 0:
        return (0, 0, 0)

    ages = [current_year - movie["year"] for movie in movies]
    oldest_film = max(ages)
    newest_film = min(ages)
    avg_age = math.ceil(sum(ages) / len(ages))
    return (oldest_film, newest_film, avg_age)


def duration_in_hours(minutes):
    '''Переводит минуты в формат "2ч 35м"'''
    h = minutes // 60
    min = minutes % 60
    return f"{h}ч {min}м"


def rating_tier(rating):
    """По оценке возвращает категорию"""
    if rating >= 9:
        return "шедевр (обязательно к просмотру)" if rating >= 9.5 else "шедевр"
    elif 7 <= rating < 9:
        return "хорошо (стоит посмотреть)" if rating >= 8 else "хорошо"
    elif 5 <= rating < 7:
        return "средне" if rating >= 6 else "средне (не стоит тратить время)"
    else:
        return "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новый"
        case _ if 2015 <= year <= 2020:
            return "недавний"
        case _ if year < 2015:
            return "старый"


def print_non_comedy_titles(movies):
    titles = []
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        titles.append(movie["title"])
    print(f"Некомедийные фильмы: {', '.join(titles)}")


def find_first_masterpiece(movies):
    m = 0
    while m < len(movies):
        if movies[m]["rating"] > 9.0:
            print(f"Первый шедевр: {movies[m]['title']}")
            break
        m += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold):
    counter = 0
    for movie in movies:
        duration = movie.get("duration_min", 0)
        if duration > threshold:
            counter += 1
    return counter


def normalize_title(title):
    title = title.split(" ")
    norm_title = []
    for word in title:
        word = word[0].upper() + word[1:]
        norm_title.append(word)
    return " ".join(norm_title)


def make_slug(title):
    title = normalize_title(title)
    slug_title = title.lower()
    slug_title = slug_title.replace(" ", "-")
    return slug_title


def format_report_line(movie):
    title = movie.get("title", "")
    year = movie.get("year", 0)
    rating = movie.get("rating", 0.0)
    duration_min = movie.get("duration_min", 0)

    title = normalize_title(title)

    duration = duration_in_hours(duration_min)

    genres = movie.get("genres", "")
    genres = list(genres)
    genres.sort()
    genres = ", ".join(genres)

    return f"{title} ({year}) - {rating}/10, {duration}, жанры: {genres}"


def main():
    avg_rating = average_rating(movies)
    print(f"Средняя оценка по каталогу: {avg_rating}")

    oldest, newest, avg_age = catalog_age_stats(movies)
    print(
        f"Самый старый фильм = {oldest}, "
        f"cамый новый фильм = {newest}, "
        f"cредний возраст фильмов = {avg_age}"
    )

    sample_duration = movies[0]["duration_min"]
    print(f"Длительность первого фильма: {duration_in_hours(sample_duration)}")

    for movie in movies:
        print(
            f"Фильм {movie["title"]} с рейтингом {movie["rating"]}: "
            f"{rating_tier(movie["rating"])}"
        )
        print(f"Фильм {movie["title"]} {movie["year"]}: {decade_label(movie["year"])}")

    print_non_comedy_titles(movies)

    find_first_masterpiece(movies)

    long_movies = count_long_movies(movies, 120)
    print(f"Количество фильмов длинее 120 минут: {long_movies}")

    print(
        f"normalize_title: "
        f'{normalize_title("silent hours")}'
    )

    print(
        f"make_slug: "
        f'{make_slug("silent hours")}'
    )

    print("format_report_line:")
    for movie in movies:
        print(format_report_line(movie))


if __name__ == "__main__":
    main()
