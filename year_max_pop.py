'''
Given a list of people with their birth and end years,
between a specific start year and end year,
find the year with the most number of people alive.
'''
import numpy as np


def year_max_pop(people, start_year, end_year):
    n_years = end_year - start_year + 1
    pops = np.zeros(n_years)
    for birth, death in people:
        assert birth <= death
        idx = [i - 1900 for i in range(birth, death + 1)]
        pops[idx] += 1
    return np.argmax(pops) + 1900


people = [[1900, 1988], [1932, 2000], [1957, 1957],
          [1956, 1999], [1935, 1945], [1920, 1944],
          [1998, 2000]]
assert year_max_pop(people, 1900, 2000) == 1935
