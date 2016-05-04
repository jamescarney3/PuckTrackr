import requests
import re
import json

from game_parser import parse_game
from event_parser import parse_event

from bs4 import BeautifulSoup

# workflow here should roughly be:
# - request game report from url
# - on a 200 response parse html body into a representative dict
# - save dict as .json file (@TODO give munch_report a way to
#   know what dir to save a given game json object to)
# - make entries into a central db for game and all corresponding
#   event records

# blockers:
# - @TODO need a way to interact with db from scraper, decide
#   which db to use
# - @TODO need some sort of controller to periodically scrape for
#   games, keep track of its own progress, and generate URLs /
#   dir names to pass to parse_full_report

def munch_report(url):
    content = requests.get(url).content
    soup = BeautifulSoup(content)
    events = soup.find_all('tr', {'class': 'evenColor'})
    visitor_info = soup.find('table', {'id': 'Visitor'})
    home_info = soup.find('table', {'id': 'Home'})
    game_info = soup.find('table', {'id': 'GameInfo'})

    return {
        'events': events,
        'visitor_info': visitor_info,
        'home_info': home_info,
        'game_info': game_info
    }

def parse_full_report(url):
    data = munch_report(url)
    game = parse_game(
        data['visitor_info'],
        data['home_info'],
        data['game_info'])

    events = []
    for event in data['events']:
        events.append(parse_event(event))

    game['events'] = events
    json.dump(game, open('data_out/game.json', 'wb'))
    return game
