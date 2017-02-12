a={}
#a[1022.23]={}
#a[1022.22]={"jack":{"Lontong":{111:"N"}}}
#print a[1022.22]['jack']['Lontong'][111]
prefix = 'global.aim3'
source = "aimMy Bot 1.csv"
destination = "bot1.txt"
txttmp=""
with open(source, 'r') as src:
    with open(destination, 'w') as dest:
        for line in src:
            txt=line.rstrip()
            txt=txt.split('|')
            for i in range(len(txt)):
                if(i==0):
                    if (not(txt[i] in a.keys())):
                        a[txt[i]]={}
                elif(i==1):
                    if (not(txt[i] in a[txt[i-1]].keys())):
                        a[txt[i-1]][txt[i]]={}
                elif(i==2):
                    if (not(txt[i] in a[txt[i-2]][txt[i-1]].keys())):
                        a[txt[i-2]][txt[i-1]][txt[i]]={}
                elif(i==3):
                    if (not(txt[i] in a[txt[i-3]][txt[i-2]][txt[i-1]].keys())):
                        a[txt[i-3]][txt[i-2]][txt[i-1]][txt[i]]=[]
                elif(i==4):
                    a[txt[i-4]][txt[i-3]][txt[i-2]][txt[i-1]].append([txt[i]])
                elif(i==5):
                    a[txt[i-5]][txt[i-4]][txt[i-3]][txt[i-2]][len(a[txt[i-5]][txt[i-4]][txt[i-3]][txt[i-2]])-1].append(txt[i])
                elif(i==6):
                    a[txt[i-6]][txt[i-5]][txt[i-4]][txt[i-3]][len(a[txt[i-6]][txt[i-5]][txt[i-4]][txt[i-3]])-1].append(txt[i])
c=[]
for x in a.keys():
    txttmp+="ds_map_add(aimdata,"+str(x)+",ds_map_create());\n"
    txttmp+="tmppx=ds_map_find_value(aimdata,"+str(x)+");\n"
    for y in a[x].keys():
        txttmp+="ds_map_add(tmppx,"+str(y)+",ds_map_create());\n"
        txttmp+="tmppy=ds_map_find_value(tmppx,"+str(y)+");\n"
        for ex in a[x][y].keys():
            txttmp+="ds_map_add(tmppy,"+str(ex)+",ds_map_create());\n"
            txttmp+="tmppex=ds_map_find_value(tmppy,"+str(ex)+");\n"
            for ey in a[x][y][ex]:
                txttmp+="ds_map_add(tmppex,"+str(ey)+",ds_map_create());\n"
                txttmp+="tmppey=ds_map_find_value(tmppex,"+str(ey)+");\n"
                for i in a[x][y][ex][ey]:
                    txttmp+="ds_list_add(tmppey,ds_list_create());\n"
                    txttmp+="tmppr=ds_list_find_value(tmppey,ds_list_size(tmppey)-1);\n"
                    for j in range(len(i)):
                        if j==1:
                            txttmp+="ds_list_add(tmppr,'"+str(i[j])+"');\n"
                        else:
                            txttmp+="ds_list_add(tmppr,"+str(i[j])+");\n"
print txttmp
#print a
