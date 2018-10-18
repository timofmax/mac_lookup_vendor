import urllib.request as urllib2
import json
import codecs
import yaml
from time import sleep

'''
time.sleep only for occasion if macvendors API not able to handle
long list of mac-address. Not tested for long lists.
'''
#API base url,you can also use https if you need
url = "http://macvendors.co/api/"


sps = {}
with open('mac_list.txt') as f:
    txt = f.read()
    mac_list = []
    for mac in txt.split('\n'):
        if mac:
            mac_list.append(mac[0:17].strip())
print("Number of MAC's: {}".format(len(mac_list)))
for i in mac_list:
    request = urllib2.Request(url+i, headers={'User-Agent' : "API Browser"})
    response = urllib2.urlopen( request )
#Fix: json object must be str, not 'bytes'
    reader = codecs.getreader("utf-8")
    obj = json.load(reader(response))

#Print company name
    try:
        vendor = (obj['result']['company'])
        mac_addr = i
        sps.setdefault(mac_addr, vendor)
    except KeyError:
        print("{} - Not Defined Vendor".format(i))
        mac_addr = i
        sps.setdefault(i, "Not Defined Vendor")

print("Numbers of MAC's from API is: {}".format(len(sps)))
with open("yaml_mac.txt", "w") as f:
    yaml.dump(sps, f, default_flow_style=False)

