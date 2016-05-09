import json
import os
import datetime

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
        game_json = parse_full_report(build_url(left_off))
        save_game_json(game_json, left_off)
        log_success(build_url(left_off))
        left_off['times_failed'] = 0
    except TypeError:
        log_failure(build_url(left_off))
        left_off['times_failed'] += 1

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

def scraper_root_dir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def update_left_off(left_off):
    json.dump(left_off, open(scraper_root_dir() + '/resources/left_off.json', 'wb'))

def save_game_json(game_json, left_off):
    serial_num = get_serial_num(left_off)
    save_dir = scraper_root_dir() + '/data_out/' + str(left_off['year']) + str(left_off['year'] + 1)

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    json.dump(game_json, open(save_dir + '/' + serial_num, 'wb'))

def log_success(url):
    save_dir = scraper_root_dir() + '/logs'
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
    with open(save_dir + '/success.log', 'a') as success_log:
        success_log.write(timestamp + 'success: ' + url + '\n')

def log_failure(url):
    save_dir = scraper_root_dir() + '/logs'
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
    with open(save_dir + '/success.log', 'a') as failure_log:
        failure_log.write(timestamp + ' failed: ' + url + '\n')
