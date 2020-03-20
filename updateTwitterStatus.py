#!/usr/bin/env python
import sys
import time 
import socket
from myconf import *

from twython import Twython

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

time.sleep(300)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
 
tweetStr = host_name + ' - ' + get_ip()
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)
api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr

