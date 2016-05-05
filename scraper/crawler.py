from datetime import date

base_url = 'http://www.nhl.com/scores/htmlreports/';

START_YEAR = 2010
SEPTEMBER = 9

# regular season & preseason start constant
START_GAME = 1

# playoff constants
START_ROUND = 1
START_SERIES = 1
START_SERIES_GAME = 1
POSTSEASON_ROUNDS = 4
# series number always = 2^(4-<current round>)
SERIES_MAX_GAMES = 7

# universal serialization constants
SEASON_FLAGS = {
    'preseason': 1,
    'season': 2,
    'postseason': 3}

# NB
# for testing i'll assume each preseason has 120 games, each season
# has 1230 games, and each playoff series goes 7 games

def generate_urls(
    year=START_YEAR,
    flag=SEASON_FLAGS['preseason'],
    game=START_GAME,
    playoff_round=START_ROUND,
    series=START_SERIES,
    series_game=START_SERIES_GAME):

    game_urls = []
    today = date.today()

    # if september, use <this year><next year>
    while year < today.year or year <= today.year and today.month >= SEPTEMBER:
        year_string = str(year) + str(year + 1)
        while flag <= len(SEASON_FLAGS):
            add_game_strings(
                game_urls,
                year_string,
                flag, game,
                playoff_round,
                series,
                series_game)
            flag += 1

        flag = 1
        year += 1

    return game_urls

def add_game_strings(game_urls, year_string, flag, game, playoff_round, series, series_game):
    flag_string = str(flag).zfill(2)
    if flag == SEASON_FLAGS['preseason']:
        # magic number to be expunged when logic lands for finding last
        while game <= 120:
            game_string = str(game).zfill(4)
            game_urls.append(build_url(year_string, flag_string, game_string))
            game += 1
        game = 1

    elif flag == SEASON_FLAGS['season']:
        # magic number to be expunged when logic lands for finding last
        while game <= 1230:
            game_string = str(game).zfill(4)
            game_urls.append(build_url(year_string, flag_string, game_string))
            game += 1
        game = 1

    elif flag == SEASON_FLAGS['postseason']:
        add_playoff_game_strings(
            game_urls,
            year_string,
            flag, game,
            playoff_round,
            series,
            series_game)

def add_playoff_game_strings(game_urls, year_string, flag, game, playoff_round, series, series_game):
    while playoff_round <= POSTSEASON_ROUNDS:
        round_string = str(playoff_round)
        while series <= 2**(POSTSEASON_ROUNDS - playoff_round):
            series_string = str(series)
            while series_game <= 7:
                game_string = str(series_game)
                game_urls.append(
                    build_url(
                        year_string,
                        flag_string,
                        build_playoff_game_string(
                            round_string,
                            series_string,
                            game_string)))
                series_game += 1

            series_game = 1
            series += 1

        series = 1
        playoff_round += 1


def build_url(year_string, flag_string, game_string):
    return base_url + year_string + '/PL' + flag_string + game_string + '.HTM'

def build_playoff_game_string(round_string, series_string, game_string):
    return (round_string + series_string + game_string).zfill(4)
