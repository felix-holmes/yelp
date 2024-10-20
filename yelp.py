import json

def loadData(path):
    """
    Loads contents of file and returns Python object.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return

def getBusinessCount(yelpDict, businessName):
    """
    Returns count of businesses with business name.
    """
    count = 0
    for business in yelpDict:
        if yelpDict[business]['name'].lower() == businessName.lower():
            count += 1
    return count

def uniqueCities(yelpDict):
    """
    Returns list of all cities that appear in Yelp dictionary.
    """
    cities = []
    for business in yelpDict:
        city = yelpDict[business]['city']
        if city not in cities:
            cities.append(city)
    cities.sort()
    return cities

def helper(business):
    """
    Helper!
    """
    return business['stars'], business['name']
    
def findBusinesses(yelpDict, category, city, starLimit, minReview, outFilename):
    """
    Gathers all the businesses in a given city and category that meets minimum
    star limit and minimum number of reviews.
    """
    filtered = []
    for business in yelpDict.values():
        if (category in business['categories']
            and business['city'].lower() == city.lower()
            and business['stars'] >= starLimit
            and business['review_count'] >= minReview):
            filtered.append(business)
    srted = sorted(filtered, key=helper)
    with open(outFilename, 'w', encoding='utf-8') as f:
        json.dump(srted, f)
        
def findCategories(yelpDict, threshold):
    """
    Finds all categories in a Yelp dictionary at or above a given threshold.
    """
    counts = {}
    above = {}
    for business in yelpDict.values():
        for category in business['categories']:
            if category in counts:
                counts[category] += 1
            else:
                counts[category] = 1
    for category, count in counts.items():
        if count >= threshold:
            above[category] = count
    return above

def bestPizzaPlace(yelpDict):
    """
    Finds the best pizza place in Yelp dictionary.
    """
    best = []
    maxStars = 0
    maxReviews = 0
    for business in yelpDict.values():
        if 'Pizza' in business['categories']:
            stars = business['stars']
            reviews = business['review_count']
            if stars > maxStars or (stars == maxStars and reviews > maxReviews):
                maxStars = stars
                maxReviews = reviews
                best = [business]
            elif stars == maxStars and reviews == maxReviews:
                best.append(business)
    return best
