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
# - @TODO NEED NEED NEED error handling at the soup_scraper layer
#   in case a url is dead or empty or otherwise not the expected
#   game report
# - @TODO need a way to interact with db from scraper, decide
#   which db to use
# - @TODO need some sort of controller to periodically scrape for
#   games

def parse_full_report(url, save_dir, serial_num):
    content = requests.get(url).content
    soup = BeautifulSoup(content)
    events = soup.find_all('tr', {'class': 'evenColor'})
    visitor_info = soup.find('table', {'id': 'Visitor'})
    home_info = soup.find('table', {'id': 'Home'})
    game_info = soup.find('table', {'id': 'GameInfo'})

    game = parse_game(home_info, visitor_info, game_info)
    game['events'] = []

    for event in events:
        game['events'].append(parse_event(event))

    json.dump(game, open(save_dir + '/' + serial_num, 'wb'))

    return game
