import os
import csv
print ('hello')
folders = [x[0] for x in os.walk(os.getcwd())]
print (folders)
file1 = os.getcwd() + '\\test.csv'
print (file1)
Fields = ['Folder','File_Count','Folder_Count']
size = 0
path = '.'
#for path, dirs, files in os.walk(start_path):
#    for f in files:
#       fp = os.path.join(path, f)


with open(file1, 'w', newline='', ) as csvfile:
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerows([Fields])
    csvwriter.writerows([folders])
