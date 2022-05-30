from bs4 import BeautifulSoup
import requests, re

points = {
    "bdsm": 6,
    "fantasy": 4,
    "filmed": 4,
    "foot job": 4,
    "futanari": 4,
    "gangbang": 6,
    "incest": 4,
    "inflation": 8,
    "lactation": 8,
    "loli": 10,
    "mind break": 8,
    "mind control": 8,
    "monster": 6,
    "nekomimi": 4,
    "ntr": 6,
    "orgy": 6,
    "pregnant": 8,
    "rape": 15,
    "rimjob": 10,
    "scat": 50,
    "tentacle": 6,
    "ugly bastard": 10
}


def main(urls):
    links = get_tags(urls)
    response = rate(links)
    return response


def get_tags(urls):
    links = None

    url = requests.get(urls)
    soup = BeautifulSoup(url.text, 'html.parser')
    links = [link["href"] for link in soup.find_all('a', {"href": re.compile('^/browse/tags/'), "class": "ml-0 "
                                                                                                         "mr-3 "
                                                                                                         "btn "
                                                                                                         "btn"
                                                                                                         "--outline"
                                                                                                         " btn--dep"
                                                                                                         "ressed bt"
                                                                                                         "n--router"
                                                                                                         " grey--te"
                                                                                                         "xt"})]
    return links


def rate(links):
    rank_value = 0
    has_multiple = 0
    response = str()
    tags = [link[13:] for link in links]
    for tag in tags:
        if tag == "gangbang" or "orgy":
            has_multiple = 1
        try:
            if not tag == "gangbang" or "orgy" and not has_multiple == 1:
                rank_value += points[str(tag)]
        except KeyError:
            pass
    if rank_value == 0:
        response = "wow your boring"
    if rank_value in range(3, 9):
        response = "nothing wrong with a little kinks!"
    if rank_value in range(9, 17):
        response = "now thats pretty weird man"
    if rank_value in range (17, 30):
        response = "please get help. please."
    if rank_value >= 30:
        response = "you are the lowest of the low."
    return response
