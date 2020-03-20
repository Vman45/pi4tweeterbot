#!/usr/bin/env python
import sys
import time 
import socket
import requests
from myconf import *
from datetime import datetime

now = datetime.now()

current_hour = now.strftime("%H")

from twython import Twython

r = requests.get('https://it.wikipedia.org/wiki/Speciale:PaginaCasuale') 
print(r.url) 
 
tweetStr = "La pagina delle " +  current_hour + ": " + r.url + "\n#wiki #random #wikipedia #wikimedia"
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)
api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr

