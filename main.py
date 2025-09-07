import keyboard
import random
import time

game_grid = [
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "]
]
#goal player can shoot and move in any direction but it has to be controlled by the keyboard
#keybinds, movement - wasd, changing shooting direction E to go 90 deg clockwise and Q to go 90 deg anti clockwise, space to shoot

def enemy_spawn(game_grid, e_pos_list):
    spawn_y = random.randint(0,7)
    spawn_x = random.randint(0,7)
    while game_grid[spawn_y][spawn_x] != " ":
        spawn_y, spawn_x = random.randint(0,7), random.randint(0,7)
    e_pos_list.append([spawn_y, spawn_x])

def move_check():
    while True:
        if keyboard.read_key() in ["w", "a", "s", "d", "q", "e", "space"]:
            return keyboard.read_key()
        

def shoot(player_pos, player_dir):
    if player_dir == 12:
        bullet_pos = [player_pos[0] - 1, player_pos[1]]
    if player_dir == 3:
        bullet_pos = [player_pos[0], player_pos[1] + 1]
    elif player_dir == 6:
        bullet_pos = [player_pos[0] + 1, player_pos[1]]
    elif player_dir == 9:
        bullet_pos = [player_pos[0], player_pos[1] - 1]
    return bullet_pos, player_dir

def move_player(player_pos, move, player_dir):
    if move == "w" and player_pos[0] != 0:
        player_pos[0] -= 1
    if move == "s" and player_pos[0] != 7:
        player_pos[0] += 1
    if move == "a" and player_pos[1] != 0:
        player_pos[1] -= 1
    if move == "d" and player_pos[1] != 7:
        player_pos[1] += 1
    if move == "e":
        player_dir = player_dir + 3 if player_dir < 12 else 3
    if move == "q":
        player_dir = player_dir - 3 if player_dir > 3 else 12

    return player_dir


def new_frame(player_pos, player_dir, e_pos_list, game_grid, move):
    game_grid = [
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "]
]
    game_grid[player_pos[0]][player_pos[1]] = "P"

    if move == "space":
        bullet_pos, bullet_dir = shoot(player_pos, player_dir)

        while bullet_pos != []:
            time.sleep(0.2)
            if bullet_pos in e_pos_list:
                e_pos_list.remove(bullet_pos)
            if not bullet_pos[0] > 7 or bullet_pos[0] < 0 or bullet_pos[1] > 7 or bullet_pos[1] < 0:    
                game_grid[bullet_pos[0]][bullet_pos[1]] = "|" if bullet_dir in [12, 6] else "—"
            if bullet_dir == 12:
                bullet_pos = [bullet_pos[0] - 1, bullet_pos[1]]
            if bullet_dir == 6:
                bullet_pos = [bullet_pos[0] + 1, bullet_pos[1]]
            if bullet_dir == 3:
                bullet_pos = [bullet_pos[0], bullet_pos[1] + 1]
            if bullet_dir == 9:
                bullet_pos = [bullet_pos[0], bullet_pos[1] - 1]

            if bullet_pos[0] > 7 or bullet_pos[0] < 0 or bullet_pos[1] > 7 or bullet_pos[1] < 0:
                bullet_pos = []

            print("________________________________________")
            print("                                        ")
            for i in range(8):
                print(game_grid[i])
            print("________________________________________")


    for pos in e_pos_list:
        game_grid[pos[0]][pos[1]] = "E"
            
   
    return game_grid



game_over_text = """
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║██║   ██║██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝╚██████╔╝███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""
    

running = True
player_pos = [7,3]
e_pos_list = []
bullet_pos = []
bullet_dir = 12
player_dir = 12
print("Press W to start")
while running:
    turn = True
    move = None
    
    
    
    
    move = move_check()
    player_dir = move_player(player_pos, move, player_dir)
    print(player_dir)
    enemy_spawn(game_grid, e_pos_list)

    game_grid = new_frame(player_pos, player_dir, e_pos_list, game_grid, move)

    time.sleep(0.1)
    print("________________________________________")
    print("                                        ")
    for i in range(8):
        print(game_grid[i])
    print("________________________________________")

    if player_pos in e_pos_list:
        print(game_over_text)
        running = False
