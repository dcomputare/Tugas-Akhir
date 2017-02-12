prefix = '111'
suffix = '222'

prefix = 'global.aim3'
idx=1;
suffix=']="'
lines=0
totalarray=[]
source="aimMy Bot 3.csv"
destination="bot3.txt"
with open(source, 'r') as src:
    with open(destination, 'r') as dest:
       for line in src:
         print "x"
#dest.write('ds_list_add('+prefix+line.rstrip()+'");\n')
