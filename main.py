import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')


clear()
with open("./sprites/GAME_NAME.txt", 'r') as f:
        print(f.read())


