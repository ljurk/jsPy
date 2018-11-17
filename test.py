temp = {'outlook': {'sunny': {'humidity': {'high': [ 'no' ,1 ] , 'normal': 'yes'}}, 'rainy': {'wind': {'strong': 'no', 'weak': 'yes'}}, 'overcast': 'yes'}}

def formatData(t,s):
    if not isinstance(t,dict) and not isinstance(t,list):
        print("-"*s+str(t))
    else:
        for key in t:
            print("-"*s+str(key))
            if not isinstance(t,list):
                formatData(t[key],s+1)

formatData(temp,0)
