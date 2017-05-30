#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    tree = ET.ElementTree(file=filename)
    #tree = ET.parse(filename)
    root = tree.getroot()
    #return root.tag, root.attrib
    
    #for child_of_root in root:
    #    return child_of_root.tag,child_of_root.attrib
        
    '''for elem in tree.iter():
        return elem.tag, elem.attrib'''
    
    elemlist=[]
    for elem in tree.iter():
        elemlist.append(elem.tag)
    
    tags = {}
    for tag in elemlist:
        tags.update({tag : elemlist.count(tag)})
    return tags
    
    #for elem in tree.iter(tag='node id'):
    #    print elem.tag, elem.attrib
        
    '''with open(filename, "r") as file:
        lines = file.split()
        for line in lines:
            return line'''


def test():

    tags = count_tags('example.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}

    
count_tags('example.osm')
