import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 3600

# The maximum rent you want to pay per month.
MAX_PRICE = 6200

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'sfbay'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
#AREAS = ["eby", "sfc", "sby", "nby"]
AREAS = ['sfc']

#The minimum number of bedrooms in a result
BEDROOMS = 2

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {                        
    "nopa": [                    
        [37.771885, -122.458935],
        [37.783486, -122.437348],
    ],                           
    "castro_market": [           
        [37.746914, -122.444944],
        [37.770223, -122.403188],
    ],                           
    "colevalley_ashburyhts": [   
        [37.7594, -122.455373],  
        [37.7703, -122.441769],  
    ],                           
    "pac_heights": [             
        [37.787183, -122.446918],
        [37.798917, -122.422371],
    ],                           
    "lower_pac_heights": [       
        [37.780157, -122.447240],
        [37.789217, -122.429494],
    ],                           
    "haight": [                  
        [37.766389, -122.454118],
        [37.773378, -122.436372],
    ],                           
    "sunset": [                  
        [37.74408, -122.504511], 
        [37.766322, -122.452723],
    ],                           
    "richmond": [                
        [37.771631, -122.489748],
        [37.78029, -122.45121],  
    ],                           
    "noe_valley": [              
        [37.735375, -122.444644],
        [37.751936, -122.424173],
    ],                           
    "potrero_hill": [            
        [37.750443, -122.402372],
        [37.765541, -122.393188],
    ],                           
    "twinpeaks_diamondhts": [    
        [37.745013, -122.465072],
        [37.763065, -122.442026],
    ],                           
    "nob_hill": [                
        [37.789421, -122.424216],
        [37.800544, -122.408595],
    ],                           
    "presidio": [                
        [37.78162, -122.472711], 
        [37.792304, -122.446532],
    ]                            
}                                

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["alamo square / nopa", "dogpatch", "bernal heights", "castro / upper market", "cole valley / ashbury hts", "haight ashbury", "inner richmond", "inner sunset / UCSF", "laurel hts / presidio", "lower haight", "lower nob hill", "lower pac hts", "mission district", "nob hill", "noe valley", "pacific heights", "twin peaks / diamond hts"]
## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 2 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "oakland_19th_bart": [37.8118051,-122.2720873],
    "macarthur_bart": [37.8265657,-122.2686705],
    "rockridge_bart": [37.841286,-122.2566329],
    "downtown_berkeley_bart": [37.8629541,-122.276594],
    "north_berkeley_bart": [37.8713411,-122.2849758]
}

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
