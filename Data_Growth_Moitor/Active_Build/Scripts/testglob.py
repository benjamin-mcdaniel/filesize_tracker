
# define imports
import os
from os.path import getsize
from os import walk
import glob

# change working directory
# os.chdir(r"C:\Users\benja\Source\Repos\sandbox")
# path = os.getcwd()
path = "c:\\"
# announce start
print(' -------------- Starting --------------')
print(path)
print(' -------------- Starting --------------')

# Start scraping
print("------------------------")
for (dirpath,dirnames,filenames) in walk(path):
        size = 0
        count = 0
        count = len(filenames)
        folders = 0
        folders = len(dirnames)
        print(dirpath,"Folders:",folders,"Files:",count)


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
