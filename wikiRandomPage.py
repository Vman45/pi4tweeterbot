# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
import time 
import socket
import requests
from myconf import *
from datetime import datetime
from twython import Twython
from lxml.html import fromstring

# get time
now = datetime.now()
current_hour = now.strftime("%H")

# get url
r = requests.get('https://it.wikipedia.org/wiki/Speciale:PaginaCasuale') 

# get title
title = fromstring(r.content).findtext('.//title')

# remove "- Wikipedia"
title = title [:-11]

# string creation
tweetStr = "La pagina delle " +  current_hour + ": " + title + "\n\n" + r.url + "\n\n#wiki #random #wikipedia #wikimedia"

# tweet sending
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)
api.update_status(status=tweetStr)

print "\n" + tweetStr

