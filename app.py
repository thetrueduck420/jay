import pfs.pyfs as pyfs

def edit():
    print("edit mode, say 'user' to go to user mode");
    while (True):
        edit_input = input("edit: ");
        if (edit_input == "user"):
            break;

        print("what should i evaluate: ")
        code = input("code: ");
        pyfs.addFile(edit_input, code);

def user():
    user_input = input("prompt: ");
    if (user_input == "exit"):
        exit();
    if (user_input == "edit"):
        edit();
    if (user_input in pyfs.fs):
        eval(pyfs.readFile(user_input));

print("default to user mode, say 'edit' to edit things");
while(True):
    user();

            
    
