def write(fname) :
    with open(fname,'w') as file:
        file.write('i love python'.title())




def read(fname):
    with open(fname,'r') as file:
        for line in file:
            print line.strip()