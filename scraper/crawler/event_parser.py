from bs4 import BeautifulSoup
import re

whiteSpaceReducer = re.compile('(\s|\xa0|&nbsp;)+')

def parse_event(event_el):
    vals = []
    event_options = {}

    for td in event_el.find_all('td', recursive=False):
        vals.append(whiteSpaceReducer.sub(' ', td.get_text(' ', strip=True)))

    event_options['serial'] = vals[0]
    event_options['period'] = vals[1]
    if vals[2]:
        event_options['personnel'] = vals[2]
    event_options['time_elapsed'] = vals[3].split()[0]
    event_options['time_remaining'] = vals[3].split()[1]
    event_options['event_type'] = vals[4]
    event_options['description'] = vals[5]
    if vals[4] != 'STOP' and vals[4] != 'PSTR' and vals[4] != 'PEND' and vals[4] != 'GEND':
        event_options['team'] = vals[5][0:3]
    if vals[6]:
        event_options['visitor_players'] = parse_on_ice(vals[6])
    if vals[7]:
        event_options['home_players'] = parse_on_ice(vals[7])

    return event_options

def parse_on_ice(player_table_text):
    players = []
    els = player_table_text.split()
    while len(els) >= 2:
        players.append({
            'number': els.pop(0),
            'position': els.pop(0)})

    return players
