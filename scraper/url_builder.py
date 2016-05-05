BASE_URL = 'http://www.nhl.com/scores/htmlreports/';
SEASON_FLAGS = {
    'preseason': 1,
    'season': 2,
    'postseason': 3}

def build_url(left_off):
    serial_string = get_serial_num(left_off)
    year_string = str(left_off['year']) + str(left_off['year'] + 1)
    return BASE_URL + year_string + '/PL' + serial_string + '.HTM'

def get_serial_num(left_off):
    if (   SEASON_FLAGS['preseason'] == left_off['season_flag']
        or SEASON_FLAGS['season'] == left_off['season_flag']):
        serial_string = str(left_off['season_flag']).zfill(2) + str(left_off['game']).zfill(4)
        return serial_string
    if SEASON_FLAGS['postseason'] == left_off['season_flag']:
        game_serial_string = (str(left_off['round']) + str(series) + str(left_off['game'])).zfill(4)
        serial_string = str(left_off['season_flag']).zfill(2) + game_serial_string
        return serial_string
