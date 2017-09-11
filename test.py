from _collections import OrderedDict
import json


a = {
     'a':3,
     'b':2}
b = OrderedDict()
b['a'] = 1
b['b'] = 2

print(min(a.values()))
print(min(a, key=lambda s:a[s]))
print(a.items())

