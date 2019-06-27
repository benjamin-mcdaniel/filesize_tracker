import os
from os import walk
# from os.path import join, getsize
from os import walk
from os.path import join, getsize
path = os.getcwd()
os.chdir(r"C:\Users\benja\Source\Repos\sandbox")


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
    print(root)
    for f in list_folders:
        folder_size = 0
        tree_size = 0
        total_tree_size = 0
        print("Folder:", f)
        folder_size = getsize(f)
        tree_size = get_size(start_path=f)
        total_tree_size = folder_size + tree_size
        print("size:", folder_size, "tree size:", total_tree_size)
        print(' ----------------------------')
print(root)


