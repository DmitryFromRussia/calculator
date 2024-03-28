import pygame

pygame.init()

# Создание окна программы:
screen = pygame.display.set_mode((240, 420))
# Название приложения:
pygame.display.set_caption("Калькулятор")

# Цвета, используемые в программе:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
LIGHT_GRAY = (120, 120, 120)
DARK_GRAY = (80, 80, 80)
ORANGE = (215, 30, 0)

# Установка шрифта и размера текста:
font = pygame.font.SysFont("Courier", 32, bold=True)

# Строка, хранящая ввод пользователя:
current_input = ""

# Описание кнопок калькулятора, их позиции (и размера):
buttons = [
    ('1', (5, 300)), ('2', (65, 300)), ('3', (125, 300)),
    ('4', (5, 240)), ('5', (65, 240)), ('6', (125, 240)),
    ('7', (5, 180)), ('8', (65, 180)), ('9', (125, 180)),
    ('0', (5, 360)), ('.', (65, 360)), ('=', (125, 360), (110, 50)),
    ('+', (185, 300)), ('-', (185, 240)), ('*', (185, 180)),
    ('/', (185, 120)), ('(', (65, 120)), (')', (125, 120)),
    ('C', (5, 120))
]


def draw_input(text):
    '''Выводит на экран введенное выражение с правой стороны.'''
    # Задаем объект текста:
    input_text = font.render(text, True, BLACK)
    # Создаем прямоугольник - область отображения текста:
    text_rect = input_text.get_rect()
    # Устанавливаем позицию прямоугольника от его правого верхнего угла:
    text_rect.topright = (screen.get_width() - 5, 5)
    # Отрисовываем текст в прямоугольнике:
    screen.blit(input_text, text_rect)


def draw_button(text, position, button_color, size=(50, 50)):
    '''
    Отрисовывает кнопки на экране с заданными
    текстом, позицией, цветом и размером.
    '''
    pygame.draw.rect(screen, button_color, (position[0], position[1], *size))
    graffiti = font.render(text, True, WHITE)
    screen.blit(
        graffiti,
        (
            position[0] + size[0] // 2 - graffiti.get_width() // 2,
            position[1] + size[1] // 2 - graffiti.get_height() // 2,
        ),
    )


def calculate(expression):
    '''Вычисляет результат выражения, заданного в строке.'''
    try:
        return str(eval(expression))
    except Exception:
        return "Error"


# Флаг для основного цикла:
running = True
# Основной цикл приложения:
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # При нажатии кнопки мыши:
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Получение позиции курсора:
            mous_pos = event.pos
            for button in buttons:
                button_text = button[0]
                button_pos = button[1]
                button_size = button[2] if len(button) > 2 else (50, 50)
                # Создание прямоугольника с параметрами:
                button_rect = pygame.Rect(button_pos[0], button_pos[1], *button_size)
                # Проверка нажатия курсора в области "кнопки":
                if button_rect.collidepoint(mous_pos):
                    if button_text == "=":
                        current_input = calculate(current_input)
                    elif button_text == "C":
                        current_input = ""
                    else:
                        current_input += button_text
                    break
    # Заливка экрана:
    screen.fill(GRAY)
    # Цикл отрисовки кнопок:
    for button in buttons:
        button_text = button[0]
        button_pos = button[1]
        button_size = button[2] if len(button) > 2 else (50, 50)
        # Определение цвета кнопки в зависимости от ее предназначения:
        if button_text == "=":
            button_color = ORANGE
        elif button_text.isdigit() or button_text == ".":
            button_color = LIGHT_GRAY
        else:
            button_color = DARK_GRAY
        draw_button(button_text, button_pos, button_color, button_size)
    # Отрисовка ввода пользователя:
    draw_input(current_input)

    pygame.display.flip()

pygame.quit()
