GOAL_BY_GAME = {
  "bandit": {
    1: 'The password for the next level is stored in a file called "readme" located in the home directory. Use this password to log into bandit1 using SSH.',
    2: 'The password for the next level is stored in a file called "-" located in the home directory',
    3: 'The password for the next level is stored in a file called "spaces in this filename" located in the home directory',
    4: 'The password for the next level is stored in a hidden file in the "inhere" directory.',
    5: 'The password for the next level is stored in the only human-readable file in the "inhere" directory. Tip: if your terminal is messed up, try the “reset” command.',
    6: 'The password for the next level is stored in a file somewhere under the "inhere" directory and has all of the following properties: human-readable, 1033 bytes in size, not executable',
    7: 'The password for the next level is stored somewhere on the server and has all of the following properties: owned by user bandit7, owned by group bandit6, 33 bytes in size',
    8: 'The password for the next level is stored in the file "data.txt" next to the word "millionth"',
    9: 'The password for the next level is stored in the file "data.txt" and is the only line of text that occurs only once',
    10: 'The password for the next level is stored in the file "data.txt" in one of the few human-readable strings, preceded by several ‘=’ characters.',
    11: 'The password for the next level is stored in the file "data.txt", which contains base64 encoded data',
    12: 'The password for the next level is stored in the file "data.txt", where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions',
    13: 'The password for the next level is stored in the file "data.txt", which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)',
  },
  "leviathan": "This doesn't require any knowledge about programming - just a bit of common sense and some knowledge about basic Inix commands.",
    
}
END_LEVEL_BY_GAME = {
  "bandit": 13,
  "leviathan": 7,
}
PSW_BY_GAME = {
  "bandit": {
    0: "bandit0",
    1: "NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL",
    2: "rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi",
    3: "aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG",
    4: "2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe",
    5: "lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR",
    6: "P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU",
    7: "z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S",
    8: "TESKZC0XvTetK0S9xNwm25STk5iWrBvP",
    9: "EN632PlfYiZbn3PhVK3XOGSlNInNE00t",
    10: "G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s",
    11: "6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM",
    12: "JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv",
    13: "wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw",
  },
  "leviathan":{
    0: "leviathan0",
  },
}
PORT_BY_GAME = {
  "bandit": 2220,
  "leviathan": 2223,
}