from os.path import abspath, join, dirname
import math
import random

random.seed()

full_path = lambda filename: abspath(join(dirname(__file__), filename))

FILES = { 
    'first:female': full_path('dist.female.first'),
    'first:male': full_path('dist.male.first'),
    'last': full_path('dist.all.last')
}

def get_name(filename):
    with open(filename) as f:
        n = int(f.readline())
        selected = math.floor(random.uniform(0, n))
        line_num = 0
        for name in f:
            if line_num == selected:
                return name.rstrip()
            line_num += 1
    return ""


def get_first_name(gender=None):
    if gender is None:
        gender = random.choice(('female', 'male'))
    if gender not in ('female', 'male'):
        raise ValueError("Value not 'female' or 'male'")
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return '{0} {1}'.format(get_first_name(gender), get_last_name()) 


def main():
    for i in range(100):
        print(get_full_name())

if __name__ == '__main__':
    main()
