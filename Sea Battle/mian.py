import pygame
pygame.init()
import random
import time
import modules.Class as m_Class
import modules.function as m_fun
import modules.list as m_list
size_cells = 35
des = False
# отступ слева
left_ind = 70
# отступ свершу
top_ind = 105
start = True
b_hit = False
rotation =  0
explosion = 0
bot_hits = 0
player_hits = 0
bg = pygame.image.load('images/Ocean.png')
cross = pygame.image.load('images/Cross.png')
# Создания окна
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption('Sea Battle')
font = pygame.font.SysFont("Arial", size_cells)
point = pygame.image.load("images/Point.png")
# 
step = [0, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1 ]
step_b = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1 ]
# Вычесления координат 
player_ship_coords = []
bot_ship_coords = []
for row in range(10):
    player_row = []
    bot_row = []
    for col in range(10):
        player_x = left_ind + col * size_cells + 1
        player_y = top_ind + row * size_cells + 1
        player_row.append((player_x, player_y))
        bot_x = 17 * size_cells + col * size_cells + 1
        bot_y = top_ind + row * size_cells + 1
        bot_row.append((bot_x, bot_y))
    player_ship_coords.append(player_row)
    bot_ship_coords.append(bot_row)
# 
game = True
player_shots = []
bot_shots = []
screen.blit(bg,(0,0))
#
bot_turn = False
player_turn = True
decks = [m_Class.Ship4, m_Class.Ship3,  m_Class.Ship3, m_Class.Ship2, m_Class.Ship2, m_Class.Ship2, m_Class.Ship1, m_Class.Ship1, m_Class.Ship1, m_Class.Ship1]
clicks = 0  
# 
bot_ships = [] 
player_ships = []

# Создания кораблей бота def

for ships_size in step_b:
    while True:
        col =random.randint(0,9)
        row = random.randint(0,9)
        direction = random.choice(["horizontal","vertical"])
        if direction == "horizontal" and col + ships_size <= 10:
            if m_fun.valid_pos(m_list.bot_field, row, col, ships_size):
                for c in range(col, col + ships_size):
                    m_list.bot_field[row][c] = ships_size
                break
        if direction == "vertical" and row + ships_size <= 10:
            if m_fun.valid_pos(m_list.bot_field, row, col, ships_size):
                for r in range(row, row + ships_size):
                    m_list.bot_field[r][col] = ships_size
                break
# для отображения кораблей бота (попадания по ним)
for row in range(10):
    for col in range(10):
        if m_list.bot_field[row][col] != 0:
            ship = pygame.Rect(bot_ship_coords[row][col][0], bot_ship_coords[row][col][1], size_cells - 1, size_cells - 1)
            bot_ships.append(ship)
            
print(m_list.bot_field)
            
vertical = False
current_ship = None               
table2 = pygame.draw.rect(screen, (161,222,245), ((17 * size_cells, top_ind), (350,350)))
table1 = pygame.draw.rect(screen, (161,222,245), ((left_ind,  top_ind), (350, 350)))
m_fun.draw_table()
button = pygame.draw.rect(screen, (80,111,255), ((425, 550),(160, 80)))
font_b = pygame.font.SysFont("Arial", 50)
render = font_b.render("Почати", 1, "white")
screen.blit(render, (435, 555))
font_b = pygame.font.SysFont("Arial", 45)
image = bg
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            # Робота с координатами картинки
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // size_cells
            row = y // size_cells
            x = col * size_cells + 1
            y = row * size_cells + 1
             # Отоброжения картинки при нажатии на поле 1    
            if table1.collidepoint(pygame.mouse.get_pos()):
                if clicks < len(decks):
                    deck = decks[clicks]
                    deck.__init__(deck, x, y)
                    deck_rect = deck.IMAGE.get_rect()
                    deck_rect.x = x
                    deck_rect.y = y
                    player_ship = deck.rotate(deck, rotation)
                    player_ships.append(deck_rect)
                    deck.blit_sprite(deck, screen)
                    clicks += 1
                    if current_ship == None:
                        current_ship = deck_rect
                        if vertical == True:
                            for i in range(step[clicks]):
                                row1 = (current_ship.y - top_ind) // size_cells + i
                                col1 = (current_ship.x - left_ind) // size_cells  
                                m_list.player_field [row1] [col1] = step[clicks]  

                        if vertical == False:
                            for row1 in range(len(player_ship_coords)):
                                for col1 in range(len(player_ship_coords)):                                    
                                    if current_ship.collidepoint(player_ship_coords [row1] [col1]):
                                        m_list.player_field [row1] [col1] = step[clicks]
                        
                    current_ship = None
                    print(m_list.player_field)
                        
            # Ход игрока def
            if player_turn == True:
                if table2.collidepoint(pygame.mouse.get_pos()) and start == False:
                    if pygame.mouse.get_pressed(3)[0]:
                        x = col * size_cells + 1
                        y = row * size_cells + 1
                        if (x, y)  not in player_shots: 
                            player_shots.append((x, y))
                            for bot_ship in bot_ships:
                                if bot_ship.collidepoint(x, y):
                                    player_turn = True
                                    bot_turn = False
                                    player_hits += 1
                                    screen.blit(cross, (x,y))
                                    break
                                else:
                                    screen.blit(point, (x, y))
                                    player_turn = False
                                    bot_turn = True                
            else:
                image = bg 
        # Переворот корабля 
        elif event.type == pygame.KEYDOWN and start == True:
            if event.key == pygame.K_SPACE:
                rotation =(rotation + 90) % 180
                if rotation == 90:     
                    vertical = True
                else:
                    vertical = False            
    # Ограничения поставленых кораблей 
    if clicks >= 10:
        if button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            start = False
            button = pygame.draw.rect(screen, (0,255,0), ((425, 550),(160, 80)))
            screen.blit(render, (435, 555))
            #  ХОД бота def
        if bot_turn and start == False:
            if explosion == True:
                time.sleep(0.70)
                explosion = False
            if des == False:
                colp = random.randint(0, 9)
                rowp = random.randint(0, 9)
                last_direction = None
            colp %= 10
            rowp %= 10
            if m_list.player_field[rowp][colp] == "d":
                if last_direction == None:
                    directione = "up"

                else:
                    directione = last_direction
                    if dir == "u":
                        directione = "up"
                    if dir == "d":
                        directione = "down"
                    if dir == "r":
                        directione = "right"
                    if dir == "l":
                        directione = "left"

            if des == True: 
                if directione == "up":
                    if rowp > 0:
                        if m_list.player_field[rowp - 1][colp] != "d" and m_list.player_field[rowp - 1][colp] != "m":
                            rowp = rowp - 1
                            directione = 'down'
                            dir = "u"
                        else:
                            dir = "d"
                            directione = 'down'
                    else:
                        dir = "d"
                        directione = 'down'
                elif directione == 'down':
                    rowp = last_coords[0]
                    colp = last_coords[1]
                    if rowp < 9:
                        if m_list.player_field[rowp + 1][colp] != "d" and m_list.player_field[rowp + 1][colp] != "m":
                            rowp = rowp + 1
                            directione = 'right'
                            dir = "d"
                        else:
                            dir = "r"
                            directione = 'right'
                    else:
                        dir = "r"
                        directione = 'right'
                elif directione == 'right':
                    rowp = last_coords[0]
                    colp = last_coords[1]
                    if colp < 9:
                        if m_list.player_field[rowp][colp + 1] != "d" and m_list.player_field[rowp][colp + 1] != "m":
                            colp = colp + 1
                            directione = 'left'
                            dir = "r"
                        else:
                            dir = "l"
                            directione = 'left'
                    else:
                        dir = "l"
                        directione = 'left'
                elif directione == 'left':
                    rowp = last_coords[0]
                    colp = last_coords[1]
                    if colp > 0:
                        if m_list.player_field[rowp][colp - 1] != "d" and m_list.player_field[rowp][colp - 1] != "m":
                            colp = colp - 1
                            dir = "l"
                            des = False
                        else:
                            dir = None
                            des = False
                    else:
                        dir = None
                        des = False
                last_direction = directione         

            print(rowp)
            print(colp)
            x = player_ship_coords[rowp][colp][0]
            y = player_ship_coords[rowp][colp][1]

            if (x, y) not in bot_shots:
                bot_shots.append((x, y))
                if m_list.player_field[rowp][colp] != 0:
                    bot_hits += 1
                    m_list.player_field[rowp][colp] = "d"  # destroyed - разрушен
                    screen.blit(cross, (x, y))
                    explosion = True
                    bot_turn = True
                    player_turn = False
                    b_hit = True
                    last_coords = (rowp, colp)
                    print(m_list.player_field)
                    des = True
                else:
                    m_list.player_field[rowp][colp] = "m"  # miss - промах
                    screen.blit(point, (x, y))
                    explosion = False
                    bot_turn = False
                    
                    player_turn = True
                    b_hit = False

        # Победа бота
        if bot_hits == 20:
            player_turn = False
            bot_turn = False
            button_win = pygame.image.load("images/Button.png")
            render1 = font_b.render("Перемога бота", 1, (74, 0, 106))
            screen.blit(button_win, (320, 520))
            screen.blit(render1, (385, 555))
        # Победа игрока
        elif player_hits == 20:
            player_turn = False
            bot_turn = False
            button_win = pygame.image.load("images/Button.png")
            screen.blit(button_win, (320,520))
            render1 = font_b.render("Перемога гравця", 1, "blue")
            screen.blit(render1, (370,555))

    pygame.display.flip() 