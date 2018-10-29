
import os.path as pa

fname = input("File Name with ext : ")
bo = pa.exists(fname)
if bo:
    print(open(fname).read())
else:
    print("File not Available")


