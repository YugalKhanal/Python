import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990}
]

writing_data = json.dumps(movies)
Path("movies.json").write_text(writing_data)
print(writing_data)

read_data = Path("movies.json").read_text()
read_movies = json.loads(read_data)
print(read_movies)
print(read_movies[0]["title"])