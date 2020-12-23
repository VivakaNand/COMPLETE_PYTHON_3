# to find folder inside folder and file inside folder
import os
import shutil
# os.chdir(r'D:\COMPLETE PYTHON-3 COURSE\Chapter-20-OS_MODULE')
# print(os.listdir())
#fileiter = os.walk(r'D:\COMPLETE PYTHON-3 COURSE\Chapter-20-OS_MODULE')
#for current_path, folder_names, file_names, in fileiter:
#    print(f'Current path : {current_path}')
#    print(f'Folder names : {folder_names}')
#    print(f'File names : {file_names}')

# to delete empty folder
# os.rmdir('new')

# create folder inside folder
# os.makedirs('new/files')

# to delete non-empty folders
# shutil.rmtree('new')

# copy folder to other folder
# shutil.copytree('Movies','New/Movies')

# copy a file to folder
# shutil.copy('file.txt','new/file.txt')

# move file to folder
# shutil.move('file.txt','Movies/file2.txt')

# move folder to new folder 
shutil.move('new','Movies/new2')