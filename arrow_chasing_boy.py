from pico2d import *
import random

open_canvas(1280, 1024)

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

random_numbers_x = [random.randint(10, 1270) for n in range(30)]
random_numbers_y = [random.randint(10, 1014) for n in range(30)]

def move_character():
    global x, y, charx, chary, i, a, dir

    x1, y1 = random_numbers_x[i], random_numbers_y[i]
    x2, y2 = random_numbers_x[i+1], random_numbers_y[i+1]

    if(a < 101):
        t = a / 100
        charx = (1-t)*x1 + t*x2
        chary = (1-t)*y1 + t*y2
        character_animation(charx, chary, dir)
        a += 1
    else:
        character_animation(charx, chary, dir)

    if(random_numbers_x[i + 1] == charx and random_numbers_y[i + 1] == chary):
        i += 1
        a = 0
        if(random_numbers_x[i] < random_numbers_x[i+1]):
            dir = -1
        else:
            dir = 1
    else:
        arrow.draw(random_numbers_x[i + 1], random_numbers_y[i + 1])

def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def character_animation(charx, chary, dir):
    if dir == 1:
        character.clip_draw(frame * 100, 0, 100, 100, charx, chary)
    elif dir == -1:
        character.clip_draw(frame * 100, 100, 100, 100, charx, chary)

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0
i = 0
a = 0
charx = random_numbers_x[0]
chary = random_numbers_y[0]

if(random_numbers_x[0] < random_numbers_x[1]):
    dir = -1
else:
    dir = 1

while running:
    clear_canvas()
    ground.draw(640, 512)
    handle_events()
    move_character()
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()