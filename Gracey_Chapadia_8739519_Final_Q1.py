beforeFile = open (PROG1783File1Before.txt','r'')
afterFile = open (PROG1783File1After.txt','a'')

flag = False

for line in beforeFile.readlines(1):
    
    if 'Gracey Chapadia 8739519' in line :
        flag = True
    
    if flag:
        chars = line.split()
        chars[100]
        afterFile.write(str(chars))

beforeFile.close()
afterFile.close()


