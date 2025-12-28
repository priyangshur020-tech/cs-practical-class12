# 2.Read a text file line by line and display each word separated by a #.
def Words_Separated():
    f=open("Quotes.txt","r")
    while True:
        line = f.readline()
        if line == '':
            break
        else:
            words=line.split()
            for i in words :
                print(i+'#',end='')
            print()
Words_Separated()
