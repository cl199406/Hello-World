# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 17:41:41 2018

@author: cl
"""

from pymongo import MongoClient

conn=MongoClient(host='127.0.0.1',port=27017)
db=conn.mydb.test_set
for i in db.find():
    print(i)