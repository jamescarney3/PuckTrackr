

base_url = 'http://www.nhl.com/scores/htmlreports/';

# each integer will be preceded by a '0' during url construction
season_prefixes = {
    'preseason': 1,
    'season': 2,
    'postseason': 3}
postseason_rounds = [1, 2, 3, 4]
# each round will have 2^(4-round) series
# each series will have 1-7 games
