import json
import sys
import os

sourceFilePath ='/home/ljurk/.config/powerline/config.json'
setTo =''
data = {}
args = sys.argv
args.pop(0)
foundString=''
recursive =0

#show recursive
def formatData(t,s):
    if not isinstance(t,dict) and not isinstance(t,list):
        print("- "*s+str(t) + ' *e*')
    else:
        for key in t:
            print("- "*s+str(key))
            if not isinstance(t,list):
                formatData(t[key],s+1)

#open file
with open(sourceFilePath, 'r') as read_file:
    data = json.load(read_file)

#parse arguments 
for i in range(len(args)):
    if args[i].startswith('--'):
        if args[i] == '--r':
            recursive = 1
            args.pop(i)
    elif args[i].startswith('-'):
        args[i] = args[i].replace('-','',1)
    else:
        setTo = args[i]
        args.pop(i)

print(sourceFilePath)
print(args)
print('depth: ' + str(len(args)))
print()

#show objects under given path
elem=data
for i in range(len(args)):
    elem=elem[args[i]]

if recursive:
    #recursive
    formatData(elem,0)
else:
    #only actual level
    for e in elem:
        print(e)

if foundString:
    print(elem + ' *e*')
    if setTo != '':
        #change data to input
        if len(args) == 3:
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
