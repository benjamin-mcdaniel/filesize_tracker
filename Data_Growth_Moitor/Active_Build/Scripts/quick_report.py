
# define imports
import os
from os.path import join, getsize
import glob
import csv

# indicate its running

print(' -------------- Starting --------------')

# change the working directory so we can test the script against the code dir
os.chdir(r"C:\Users\benja\Source\Repos\sandbox")
print(os.getcwd())
path = os.getcwd()
folder_list = os.walk(".")
size = 0
count = 0
for folder in folder_list:
    for root, dirs, files in os.walk('.'):
        size += sum(getsize(join(root, name)) for name in files)
        count += len(files)
        mb = size/1000
print("folders", count, "files in KB", mb)

from os import walk
path = os.getcwd()
for (dirpath,dirnames,filenames) in walk(path):
    folder_size = 0
    folder_size = sum(getsize(dirpath) for name in folder_list)
    count += len(files)
    kb = size / 1000
    print(dirnames,count,kb )


def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


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
