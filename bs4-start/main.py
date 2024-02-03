from bs4 import BeautifulSoup
import requests

response = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text
soup = BeautifulSoup(content, "html.parser")

movie_data = soup.find_all("h3", class_="title")

movie_list = [movie.text for movie in movie_data]

with open(file='bs4-start/The_100_Greatest_Movies.txt', mode='a') as file:
    for n in range(1, len(movie_list)):
        file.write(f"{movie_list[-n]}\n")
