# 4.Remove all the line that contain the character "a" in the file and write to another file.
with open('input.txt','r') as int, open('output.txt','w') as out:
    for line in int:
        if 'a' not in line and 'A' not in line:
            out.write(line)