# Shell Greeter v1.1 - Ricing for your terminal!
# Script by @rohanpls
import ricebowl
import os
import shutil

ddirec = os.path.expanduser("~") + "/shellgreeter"
dfile = "greeter.py"
def check_shell():
    shell = os.environ.get("SHELL")
    if shell.endswith("bash"):
        rc_file = os.path.expanduser("~/.bashrc")
    elif shell.endswith("zsh"):
        rc_file = os.path.expanduser("~/.zshrc")
    elif shell.endswith("fish"):
        rc_file = os.path.expanduser("~/.config/fish/config.fish")
    else:
        rc_file = ""
        print("Unsupported shell. Please manually configure the installation")
    return rc_file

rc_file = check_shell()

def updateRC():
    if rc_file:
        with open(rc_file, 'a') as f:
            f.write("\npython3 ~/shellgreeter/greeter.py\n")
    return "\nInstallation complete! Reload your shell!"

if not os.path.exists(ddirec):
    os.mkdir(ddirec)
       
r = open('ricebowl.py', 'r').read()

def withPrompts():
    gen = [ "Welcome back! What do you wanna do today?",
        "Someone's in a hurry...",
        "Battling some daemons today, are we?"
        ]
    hum = [
        "Debugging: because sometimes your computer needs a good talking to.",
        "I'm not arguing, I'm just explaining why I'm right.",
        "A SQL query walks into a bar and sees two tables. \nHe approaches, and asks 'Can I join you?'",
        "Go on, make the computer do something funny.",
        "press y to execute 'rm -rf /*'",
        ]
    g = open('greeter.py','w')
    def choiceFunc():
        while True:
            c = int(input("1. Generic prompts\n2. Humor prompts\n\nEnter choice: "))
            if c in (1,2):
                return c
            else:
                print('\nInvalid choice. Please select an option from the list: ')

    print("\nSelect the prompts you want: ")
    choice = choiceFunc()
    if choice == 1:
        chosen = gen
    elif choice == 2:
        chosen = hum
    g.write(f"from random import choice\n{r}\nprompt = {chosen}\n")
    p = "print(choice(prompt)+n)"
    g.write((f"{p}"))
    g.close()
    src = "greeter.py"
    shutil.copy(src, os.path.join(ddirec, dfile))
    status = updateRC()
    return status     

def standalone():
    src = "ricebowl.py"
    shutil.copy(src, os.path.join(ddirec, dfile))
    status = updateRC()
    return status

print("Welcome to ShellGreeter!\nPlease choose your choice of installation: ")
while True:
    user_input = int(input("1. Standalone Ricebowl\n2. Ricebowl with Prompts\nEnter your choice: "))
    if user_input == 1:
        print(standalone())
        break
    elif user_input == 2:
        print(withPrompts())
        break
    else:
        print("\nInvalid input. Please try again.\n")
    
