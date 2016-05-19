from bs4 import BeautifulSoup
import re

def parse_roster(player_headings):
    players = []
    for heading in player_headings:
        number = re.compile('\d+').search(heading.get_text()).group()
        name = re.compile('\d+ ').sub('', heading.get_text(' ', strip=True))
        last = name.split(',')[0].strip()
        first = name.split(',')[1].strip()
        players.append({
            'number': number,
            'first': first,
            'last': last})
    return players
