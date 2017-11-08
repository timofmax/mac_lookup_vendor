# Docs https://macvendors.co/api
# Copied from https://gist.github.com/samymassoud/5b041cb759cd321919d4#file-macvendors-py

import urllib.request as urllib2
import json
import codecs
from time import sleep

'''
time.sleep only for occasion if macvendors API not able to handle
long list of mac-address. Not tested for long lists.
'''
#API base url,you can also use https if you need
url = "http://macvendors.co/api/"
#Mac address to lookup vendor from
#This place to write your mac-addresses
#mac addresses separated by ":" or "-" or "." are all accepted

mac_address = '''
00:17:C8:00:00:00          
10:F0:05:00:00:00          
14:36:C6:00:00:00          
20:A2:E4:00:00:00          
3C:15:C2:00:00:00          
50:8F:4C:00:00:00          
58:FB:84:00:00:00          
6C:3B:6B:00:00:00          
6C:3B:6B:00:00:00          
6C:3B:6B:00:00:00          
6C:3B:6B:00:00:00          
6C:72:E7:00:00:00          
74:C6:3B:00:00:00          
74:C6:3B:00:00:00          
7C:B0:C2:00:00:00          
98:9E:63:00:00:00         
A0:CB:FD:00:00:00          
B0:35:9F:00:00:00          
B0:35:9F:00:00:00          
C4:86:E9:00:00:00          
D0:57:7B:00:00:00          
D0:57:7B:00:00:00          
D0:57:7B:00:00:00      
'''

def mac_sps(mac_in_column):
    mac_list = []
    for i in mac_in_column.split('\n'):
        if i:
            mac_list.append(i.strip())
    return mac_list

mac_list = mac_sps(mac_address)


for i in mac_list:
    #sleep(1)
    request = urllib2.Request(url+i, headers={'User-Agent' : "API Browser"}) 
    response = urllib2.urlopen( request )
#Fix: json object must be str, not 'bytes'
    reader = codecs.getreader("utf-8")
    obj = json.load(reader(response))

#Print company name
    print (obj['result']['company']);
    print(i+'\n')
#print company address
#print (obj['result']['address']);

