from utils import SEASON_FLAGS
from utils import BASE_URL

def build_game_report_url(left_off):
    serial_string = get_serial_num(left_off)
    year_string = get_year_string(left_off)
    return BASE_URL + year_string + '/PL' + serial_string + '.HTM'

def build_home_roster_url(left_off):
    serial_string = get_serial_num(left_off)
    year_string = get_year_string(left_off)
    return BASE_URL + year_string + '/TH' + serial_string + '.HTM'

def build_visitor_roster_url(left_off):
    serial_string = get_serial_num(left_off)
    year_string = get_year_string(left_off)
    return BASE_URL + year_string + '/TV' + serial_string + '.HTM'

def get_serial_num(left_off):
    if (   SEASON_FLAGS['preseason'] == left_off['season_flag']
        or SEASON_FLAGS['season'] == left_off['season_flag']):
        serial_string = str(left_off['season_flag']).zfill(2) + str(left_off['game']).zfill(4)
        return serial_string
    if SEASON_FLAGS['postseason'] == left_off['season_flag']:
        game_serial_string = (str(left_off['round']) + str(left_off['series']) + str(left_off['game'])).zfill(4)
        serial_string = str(left_off['season_flag']).zfill(2) + game_serial_string
        return serial_string

def get_year_string(left_off):
    return str(left_off['year']) + str(left_off['year'] + 1)
