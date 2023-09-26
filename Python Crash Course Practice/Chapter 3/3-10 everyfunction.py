#This is practice for using some of the previous discussed functions in this chapter
cities = ['idaho falls', 'louisville', 'hemet', 'new york', 'phoenix']
cities.append('nashville')
cities.sort(reverse=True) 
del cities[0]
print(cities)