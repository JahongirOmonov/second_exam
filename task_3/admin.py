# from django.contrib import admin
#
# # Register your models here.
#
#
# def earliest_max_population(logs):
#     # Create a dictionary to store the population count for each year
#     population_count = {}
#
#     # Iterate through each log entry and update the population count for each year
#     for log in logs:
#         birth, death = log
#         for year in range(birth, death):
#             population_count[year] = population_count.get(year, 0) + 1
#
#     # Find the year with the maximum population count
#     max_population = max(population_count.values())
#     earliest_year = float('inf')
#     for year, population in population_count.items():
#         if population == max_population:
#             earliest_year = min(earliest_year, year)
#
#     return earliest_year
#
# # Test cases
# logs1 = [[1993,1999],[2000,2010]]
# logs2 = [[1950,1961],[1960,1971],[1970,1981]]
#
# print(earliest_max_population(logs1))  # Output: 1993
# print(earliest_max_population(logs2))
