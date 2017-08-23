import glob
import fileinput
import os

fls = []
str2 = "abcd"
str1 = "yaya"
fls = glob.glob("/homes/laksrinivas/practice/*.txt")
print fls

for i in range (0, len(fls)):
    f = open(fls[i],'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace(str1,str2)

    f = open(fls[i],'w')
    f.write(newdata)
    f.close()
