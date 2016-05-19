import requests
import re
import json

from game_parser import parse_game
from event_parser import parse_event
from roster_parser import parse_roster

from bs4 import BeautifulSoup

# workflow here should roughly be:
# - request game report from url
# - on a 200 response parse html body into a representative dict
# - save dict as .json file
# - make entries into a central db for game and all corresponding
#   event records

# blockers:
# - @TODO need a way to interact with db from scraper, decide
#   which db to use
# - @TODO need some sort of controller to periodically scrape for
#   games

# pattern here should instead be:
# --> take in a left_off hash
# --> build urls for game report and TOI reports
# --> parse game report heading data with game_parser
# --> parse game report events with event_parser
# @TODO update event_parser to extract a player # from event description
# @TODO update event_parser to parse on_ice fields into arrays of numbers
# --> parse TOI reports for home & visitor rosters with roster_parser
# --> add events and rosters to game json as events, home_players, away_players

def parse_full_report(url):
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

    game['url'] = url

    return game
