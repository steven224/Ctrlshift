# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 23:06:23 2019

@author: sfsong
"""

import requests
url = 'http://localhost:5000/api'
X_test=[[1.4022, 4, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,0, 0, 1, 0]]
r = requests.post(url,json={'X_test':[[1.4022, 4, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,0, 0, 1, 0]]})
print(r.json())
