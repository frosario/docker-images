#!/usr/bin/env python

### Redis example ###################################################

import redis
r = redis.Redis('192.168.1.3')
r.set("my_example","works!")
r.get("my_example")

# >>> r.get("my_example")
# 'works!'


### Mongodb example #################################################

from pymongo import MongoClient
connection = MongoClient("mongodb://192.168.1.3")
db = connection.demo
db.test.insert({'this':'works'})
docs = db.test.find()

for d in docs:
  print d

# {u'this': u'works', u'_id': ObjectId('58483177ae88f90023ce88f5')}


### Dyanically provision neuron ######################################

import marshal,types

def say_hello():
  print "ohai there"

#Pickle code logic and store in redis
pickle_string = marshal.dumps(say_hello.func_code)
r.set('neuron_code',pickle_string)

#On a neuron set its function
retrieved_code = r.get('neuron_code')
retrieved_code = marshal.loads(retrieved_code)
neural_function = types.FunctionType(retrieved_code,globals())

# >>> neural_function()
# Ohai there


#####################################################################
