with open("/home/roger/myPrograms/DEV_SOFT/PYTHON/INTRODUCCION/file.txt","r") as fileRead:
    content=""
    for x in fileRead.readlines():
        content+=x

    with open("/home/roger/myPrograms/DEV_SOFT/PYTHON/INTRODUCCION/file.txt","w") as fileWrite:
        listValue=["This is value A","This is value B","This is value C"]
        fileWrite.write(content+"\n")
        for x in listValue:
            fileWrite.write(x+"\n")
