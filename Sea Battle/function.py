import pygame
import random
import modules.list as m_list
pygame.init()
size_cells = 35
# отступ слева
left_ind = 70
# отступ свершу
top_ind = 105
screen = pygame.display.set_mode((1000,700))
font = pygame.font.SysFont("Arial", size_cells)
step_b = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1 ]
def draw_table(): 
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for count in range(11):
        # Первая таблица
        pygame.draw.line(screen, (0, 0, 0), (left_ind, top_ind + count * size_cells), (left_ind + 10 * size_cells, top_ind + count * size_cells), 3)
        pygame.draw.line(screen, (0, 0, 0), (left_ind + count * size_cells, top_ind), (left_ind + count * size_cells, top_ind + 10 * size_cells), 3)
        # Вторая таблица
        pygame.draw.line(screen, (0, 0, 0,), (17 * size_cells, top_ind + count * size_cells), (27 * size_cells, top_ind + count * size_cells), 3)
        pygame.draw.line(screen, (0, 0, 0,),((count + 17 ) * size_cells, top_ind), ((count + 17) * size_cells,  top_ind + 10 *size_cells), 3)
        if count < 10:
            num = font.render(str(count + 1), True, (0,0,0))
            let = font.render(letters [count], True, (0,0,0))
            # 
            num_width = num.get_width()
            num_height = num.get_height()
            let_width = let.get_width() 
            # отображает текст первой таблицы
            screen.blit(num, (left_ind - (size_cells // 2 + num_width // 2), top_ind + count * size_cells + (size_cells // 2 - num_height // 2)))
            screen.blit(let, (left_ind + count * size_cells + (size_cells // 2 - let_width // 2), top_ind - 70 // 2))
            # отображает текст второй таблицы
            screen.blit(num, (left_ind - (size_cells + num_width) + 16 * size_cells - 7, top_ind + count * size_cells + (size_cells // 2 - num_height // 2)))
            screen.blit(let, (count * size_cells + (size_cells // 2 - let_width // 2) + 17 * size_cells, top_ind - 70 // 2))
def valid_pos(field, row, col, ship_size):
    # Создания условия которое не разришает выходить из поля   
    if row < 0 or row > 9 or col < 0 or col > 9:
        return False
    # Проверка на пустоту ячеик кораблей бота 
    for r in range(row, row + ship_size):
        for c in range(col, col + ship_size):
            if r >= 0 and r < 10 and c >= 0 and c < 10:
                if field[r][c] != 0:
                    return False
    # Проверка на пустоту ячеик вокруг бота
    for r in range(row - 1, row + ship_size + 1):
        for c in range(col - 1, col + ship_size + 1):
            if r >= 0 and r < 10 and c >= 0 and c < 10:
                if field[r][c] != 0:
                    return False
    return True



