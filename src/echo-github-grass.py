import sys

grass = []
for i in sys.stdin:
    j = i.split()
    grass.append([j[0], int(j[1])])
color = [
    "\033[30m\033[48;2;230;232;237m⬜︎\033[0m",
    "\033[30m\033[48;2;140;231;152m⬜︎\033[0m",
    "\033[30m\033[48;2;57;187;81m⬜︎\033[0m",
    "\033[30m\033[48;2;40;146;60m⬜︎\033[0m",
    "\033[30m\033[48;2;26;90;41m⬜︎\033[0m"
]
height = 7
width = int(len(grass)/7) if len(grass) % 7 == 0 else int(len(grass)//7+1)
for i in range(height):
    for j in range(width):
        if len(grass) > i+j*7:
            print(color[grass[i+j*7][1]], end='')
    print("")
