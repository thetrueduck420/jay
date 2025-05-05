import difflib as diff
import os
from pathlib import Path;

def ask(text):
    knowledge = os.listdir("./database");
    
    file = diff.get_close_matches(text, knowledge, 1);
    file = str(file).split("'");
    with open ("./database/" + file[1]) as f:
        eval(f.read());

def edit(text, code):
    filename = Path("./database/" + text);
    if filename.exists():
        with open("./database/" + text, "r") as f:
            pass;
    else:
        with open("./database/" + text, "a") as f:
            f.write(code);


            
    
