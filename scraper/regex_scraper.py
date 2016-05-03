import requests
from lxml import html

import re

tagStripper = re.compile('(<.+?>)+')
whiteSpaceReducer = re.compile('(\s|&nbsp;)+')
headerStripper = re.compile('Play By Play.+--> ')

def stringifyReport(reportURL):
    plainTextReport = headerStripper.sub(
        '',
        whiteSpaceReducer.sub(
            ' ',
            tagStripper.sub('', requests.get(reportURL).content)
        ).strip()
    )
    return plainTextReport
