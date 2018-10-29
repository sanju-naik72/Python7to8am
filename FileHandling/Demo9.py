f = open("two.txt","w")
st = input("Enter Some text to file : ")
f.write(st) # Writing to file
f.close() # save and close
print("File Created and text written to it")