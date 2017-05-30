#Improving street names
"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "bangalore_india.osm"
street_type_re = re.compile(r'[.,\s]st[.,\s]', re.IGNORECASE)
postcodeinstreetname = re.compile('[,\s]*\d+[,\s]*$')
countryinstreetname = re.compile('[,\s]*india[,\s]*$')
stateinstreetname = re.compile('[,\s]*karnataka[,\s]*$')
cityinstreetname = re.compile('[,\s]*b[a,e]ngal[o,u]r[e,u][,\s]*$')
phonecharacters = re.compile(r'[;/&,.]')
expectedcityname = re.compile('[,\s]*b[a,e]ng(.*?)l[o,u]r[e,u][,\s]*$', re.IGNORECASE)

# UPDATE THIS VARIABLE
mapping = {
            "St.": "Street",
            "St": "Street",
            "Rd.": "Road",
            "Rd" : "Road",
            "Ave": "Avenue",
            "Mn": "Main"
            }


#Checks if the street attriubute exists
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street" or elem.attrib['k'] == "addr:housenumber")

def update_street_name(name):

    #If city/state/country name exists in street name, it removes them
    postcodeinstreet = postcodeinstreetname.search(name)
    if postcodeinstreet:
        name = name[0:postcodeinstreet.start()]
    countryinstreet = countryinstreetname.search(name.lower())
    if countryinstreet:
        name = name[0:countryinstreet.start()]
    stateinstreet = stateinstreetname.search(name.lower())
    if stateinstreet:
        name = name[0:stateinstreet.start()]
    cityinstreet = cityinstreetname.search(name.lower())
    if cityinstreet:
        name = name[0:cityinstreet.start()]
    #Maps abbreviations to the right street names
    for key, value in mapping.iteritems():
        exists = street_type_re.search(name)
        if exists:
            name = re.sub(key,value, name.rstrip())
    return name

#Checks if the city attriubute exists
def is_city(elem):
    return (elem.attrib['k'] == "addr:city")

#Updates the city name by appending or modifying the city name to include 'Bangalore'
def update_city_name(city):
    expected = expectedcityname.search(city)

    if expected:
        city = re.sub(r'[,\s]*b[a,e]ng(.*)l[o,u]r[e,u][,\s]*$', ' Bangalore ', city, flags=re.IGNORECASE)
    else:
        city = city + ', Bangalore'
    return city

#Checks if the postal code attriubute exists
def is_postal_code(elem):
    return (elem.attrib['k'] == "addr:postcode")

#Merges the postal code to produce a standard 6 digit code
def update_postcodes(code):

    code = "".join(code.split(" "))
    if unicode(code).isnumeric and len(code) == 6 and code[0] == '5' and code[1] == '6':
        return code
    else:
        None

#Checks if the phone number attriubute exists
def is_phone(elem):
    return (elem.attrib['k'] == "phone" or elem.attrib['k'] == "mobile_phone"
            or elem.attrib['k'] == "phone_1" or elem.attrib['k'] == "phone_2"
            or elem.attrib['k'] == "phone_3")

#Updates the phone number with the right format
#Country code for India - 91
#Area code for Bangalore - 080 (80)
#Fixed Lines - +91-80-xxxx xxxx
#Mobile/Cell - +91-xxxxxxxxxx
def update_phone(phone):

    phone = phone.strip('.')
    phone = "".join(("".join(phone.split(" "))).split("-"))

    linetype = phone[-10:-8]
    if linetype == '80' or len(phone)<9:
        return '+91-80-'+phone[-8:-4]+' '+phone[-4:]
    else:
        return '+91-'+phone[-10:]

#If there are multiple phone numbers in the same attribute,
#the function below forms a list of phone numbers
#by splitting on certain special characters found in the dataset
#and uodates each phone number in the list
def update_phonenumbers(phone):
    phones=[]
    multiplephones = re.split(phonecharacters,phone)

    for phone in multiplephones:
        if len(phone)>0:
            ph = update_phone(phone)
            phones.append(ph)
        elif len(phone)<8:
            lastnumbers = len(phone)
            ph = phones[len(phones)-1][-16:0-lastnumbers]+phone
            phones.append(ph)
    return ', '.join(phones)
