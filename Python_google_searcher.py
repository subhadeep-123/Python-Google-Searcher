# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 21:03:33 2018

@author: Subhadeep
"""

import requests
import sys
import bs4
import webbrowser
res=requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")
linkElements=soup.select('.r a')
linkToOpen=min(5, len(linkElements))
for i in range(linkToOpen):
    webbrowser.open('https://google.com'+linkElements[i].get('href'))