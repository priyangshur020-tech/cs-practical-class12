# 3.Read a text file and display the number of vowels/consonents/uppercase/lowercase characters in the file.
def CountVCUL():
    f=open("Report.txt","r")
    V=C=U=L=0
    data=f.read()
    for i in data:
        if i.isalpha():
            if i.isupper():
                U+=1
            if i.islower():
                L+=1
            if i.lower() in 'aeiou':
                V+=1
            else:
                C+=1
    print("Vowels= ",V)
    print("consonents= ",C)
    print("Uppercase= ",U)
    print("Lowercase= ",L)
CountVCUL()     