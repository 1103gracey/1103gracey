# This program is performed by gracey chaapdia 8739519.
# THis program will demonstarte the text copied from one file to other file with definite 100 charaters.
# defining the folders
beforeFile = open (PROG1783File1Before.txt','r'')
afterFile = _open (PROG1783File1After.txt','a'')

flag = False

#creating a loop
for line in beforeFile.readlines(1):

#stating conditions for loop
    if 'Gracey Chapadia 8739519' in line :
        flag = True
    
    if flag:
        chars = line.split()
        chars[100]
        afterFile.write(str(chars))

#closing both folders
beforeFile.close()
afterFile.close()


