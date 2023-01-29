# Script installer Init
# Script by @rohanpls

gen = [ "Welcome back! What do you wanna do today?",
        "Someone's in a hurry...",
        "Battling some daemons today, are we?"
    ]

hum = [
        "Debugging: because sometimes your computer needs a good talking to.",
        "I'm not arguing, I'm just explaining why I'm right.",
        "A SQL query walks into a bar and sees two tables. He approaches, and asks 'Can I join you?'",
        "Go on, make the computer do something funny.",
        "press y to execute 'rm -rf /*'",
        ]

def choiceFunc():
    c = 0
    while c not in (1,2):
        c = int(input("1. Generic prompts\n2. Humor prompts\n\nEnter choice: "))
        if c not in (1,2):
            print('\nInvalid choice. Please select an option from the list: ')
    return c

print("Select the prompts you want: ")
choice = choiceFunc()
f = open('ricebowl.py', 'a')
if choice == 1:
        chosen = gen
elif choice == 2:
        chosen = hum
        
print(f"\nprompt = {chosen}\n")
f.write(f"\nprompt = {chosen}\n")
p = "print(ricebowl+n+prompt+n)"
print(f"{p}")
f.write((f"{p}"))