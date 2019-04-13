def init():
    global myList
    file=open("manageRCCapacity/globals.dat","r")
    data=file.read()
    if (data==""):
    	data="{}"
    file.close()
    myList = eval(data)
