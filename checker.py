import csv
#import re

checker_list = []
with open ('/Users/test/pr0x-tube/urls/urls.csv', 'r+') as checker:
    reader = csv.reader(checker, delimiter=' ')
    for row in reader:
        #print(row)
        row.append(checker_list)

if len(set(checker_list)) == len(checker_list):
    print("No duplicates found")

else:
    print("Duplicates found")
