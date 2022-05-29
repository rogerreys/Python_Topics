ruta = "./"

# Write
values = ["First Line A\n", "Second Line B\n", "Third Line C\n"]
with open(ruta+"file.txt","w") as fileWrite:
    for i in values:
        fileWrite.write(i)

# Append
with open(ruta+"file.txt","a") as fileAppend:
    print("Value {}".format(fileAppend.tell())) 
    fileAppend.seek(0,0)
    fileAppend.write("Line append")

# Copy File
with open(ruta+"file.txt","r") as fileReadable:
    with open(ruta+"file2.txt","w") as fileCopied:
        for i in fileReadable:
            fileCopied.write(i)

# Additional modes  
#    r+ : Reading and writing. Cannot truncate the file.
#    w+ : Writing and reading. Truncates the file.
#         opening a file in w+ overwrites it and deletes all pre-existing data
#    a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab.

#    To work with a file on existing data, use r+ and a+

#    .tell() - returns the current position in bytes
#    .seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to beginning, relative to current position and end
with open(ruta+"file2.txt","a+") as fileAppendPlus:
    fileAppendPlus.seek(0,0)
    fileAppendPlus.write("Line to appending at the end")
    fileAppendPlus.seek(0,0)
    print(fileAppendPlus.read())