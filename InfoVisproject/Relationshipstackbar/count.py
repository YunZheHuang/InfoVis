import csv

# Create dictionary to hold the data
valDic = {}

years, genders, age, relations = set(), set(), set(), set()

# Read data into dictionary
with open('newData.csv', 'r',) as inputfile:

    reader = csv.reader(inputfile, delimiter = ',')
    next(reader)

    for row in reader:

        key = (row[0], row[1], row[2])

        years.add(key[0])
        genders.add(key[1])
        age.add(key[2])
        

        if key not in valDic:
            valDic[key]=0

        valDic[key]+=1
           if row[3] == "Family/Relative;Other"


#Prepare new CSV
newcsvfile = [["year", "gender", "age", "country", "population"]] 

for key, val in sorted(valDic.items()):
    newcsvfile.append([key[0], key[1], key[2], key[3], valDic[key]])

with open('results.csv', "w", newline='') as outputfile:
    writer = csv.writer(outputfile)
    writer.writerows(newcsvfile)  
		