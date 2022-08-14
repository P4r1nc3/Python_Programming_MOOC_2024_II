# Write your solution here:
class Series:
    def __init__(self, title:str, seasons:int, genres:list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
    
    def __str__(self):
        to_print = ''
        to_print += f'{self.title} ({self.seasons} seasons)\n'
        genres_str = ', '.join(self.genres)
        to_print += f'genres: {genres_str}\n'
        if len(self.ratings) > 0:
            to_print += f'{len(self.ratings)} ratings, average {self.get_avg_rating()} points'
        else:
            to_print += 'no ratings'
        return to_print

    def get_avg_rating(self):
        if len(self.ratings) > 0:
            avg_ratings = sum(self.ratings)/len(self.ratings)
            return round(avg_ratings, 1)
        else:
            return -1

    def rate(self, rating: int):
        self.ratings.append(rating)

def minimum_grade(grade:float, series_list:list):
    found = []
    for series in series_list:
        if series.get_avg_rating() > grade:
            found.append(series)
    return found

def includes_genre(genre: str, series_list: list):
    found = []
    for series in series_list:
        for ser_genre in series.genres:
            if ser_genre == genre:
                found.append(series)
                break
    return found