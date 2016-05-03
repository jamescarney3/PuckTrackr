import requests
import re
from bs4 import BeautifulSoup

whiteSpaceReducer = re.compile('(\s|\xa0|&nbsp;)+')

def munch_report(url):
    content = requests.get(url).content
    soup = BeautifulSoup(content)
    events = soup.find_all('tr', {'class': 'evenColor'})
    visitorInfo = soup.find('table', {'id': 'Visitor'})
    homeInfo = soup.find('table', {'id': 'Home'})
    gameInfo = soup.find('table', {'id': 'GameInfo'})

    return {
        'events': events,
        'visitorInfo': visitorInfo,
        'homeInfo': homeInfo,
        'gameInfo': gameInfo
    }
