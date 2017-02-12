prefix = 'global.aim3'
source = "aimMy Bot 1.csv"
destination = "bot1.txt"

with open(source, 'r') as src:
    with open(destination, 'w') as dest:
        for line in src:
            dest.write('ds_list_add('+prefix+',"'+line.rstrip()+'");\n')
