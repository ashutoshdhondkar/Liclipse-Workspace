import json
d = {'101': 'DEXTER',
     '102': 'Marks',
     '103':'SIES'}
jsonStr = json.dumps(d)

print(jsonStr)
'''
l = [1,2,3,"hello","Apple"]

jsonL = json.dumps(l)

print(jsonL)
'''

nD = json.loads(jsonStr)
print(nD['102'])