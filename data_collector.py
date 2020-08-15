# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:23:10 2020

@author: Paras Chaudhary
"""

import glassdoor_scraper as gs
import pandas as pd

path = "E:/Coursera/DS_PROJ/ChrDrv/chromedriver.exe"

df = gs.get_jobs('data scientist', 1000, False, path, 15)

df.to_csv('glassdoor_jobs6.csv', index = False)