import calendar
from datetime import date
import datetime
import math
import sys

from IPython.utils.timing import timing
from pymongo import MongoClient
import pymongo


print(sys.version)
print(sys.version_info)

print(datetime.datetime.now())

print(math.pi)

values = "aaa,bbb,ccc"
print(tuple(values.split(",")))
print(calendar.month(2016,4))

date1 = date(2016,4,1)
date2 = date(2016,4,5)
delta = date2 - date1
print(delta.days)

val = "IsArray"
if(val.startswith("Is")):
    print(val)
else:
    print("gIs"+val)

client = MongoClient()
db = client.test

cursor = db.restaurants.aggregate([
   {"$match":{"borough":"Queens"}},
   {"$group":{"_id":"$borough","count":{"$sum":1}}}
])
for document in cursor:
    print(document)
# db.restaurants.create_index([("cuisine", pymongo.ASCENDING)])
cursor = db.restaurants.find({"name":"Jackyu"}, {"name":1,"_id":0}).limit(5)
for document in cursor:
    print(document)
print(db.serverStatus)
print("----------------------------")
cursor = db.restaurants.find().limit(5)
for document in cursor:
    print(document)

# db.createCollection( "contacts",
#    { "validator": { "$or":
#       [
#          { "phone": { "$type": "string" } },
#          { "email": { "$regex": "/@mongodb\.com$/" } },
#          { "status": { "$in": [ "Unknown", "Incomplete" ] } }
#       ]
#    }
# } )

import redis
redis = redis.Redis(host='localhost', port=6379, db=0, password='1')
a = redis.smembers('circle:jdoe:soccer')
print(a)
redis.sadd('circle:jdoe:soccer', 'users:fred')
a = redis.smembers('circle:jdoe:soccer')
print(a)


