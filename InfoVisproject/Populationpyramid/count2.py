import csv

# Create dictionary to hold the data
valDic = {}

years, genders,relation = set(), set(), set()

# Read data into dictionary
with open('newData.csv', 'r',) as inputfile:

    reader = csv.reader(inputfile, delimiter = ',')
    next(reader)

    for row in reader:

        key = (row[0], row[2], row[14])

        years.add(key[0])
        genders.add(key[1])
        relation.add(key[2])
        

        if key not in valDic:
            valDic[key]=0

        valDic[key]+=1


#Add missing combinations
for y in years:
    for g in genders:
            for r in relation:
                key = (y, g, r)
                if key not in valDic:
                    valDic[key]=0

#Prepare new CSV
newcsvfile = [["year", "gender","relation","population"]] 

for key, val in sorted(valDic.items()):
    newcsvfile.append([key[0], key[1], key[2], valDic[key]])

with open('results5.csv', "w", newline='') as outputfile:
    writer = csv.writer(outputfile)
    writer.writerows(newcsvfile)  
		