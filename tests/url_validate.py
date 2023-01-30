import re
import sys
import os

from typing import (
    Pattern,
    Mapping,
    Match,
    Union
)

import requests
from requests.exceptions import ConnectionError, MissingSchema

URL: Pattern[str] = re.compile(".*\\[.*\\]\\((.*)\\)")

CURRENT_DIR: str = os.path.dirname(os.path.realpath(__file__))

HEADERS: Mapping[str, str] = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

FILE: str = f'{CURRENT_DIR}/../README.md'

with open(FILE) as file:
    
    for line, content in enumerate(file):
    
        match: Union[Match[str], None] = re.match(URL, content)
        if match is None:
            continue
        
        try:
            result = requests.get(match.group(1), headers=HEADERS)
    
            if result.status_code >= 400:
                print(f"{FILE} line #{line} {match.group(1)} return {result.status_code}")
                sys.exit(1)
    
            print(f"{FILE} line #{line} {match.group(1)} pass.")
        
        except ConnectionError:
            print(f"{FILE} line #{line} {match.group(1)} cannot connect.")
        
        except MissingSchema:
            print(f"{FILE} line #{line} {match.group(1)} missing schema.")
