import json
import sys
import os

sourceFilePath ='/home/ljurk/.config/powerline/config.json'
setTo =''
data = {}
jsonPath = []
args = sys.argv
args.pop(0)
argCount = len(args)

#open file
with open(sourceFilePath, 'r') as read_file:
    data = json.load(read_file)

for i in range(len(args)):
    if args[i].startswith('-'):
        args[i] = args[i].replace('-','',1)
        jsonPath.insert(i,args[i])
    else:
        setTo = args[i] 

print(sourceFilePath)
print(args)
print('depth: ' + str(argCount))
print()

#show objects under given path
elem=data
for i in range(argCount):
    elem=elem[jsonPath[i]]
for e in elem:
    print(e)

#show all
#elem=data
#for i in range(len
    #backup actual config
    #os.system('cp ' + sourceFilePath + ' ' + sourceFilePath + '.old')
    #change data to input
    #data['ext']['shell']['colorscheme'] = setTo
#    #write to file
#    with open(sourceFilePath, 'w') as write_file:
#        json.dump(data, 
#                write_file,
#                ensure_ascii = False,
#                sort_keys = True,
#                indent = 4 )
#    os.system('powerline-daemon --replace')
