prefix = '111'
suffix = '222'

prefix = 'aim1['
idx=1;
suffix=']="'
lines=0
with open('source.txt', 'r') as src:
    with open('dest.txt', 'w') as dest:
       for line in src:
	   lines+=1
       dest.write(prefix+'0]='+str(lines)+';\n')
with open('source.txt', 'r') as src:
    with open('dest.txt', 'a') as dest:
       for line in src:
           dest.write(prefix+str(idx)+suffix+line.rstrip()+'";\n')
	   idx+=1