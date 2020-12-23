# w # use to create new file and overwrite in the file
# a # use to append the text and also create new file 
# r+ # use to read and also to write text from strat and overwrite the text in the file does not create new file

with open('file.txt','r+') as f:
    f.seek(len(f.read()))
    f.write("please do it")    