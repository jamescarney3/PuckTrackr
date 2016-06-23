from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('postgresql://postgres@localhost/hockey')

metadata = MetaData(db)
players = Table('players', metadata,
    Column('id', Integer, primary_key=True),
    Column('first', String(40)),
    Column('last', String(40)),
    Column('number', Integer),
    Column('team', String)
)

# needs a join with players
events = Table('events', metadata,
    Column('id', Integer, primary_key=True),
    Column('game_id', Integer, ForeignKey('games.id')),
    Column('serial', Integer),
    Column('period', Integer),
    Column('personnel', String),
    Column('time_elapsed', Interval),
    Column('time_remaining', Interval),
    Column('event_type', String),
    Column('description', String),
    Column('team', String)
)

player_events = Table('player_events', metadata,
    Column('id', Integer, primary_key=True),
    Column('player_id', Integer, ForeignKey('players.id')),
    Column('event_id', Integer, ForeignKey('events.id'))
)

games = Table('games', metadata,
    Column('id', Integer, primary_key=True),
    Column('serial', Integer),
    Column('date', Date),
    Column('attendance', Integer),
    Column('arena', String),
    Column('home_team', String),
    Column('home_score', Integer),
    Column('home_abbreviation', String(3)),
    Column('visitor_team', String),
    Column('visitor_score', Integer),
    Column('visitor_abbreviation', String(3)),
    Column('url', String)
)

metadata.create_all(db)
