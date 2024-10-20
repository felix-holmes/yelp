# -*- coding: utf-8 -*-
"""
Author(s): Felix Holmes
Consulted:
Date: 2024-04-25
Purpose: Yelp task: Working with dictionaries and tuples and
    real world data. YELP data set covers different metropolitan areas
    in 4 countries (not including Boston).
"""

#---------#
# Imports #
#---------#

# This will be needed to access JSON loading and storing functions.
import json

#---------------------------#
# Write your functions here #
#---------------------------#

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
    maxstars = 0
    maxreviews = 0
    for business in yelpDict.values():
        if 'Pizza' in business['categories']:
            stars = business['stars']
            reviews = business['review_count']
            if stars > maxstars or (stars == maxstars and reviews > maxreviews):
                maxstars = stars
                maxreviews = reviews
                best = [business]
            elif stars == maxstars and reviews == maxreviews:
                best.append(business)
    return best

#--------------#
# Testing data #
#--------------#

soloYelp = {
  "XguKrY0dAuaK1W6HUlUQ1Q": {"state": "OH", "address": "547 Sackett Ave", "review_count": 29, "stars": 3.5, "name": "Retz's Laconi's II", "city": "Cuyahoga Falls", "categories": ["Italian", "Restaurants", "Pizza"]}
}

microYelp = {
  "PMH4oUa-bWELKogdtkWewg": {'state': 'ON', 'address': '100 City Centre Dr', 'review_count': 16, 'stars': 2.0, 'name': 'GoodLife Fitness', 'city': 'Mississauga', 'categories': ['Fitness & Instruction', 'Sports Clubs', 'Gyms', 'Trainers', 'Active Life']},
  "XguKrY0dAuaK1W6HUlUQ1Q": {'state': 'OH', 'address': '547 Sackett Ave', 'review_count': 29, 'stars': 3.5, 'name': "Retz's Laconi's II", 'city': 'Cuyahoga Falls', 'categories': ['Italian', 'Restaurants', 'Pizza']},
  "Wpt0sFHcPtV5MO9He7yMKQ": {'state': 'NV', 'address': '3020 E Desert Inn Rd', 'review_count': 20, 'stars': 2.0, 'name': "McDonald's", 'city': 'Las Vegas', 'categories': ['Restaurants', 'Fast Food', 'Burgers']},
  "1K4qrnfyzKzGgJPBEcJaNQ": {'state': 'ON', 'address': '1058 Gerrard Street E', 'review_count': 39, 'stars': 3.5, 'name': 'Chula Taberna Mexicana', 'city': 'Toronto', 'categories': ['Tiki Bars', 'Nightlife', 'Mexican', 'Restaurants', 'Bars']},
  "7gquCdaFoHZCcLYDttpHtw": {'state': 'SC', 'address': '8439 Charlotte Hwy', 'review_count': 17, 'stars': 4.0, 'name': 'Bubbly Nails', 'city': 'Fort Mill', 'categories': ['Nail Salons', 'Beauty & Spas']},
  "Mmh4w2g2bSAkdSAFd_MH_g": {'state': 'SC', 'address': '845 Stockbridge Dr', 'review_count': 77, 'stars': 3.0, 'name': 'Red Bowl', 'city': 'Fort Mill', 'categories': ['Restaurants', 'Asian Fusion']},
  "vMO2vNyWLuxumso7t3rbYw": {'state': 'ON', 'address': '300 Borough Drive', 'review_count': 5, 'stars': 4.0, 'name': "Pablo's Grill It Up", 'city': 'Scarborough', 'categories': ['Food Court', 'Restaurants', 'Barbeque']},
  "h2XsV6mR6c7QURhlsi0RqA": {'state': 'AZ', 'address': '211 E 10th Dr, Ste 2', 'review_count': 26, 'stars': 4.5, 'name': "John's Refrigeration Heating and Cooling", 'city': 'Mesa', 'categories': ['Home Services', 'Air Duct Cleaning', 'Local Services', 'Heating & Air Conditioning/HVAC']},
  "c6Q3HP4cmWZbD9GX8kr4IA": {'state': 'NC', 'address': '4837 N Tryon St', 'review_count': 8, 'stars': 3.5, 'name': 'Pep Boys', 'city': 'Charlotte', 'categories': ['Auto Parts & Supplies', 'Auto Repair', 'Tires', 'Automotive']},
  "1EuqKW-JC-Fm3RSWRqKdrg": {'state': 'NV', 'address': '2075 E Warm Springs Rd', 'review_count': 5, 'stars': 5.0, 'name': 'Life Springs Christian Church', 'city': 'Las Vegas', 'categories': ['Religious Organizations', 'Churches']},
  "VZ37HCZVruFm-w_Mkl1aEQ": {'state': 'AZ', 'address': '13637 N Tatum Blvd, Ste 8', 'review_count': 16, 'stars': 5.0, 'name': 'Conservatory of Dance', 'city': 'Phoenix', 'categories': ['Education', 'Dance Schools', 'Arts & Entertainment', 'Fitness & Instruction', 'Specialty Schools', 'Active Life', 'Dance Studios', 'Performing Arts']},
  "htKaC4cHY4wlB4Wqb8CDnQ": {'state': 'PA', 'address': '4730 Liberty Ave', 'review_count': 4, 'stars': 4.0, 'name': 'Allure', 'city': 'Pittsburgh', 'categories': ['Accessories', "Women's Clothing", 'Fashion', 'Shopping']},
  "7fiIMBxbOYdAv3XMcmWivw": {'state': 'OH', 'address': '850 Euclid Ave', 'review_count': 3, 'stars': 3.0, 'name': "Renee's Relaxation and Body Mechanics", 'city': 'Cleveland', 'categories': ['Massage', 'Beauty & Spas']},
  "4SBY4CHiMD8YOCEU9_fdnw": {'state': 'ON', 'address': '123 Queen Street W', 'review_count': 3, 'stars': 4.0, 'name': 'Fidora Salon and Spa', 'city': 'Toronto', 'categories': ['Day Spas', 'Hair Salons', 'Beauty & Spas']},
  "6aFAEeJ3nS-iWGt7Tn7S0Q": {'state': 'NC', 'address': '19925 Jetton Rd, Ste 100', 'review_count': 5, 'stars': 5.0, 'name': 'KS Audio Video', 'city': 'Cornelius', 'categories': ['Home Services', 'Television Service Providers', 'Home Automation', 'Home Theatre Installation', 'Professional Services']},
}
