import math
import os
from os.path import dirname
import random
import sys

import_path = dirname(os.getcwd())
sys.path.append(import_path)
import namesfi

map_table = {
    'å': 'a',
    'ä': 'a',
    'ö': 'o'
}

company_domain = [
    'h20.io', 'supermessage.com',
    'designshop.ie', 'framemusic.info',
    'chatme.io', 'sixfigures.com',
    'researchpart.co', 'snowcat.com'
]

def map_scands(name):
    s = ''
    for ch in name:
        if ch in map_table:
            ch = map_table[ch]
        s += ch
    return s

def generate_email(first_name, last_name):
    email = map_scands(first_name.lower()[:3] + last_name.lower())
    k = math.floor(random.uniform(0, len(company_domain)))
    email += '@' + company_domain[k]
    return email


def main():
    random.seed()
    n = (int(sys.argv[1]) if len(sys.argv) > 1 else 20)

    for i in range(n):
        first_name = namesfi.get_first_name()
        last_name = namesfi.get_last_name()
        email = generate_email(first_name, last_name)
        row = '{0},{1},{2}'.format(first_name, last_name, email)
        print(row)

if __name__ == '__main__':
    main()
