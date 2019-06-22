
# define imports
import os
from os.path import getsize
from os import walk
import glob

# change working directory
os.chdir(r"C:\Users\benja\Source\Repos\sandbox")
path = os.getcwd()
# announce start
print(' -------------- Starting --------------')
print(path)
print(' -------------- Starting --------------')

# Start scraping

for (dirpath,dirnames,filenames) in walk(path):

    size = sum(getsize(name) for name in files)
    count += len(files)
    kb = size / 1000
    print(dirnames,count,kb )





# folders = [x[0] for x in os.walk(os.getcwd())]
# print (folders)


# current_dir = os.getcwd() + '\\test.csv'
# print (current_dir)

#Fields = ['Folder','File_Count','Folder_Count']





# for path, dirs, files in os.walk(start_path):
#    for f in files:
#       fp = os.path.join(path, f)


# with open(current_dir, 'w', newline='\n', ) as csvfile:
#    csvwriter = csv.writer(csvfile)
#
#    csvwriter.writerows([Fields])
#    csvwriter.writerows([folders])
