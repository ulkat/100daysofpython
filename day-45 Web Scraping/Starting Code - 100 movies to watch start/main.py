import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")

movie_names =[name.getText() for name in  soup.find_all(name="h3", class_="title")]
movie_names.reverse()

with open("movies.txt", "w") as file:
    for movie in movie_names:
        file.write(f"{movie} \n")
