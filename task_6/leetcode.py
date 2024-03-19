# 1 - topshiriq

s = "luffy is still joyboy"
def lengthOfLastWord(s):
    counter = 0
    qale = s.rstrip()
    x = len(qale)
    for i in range(x, 0, -1):
        if (ord(qale[i - 1]) >= 65 and ord(qale[i - 1]) <= 90) or (ord(qale[i - 1]) >= 97 and ord(qale[i - 1]) <= 122):
            counter += 1
        else:
            break
    return counter

print(lengthOfLastWord(s))


# 2 - topshiriq
from collections import defaultdict
# def maximumPopulation(logs):
    # population = defaultdict(int)
    #
    # for birth, death in logs:
    #     for year in range(birth, death):
    #         population[year] += 1
    #
    #
    # max_population = 0
    # earliest_year = 99999999
    # print(population)
    #
    # for year, count in population.items():
    #     # print(year, count)
    #     if count > max_population:
    #         max_population = count
    #         earliest_year = year
    #     elif count == max_population and year < earliest_year:
    #         earliest_year = year
    #
    # return earliest_year

#
# logs = [[1993, 1999], [2000, 2010]]
# print(maximumPopulation(logs))







