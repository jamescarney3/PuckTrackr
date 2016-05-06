import json
import os

from url_builder import build_url, get_serial_num
from soup_scraper import parse_full_report

SEPTEMBER = 9
POSTSEASON_ROUNDS = 4
TIMES_FAILED_LIMIT = 10
GAMES_PER_PRESEASON = 120
SERIES_MAX_GAMES = 7
SEASON_FLAGS = {
    'preseason': 1,
    'season': 2,
    'postseason': 3}

def process_next_game(left_off):
    try:
        save_game_json(left_off)
        left_off['times_failed'] = 0
        print 'game saved for ' + build_url(left_off) + '!'
        # log_success(build_url(left_off))
    except TypeError:
        left_off['times_failed'] += 1
        print 'no game data for ' + build_url(left_off) + '!'
        # log_failure(build_url(left_off))

    update_left_off(increment_left_off(left_off))

def increment_left_off(left_off):
    if left_off['season_flag'] == SEASON_FLAGS['preseason'] or left_off['season_flag'] == SEASON_FLAGS['season']:
        if left_off['times_failed'] < TIMES_FAILED_LIMIT:
            left_off['game'] += 1
        else:
            left_off['times_failed'] = 0
            left_off['game'] = 1
            left_off['season_flag'] += 1
    elif left_off['season_flag'] == SEASON_FLAGS['postseason']:
        if left_off['game'] < SERIES_MAX_GAMES:
            left_off['game'] += 1
        elif left_off['series'] < 2**(POSTSEASON_ROUNDS - left_off['round']):
            left_off['game'] = 1
            left_off['series'] += 1
        elif left_off['round'] < POSTSEASON_ROUNDS:
            left_off['game'] = 1
            left_off['series'] = 1
            left_off['round'] +=1
        else:
            left_off['times_failed'] = 0
            left_off['game'] = 1
            left_off['round'] = 1
            left_off['series'] = 1
            left_off['season_flag'] = 1
            left_off['year'] += 1
    return left_off

def update_left_off(left_off):
    json.dump(left_off, open('left_off.json', 'wb'))

def save_game_json(left_off):
    url = build_url(left_off)
    serial_num = get_serial_num(left_off)
    save_dir = 'data_out/' + str(left_off['year']) + str(left_off['year'] + 1)

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    parse_full_report(url, save_dir, serial_num)
