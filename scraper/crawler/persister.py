from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('postgresql://postgres@localhost/hockey')
