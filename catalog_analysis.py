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


if __name__ == "__main__":
    main()
