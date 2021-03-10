import os
from bubble_sort import bubble

file_path = os.getcwd()

with open(os.path.join(file_path, '1.txt')) as f:
    file_name = os.path.basename(f.name)
    file1 = [file_name, f.read().split('\n')]

with open(os.path.join(file_path, '2.txt')) as f:
    file_name = os.path.basename(f.name)
    file2 = [file_name, f.read().split('\n')]

with open(os.path.join(file_path, '3.txt')) as f:
    file_name = os.path.basename(f.name)
    file3 = [file_name, f.read().split('\n')]

files_list = bubble(file1, file2, file3)

with open(os.path.join(file_path, 'End_files.txt'), 'a') as nf:
    for file in files_list:
        nf.write(file[0] + '\n')
        nf.write(str(len(file[1]))+'\n')
        nf.write('\n'.join(file[1]) + '\n')