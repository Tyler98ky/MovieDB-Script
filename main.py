import requests
from PIL import Image
from io import BytesIO
import PIL


api_key = "031b87d57135d122fd6f7877bbeb9c77"


def print_popular():
    popular = requests.get('https://api.themoviedb.org/3/discover/movie?api_key={}&language=en-US&sort_by=popularity.desc&include_adult=fals'
                           'e&include_video=false&page=1&primary_release_year=2018'.format(api_key)).json()

    print("\nMost Popular Movies for 2018: \n")
    for x in range(20):
        print("{}. {}".format(x + 1, popular['results'][x]['title']))

        # Optional stuff to print the poster for movies
        # temp = requests.get('\t\thttps://image.tmdb.org/t/p/w500{}'.format(popular['results'][x]['poster_path']))
        # i = Image.open(BytesIO(temp.content))
        # i.show()

        for _ in range(50):
            print('-', end='')
        print('')


def print_in_theater():
    print("\n\n\n\nIn Theaters Now: \n")

    in_theaters = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key={}&language="
                               "en-US&page=1".format(api_key)).json()
    for x in range(20):
        print("{}. {}".format(x + 1, in_theaters['results'][x]['title']))
        for _ in range(50):
            print('-', end='')
        print('')


def print_coming_soon():
    print("\n\n\n\nComing Soon: \n")

    coming_soon = requests.get("https://api.themoviedb.org/3/movie/upcoming?api_key=031b87d57135d12"
                               "2fd6f7877bbeb9c77&language=en-US&page=1".format(api_key)).json()

    for x in range(20):
        print("{}. {}".format(x + 1, coming_soon['results'][x]['title']))

        for _ in range(50):
            print('-', end='')
        print('')


print_popular()
print_in_theater()
print_coming_soon()
