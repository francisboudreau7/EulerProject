import string 

text_file = open("p022_names.txt", "r")
lines = text_file.read().split(',')
for x in range(len(lines)):
    lines[x]=lines[x].replace('"','')
text_file.close()
lines.sort()

sum=0


for i in range(len(lines)):
    for j in range(len(lines[i])):
        sum+=(string.ascii_uppercase.index(lines[i][j])+1)*(i+1)

print(sum)