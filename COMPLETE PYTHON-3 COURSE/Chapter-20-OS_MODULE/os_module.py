# os module
import os
#os.getcwd # tocheck current working directory
#print(os.getcwd())

# to create a new folder in directory
#os.mkdir('Movies')
#if os.path.exists('movies'):
#    print('Already exists')
#else:
#    os.mkdir('Movies')

# to create file 
#open('file.txt', 'w').close()
#os.mkdir(r'D:\COMPLETE PYTHON-3 COURSE\Chapter-20-OS_MODULE\Movies')

# listdir # list the file and folder in current working directory
#print(os.listdir()) 

# listdir # list the file and folder in 'D:\COMPLETE PYTHON-3 COURSE\Chapter-20-OS_MODULE" directory
#print(os.listdir(r'D:\COMPLETE PYTHON-3 COURSE\Chapter-20-OS_MODULE')) 

# to find path for current working directory
#for item in os.listdir():
#    # this method works for window only
#    #print(r'D:\COMPLETE PYTHON-3 COURSE\Chapter-20-OS_MODULE'+'\\'+item)
#   # this method work for all os
#    path = os.path.join(os.getcwd(),item)
#    print(path)

# to find path for custom directory
for item in os.listdir(r'D:\COMPLETE PYTHON-3 COURSE'):
    path = os.path.join(r'D:\COMPLETE PYTHON-3 COURSE',item)
    print(path)