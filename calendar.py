#!/usr/bin/env python

from eInk import *
from time import sleep
import sys
import json

f = open('config.json', 'r')
c = ujson.loads(f.readall())

print(GoogleAPI)
