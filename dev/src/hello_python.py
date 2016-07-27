import xml.sax
import json
import urllib2
import urlparse

def my_handler(event, context):
    u = urllib2.urlopen(event['datasend'])
    content = u.read();

    return "hello workd"

