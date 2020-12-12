glass = []
for i in range(53*7):
    j = input().split()
    glass.append([j[0], int(j[1])])
color = [
    "\033[30m\033[48;2;230;232;237m⬜︎\033[0m",
    "\033[30m\033[48;2;140;231;152m⬜︎\033[0m",
    "\033[30m\033[48;2;57;187;81m⬜︎\033[0m",
    "\033[30m\033[48;2;40;146;60m⬜︎\033[0m",
    "\033[30m\033[48;2;26;90;41m⬜︎\033[0m"
]
for i in range(7):
    for j in range(53):
        print(color[glass[i+j*7][1]], end='')
    print("")
