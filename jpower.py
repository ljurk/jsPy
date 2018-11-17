import json
import sys
import os

sourceFilePath ='/home/ljurk/.config/powerline/config.json'
setTo =''
data = {}
args = sys.argv
args.pop(0)
foundString=''

#open file
with open(sourceFilePath, 'r') as read_file:
    data = json.load(read_file)

for i in range(len(args)):
    if args[i].startswith('-'):
        args[i] = args[i].replace('-','',1)
    else:
        setTo = args[i]
        args.pop(i)

argCount = len(args)
print(sourceFilePath)
print(args)
print('depth: ' + str(argCount))
print()

#show objects under given path
elem=data
for i in range(argCount):
    elem=elem[args[i]]

for e in elem:
    if len(e) == 1:
        foundString = True
    else:
        print(e)

if foundString:
    print(elem)
    if setTo != '':
        #change data to input
        if argCount == 3:
            print('change ' + data[args[0]][args[1]][args[2]] + ' to ' + setTo)
            #backup actual config
            os.system('cp ' + sourceFilePath + ' ' + sourceFilePath + '.old')
            data[args[0]][args[1]][args[2]] = setTo
            #write to file
            with open(sourceFilePath, 'w') as write_file:
                json.dump(data, 
                        write_file,
                        ensure_ascii = False,
                        sort_keys = True,
                        indent = 4 )
            os.system('powerline-daemon --replace')
