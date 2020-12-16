import sys

glass = []
for i in sys.stdin:
    j = i.split()
    glass.append([j[0], int(j[1])])
color = [
    "\033[30m\033[48;2;230;232;237m⬜︎\033[0m",
    "\033[30m\033[48;2;140;231;152m⬜︎\033[0m",
    "\033[30m\033[48;2;57;187;81m⬜︎\033[0m",
    "\033[30m\033[48;2;40;146;60m⬜︎\033[0m",
    "\033[30m\033[48;2;26;90;41m⬜︎\033[0m"
]
height = 7
width = len(glass)/7 if len(glass) % 7 == 0 else len(glass)//7+1
for i in range(height):
    for j in range(width):
        if len(glass) > i+j*7:
            print(color[glass[i+j*7][1]], end='')
    print("")
