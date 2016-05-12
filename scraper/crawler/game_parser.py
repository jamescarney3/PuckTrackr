from bs4 import BeautifulSoup
import re

from utils import ABBREVIATIONS

whiteSpaceReducer = re.compile('(\s|\xa0|&nbsp;)+')
name_isolator = re.compile(' Game \d+ (Home|Away) Game \d+')
attendance_matcher = re.compile('(\d+,|)\d+')
arena_isolator = re.compile('(Attendance|Ass./Att) (\d+,|)\d+ (at|@) ')

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
    # if game_info_vals[2]:
    #     game_options['season'] = 'playoffs'
    game_options['date'] = game_info_vals[3]
    game_options['attendance'] = attendance_matcher.search(game_info_vals[4]).group()
    game_options['arena'] = arena_isolator.sub('', game_info_vals[4])
    # game_options['start'] = game_info_vals[5] ---- regexed for start time
    # game_options['end'] = game_info_vals[5] ---- regexed for end time
    game_options['home_team'] = name_isolator.sub('', home_info_vals[5])
    game_options['home_abbreviation'] = ABBREVIATIONS[name_isolator.sub('', home_info_vals[5]).lower()]
    game_options['home_score'] = int(home_info_vals[1])
    game_options['visitor_team'] = name_isolator.sub('', visitor_info_vals[5])
    game_options['visitor_abbreviation'] = ABBREVIATIONS[name_isolator.sub('', visitor_info_vals[5]).lower()]
    game_options['visitor_score'] = int(visitor_info_vals[1])

    return game_options
