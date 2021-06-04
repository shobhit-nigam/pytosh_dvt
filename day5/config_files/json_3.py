import json

dictb = {'ww':30, 'rr':40,
         'nested':{20:'tt', 77:'rr'} }

with open("example_3.json", "w") as fj:
    json.dump(dictb, fj)


