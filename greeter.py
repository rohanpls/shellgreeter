from random import choice

ricebowl = """
                   ░
               ░  ░
              ░  ░
             ░    ░[30m     [33m▄▀ ▄▀[37m
              ░       [33m▄▀ ▄▀[37m
              [0;1m▄▄█[0;1;30;47m\[0;1m█▄[0;33m▄▀[37m [33m▄▀[37m
         [31m__[0;37m▄[0;1;30;47m`/[0;1m█[0;1;30;47m/`[0;1m██[0;1;30;47m`[0;1m█[0;33;47m▄▀[0;31m__[37m
       [31m▄[0;31;47m▀[0;1;30;47m·`.,[0;1m█[0;1;30;47m.[0;1m██[0;1;30;47m\-[0;1m██[0;1;30;47m/[0;1m█[0;1;30;47m`·[0;31;47m▀[0;31m▄[37m
      [1;31m▐█[0;1;31;47m▄[0;1m██████[0;1;30;47m,,[0;1m████[0;1;33;47mπr8[0;31;47m▄▄[0;31m█▌[37m
      [1;31m▐[37;41m▓[31m▓▓▄▄▄▄▄▄▄▄▄▄▄▄▄▄▒▒░[0;31m▌[37m
      [1;31m▐[37;41m▓[31m▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒░░[0;31m▌[37m
       [1;31m█[37;41m▓[31m▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒░░[0;31m█[37m
       [1;31m▐[37;41m▓▓[31m▓▓▓▓▒▒▒▒▒▒▒▒▒░░░[0;31m▌[37m
        [1;31m▀█[37;41m▓▓[31m▓▓▓▒▒▒▒▒▒▒░░[0;31m█▀[37m
          [1;31m▀██[41m▓▓▒▒▒▒▒▒[40m██[0;31m▀[37m
             [1;31m▀▀▀▀▀▀▀▀[0m

"""



msg = [ "Welcome back! What do you wanna do today?",
        "Someone's in a hurry...",
        "Battling some daemons today, are we?",
        "How do you know if someone uses Arch? \n Don't worry, they'll tell you.",
    ]

humour = [
        "Debugging: because sometimes your computer needs a good talking to.",
        "I'm not arguing, I'm just explaining why I'm right.",
        "A SQL query walks into a bar and sees two tables. He approaches, and asks 'Can I join you?'",
        "Go on, make the computer do something funny.",
        "press y to execute 'rm -rf /*'",
        ]

print(ricebowl, '\n' + choice(msg) + '\n')