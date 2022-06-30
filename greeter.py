import random

with open("ricebowl.txt", 'r') as ricebowl:
    print(ricebowl.read())

msg = ( "Welcome back! What do you wanna do today?",
        "Ooooooo someone's in a hurry...",
        "Battling some daemons today, are we?",
        "How do you know if someone uses Arch? \n Don't worry, they'll tell you.",
    )

print(random.choice(msg) + '\n')