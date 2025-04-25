import pyfs.pyfs as pyfs

data = [];
while(True):
    user_input = input("prompt: ")
    if (user_input == "exit"):
        break;
    else:
        if user_input in pyfs.fs:
            print(pyfs.readFile(user_input));
        else:
            pyfs.addFile(user_input, input("what should i say?: "))

            
    
