import re
import json

from bs4 import BeautifulSoup

from url_builder import build_game_report_url, build_home_roster_url, build_visitor_roster_url
from game_parser import parse_game
from roster_parser import parse_roster

# - @TODO update event_parser to give events home_players and visitor_players props

def parse_full_report(left_off):
    game_report_url = build_game_report_url(left_off)
    home_roster_url = build_home_roster_url(left_off)
    visitor_roster_url = build_visitor_roster_url(left_off)

    game_json = parse_game(game_report_url)
    home_players = parse_roster(home_roster_url)
    visitor_players = parse_roster(visitor_roster_url)

    game_json['home_players'] = home_players
    game_json['visitor_players'] = visitor_players

    return game_json
