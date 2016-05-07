from bs4 import BeautifulSoup
import re

whiteSpaceReducer = re.compile('(\s|\xa0|&nbsp;)+')

def parse_game(visitor_info, home_info, game_info):
    visitor_info_vals = []
    home_info_vals = []
    game_info_vals = []
    game_options = {}

    for td in visitor_info('td'):
        visitor_info_vals.append(whiteSpaceReducer.sub(' ', td.get_text(' ', strip=True)))

    for td in home_info('td'):
        home_info_vals.append(whiteSpaceReducer.sub(' ', td.get_text(' ', strip=True)))

    for td in game_info('td'):
        game_info_vals.append(whiteSpaceReducer.sub(' ', td.get_text(' ', strip=True)))

    game_options['serial'] = re.compile('\D').sub('', game_info_vals[6])
    # in progress - make this work with url_id for a given game
    # if game_info_vals[2]:
    #     game_options['season'] = 'playoffs'
    game_options['date'] = game_info_vals[3]
    # game_options['attendance'] = game_info_vals[4] ---- regexed for number
    # game_options['arena'] = game_info_vals[4] ---- regexed for arena name
    # game_options['start'] = game_info_vals[5] ---- regexed for start time
    # game_options['end'] = game_info_vals[5] ---- regexed for end time

    return game_options
