import os
import panda
from os import walk
# from os.path import join, getsize
from os import walk
from os.path import join, getsize
path = os.getcwd()
os.chdir(r"C:\Users\benja\Source\Repos\sandbox")


dataframe = panda.dataframe(columns=['row', 'path', 'folder_name', 'folder_size', 'tree_size', 'total_tree_size', 'last_edit_time', 'created_time', 'tree_file_count', 'tree_folder_count'])

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


print(' -------------- imports done --------------')

current_target = os.walk(os.getcwd())

print(' -------------- set directory --------------')
list_folders = []
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    list_folders.append(root)

    row = 0
for folder in list_folders:
    row += 1
    dataframe_row = []
    folder_size = 0
    tree_size = 0
    total_tree_size = 0
    last_edit_time = 0
    created_time = 0
    tree_file_count = 0
    tree_folder_count = 0
    tree_folder_count = sum([len(dirs) for r, d, files in os.walk(folder)])
    tree_file_count = sum([len(files) for r, d, files in os.walk(folder)])
    created_time = os.path.getctime(folder)
    last_edit_time = os.path.getmtime(folder)
    print("Folder:", folder)
    folder_size = getsize(folder)
    tree_size = get_size(start_path=folder)
    total_tree_size = folder_size + tree_size
    print("folder size:", folder_size, "sub_tree size:", tree_size, "tree size:", total_tree_size, "file count:", tree_file_count, "folder count:", tree_folder_count)
    print("folder last edit:", last_edit_time, "Folder Created:", created_time)
    dataframe_row= ({'row' : row, 'path' : folder , 'folder_size' : folder_size, 'tree_size' : tree_size , 'total_tree_size' : total_tree_size , 'last_edit_time' : last_edit_time , 'created_time' : created_time, 'tree_file_count' : tree_file_count, 'tree_folder_count' : tree_folder_count})
    dataframe_row
    print(' ----------------------------')


print(root)


