# DEPRECATED

import requests
from lxml import html

import re

tagStripper = re.compile('(<.+?>)+')
whiteSpaceReducer = re.compile('(\s|&nbsp;)+')
headerStripper = re.compile('Play By Play.+--> ')

# Unlikely to see further use due do relative complicatedness of parsing
# full game reports as single strings vs processing reports with html
# parsing & scraping utilities

def stringifyReport(reportURL):
    plainTextReport = headerStripper.sub(
        '',
        whiteSpaceReducer.sub(
            ' ',
            tagStripper.sub('', requests.get(reportURL).content)
        ).strip()
    )
    return plainTextReport
