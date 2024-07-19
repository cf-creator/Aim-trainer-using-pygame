import time
import pygame
import random


pygame.init()

# set the display screen
screen = pygame.display.set_mode((800,500))
# rectangle
rect = pygame.Rect(200, 125, 30, 30)

# caption
pygame.display.set_caption("aim trainer using pygame")

# frame rate
clock = pygame.time.Clock()
total = 0
vel = 2
vel_y = 2


color = "red"
options = ["green", "blue", "yellow", "white", "light blue"]

font = pygame.font.SysFont(None, 36)

def loop3():
    global font, color, options
    total_o = 0
    rect5 = pygame.Rect(200, 125, 50, 50)
    screen = pygame.display.set_mode((800, 500))
    clock = pygame.time.Clock()
    vel_5o1 = 4
    rect_o = pygame.Rect(700, 0, 100, 60)
    # Font
    font = pygame.font.SysFont(None, 36)
    # to keep a track on the time
    start = time.time()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True

        # our mouse pos
        x,y = pygame.mouse.get_pos()

        # to register our mouse press
        m = pygame.mouse.get_pressed()

        # to get the time in seconds
        elapsed_time = time.time() - start

        color = random.choice(options)

        rect5.y +=vel_5o1
        rect5.h -=1
        rect5.w-=1
        pygame.time.delay(20)

        if rect5.h < 0 or rect5.w < 0:
            total_o-=1
            rect5.x = random.randint(0, 700)
            rect5.y = random.randint(70, 100)
            rect5.h = 50
            rect5.w = 50

        if rect5.collidepoint(x,y):
            if m[0]:
                rect5.h = 50
                rect5.w = 50
                rect5.x = random.randint(100, 700)
                rect5.y = random.randint(70, 125)
                total_o+=1

        screen.fill("black")
        pygame.draw.rect(screen, color, rect5, 10)
        txt = font.render(f"score: {total_o}\n time: {elapsed_time: .1f}", False, "blue")
        screen.blit(txt, (0,0))
        txt2 = font.render("Menu", True, "white")
        txt1 = txt2.get_rect(center=(rect_o.center))
        screen.blit(txt2, txt1)
        pygame.draw.rect(screen, "blue", rect_o, 1)
        if rect_o.collidepoint(x, y):
            if m[0]:
                menu()
        pygame.display.flip()
        clock.tick(60)

def loop2():
    rect1 = pygame.Rect(200, 125, 50, 50)
    screen1 = pygame.display.set_mode((800, 500))
    rect_o = pygame.Rect(700, 0, 100, 60)
    font = pygame.font.SysFont(None, 36)
    start_time = time.time()
    total_1 = 0
    run1 = True
    while run1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run1 = True

        x,y = pygame.mouse.get_pos()
        m = pygame.mouse.get_pressed()

        rect1.h-=1
        rect1.w-=1
        pygame.time.delay(10)
        if rect1.h < 0 or rect1.w < 0:
            total_1 -= 1
            rect1.x = random.randint(30, 800 - 60)
            rect1.y = random.randint(30, 500 - 60)
            rect1.h = 50
            rect1.w = 50
        if rect1.collidepoint(x, y):
            if m[0]:
                total_1 += 1
                rect1.h = 50
                rect1.w = 50
                rect1.x = random.randint(50, 800 - 60)
                rect1.y = random.randint(50, 500 - 60)

        screen1.fill("black")
        pygame.draw.rect(screen1, "blue", rect1, 10)
        txt = font.render("Menu", True, "white")
        txt1 = txt.get_rect(center=(rect_o.center))
        screen.blit(txt, txt1)
        txt2 = font.render(f"score: {total_1}\n time:  {time.time() - start_time:.1f}", False, "blue")
        screen.blit(txt2, (0, 0))
        pygame.draw.rect(screen, "blue", rect_o, 1)
        if rect_o.collidepoint(x, y):
            if m[0]:
                menu()
        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)

def loop1():
    global total, color, options
    run = True
    rect_o = pygame.Rect(700, 0, 100, 60)
    font = pygame.font.SysFont(None, 36)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True

        x,y = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        if rect.collidepoint(x,y):
            if mouse[0]:
                color = random.choice(options)
                total += 1
                rect.y = random.randint(60, 500 - rect.h)
                rect.x = random.randint(60, 800 - rect.w)

        screen.fill("black")

        pygame.draw.rect(screen, color, rect, 5)

        text = font.render(f"score: {total}", True, "white")
        screen.blit(text, (0, 0))
        txt = font.render("Menu", True, "white")
        txt1 = txt.get_rect(center=(rect_o.center))
        screen.blit(txt, txt1)
        pygame.draw.rect(screen, "blue", rect_o, 1)

        if rect_o.collidepoint(x,y):
            if mouse[0]:
                menu()

        pygame.display.flip()
        clock.tick(60)

def menu():
    screen = pygame.display.set_mode((800, 500))

    font = pygame.font.SysFont(None, 36)
    title_font = pygame.font.SysFont(None, 48)

    rect1 = pygame.Rect(200, 100, 400, 50)
    rect2 = pygame.Rect(200, 200, 400, 50)
    rect3 = pygame.Rect(200, 300, 400, 50)

    run = True
    while run:
        for event in pygame.event.get():
            screen.fill("black")

        title_text = title_font.render("Choose one of these levels", False, "white")
        title_rect = title_text.get_rect(center=(screen.get_width() / 2, 50))
        screen.blit(title_text, title_rect)

        txt1 = font.render("Level 1", False, "white")
        txt1_rect = txt1.get_rect(center=(rect1.center))
        screen.blit(txt1, txt1_rect)
        pygame.draw.rect(screen, "green", rect1, 1)

        txt2 = font.render("Level 2", False, "white")
        txt2_rect = txt2.get_rect(center=(rect2.center))
        screen.blit(txt2, txt2_rect)
        pygame.draw.rect(screen, "green", rect2, 1)

        txt3 = font.render("Level 3", False, "white")
        txt3_rect = txt3.get_rect(center=(rect3.center))
        screen.blit(txt3, txt3_rect)
        pygame.draw.rect(screen, "green", rect3, 1)

        rect4 = pygame.Rect(200, 400, 400, 50)
        txt4 = font.render("Exit", False, "white")
        txt4_rect = txt4.get_rect(center=(rect4.center))
        screen.blit(txt4, txt4_rect)
        pygame.draw.rect(screen, "green", rect4, 1)

        x, y = pygame.mouse.get_pos()
        m = pygame.mouse.get_pressed()
        if rect1.collidepoint(x, y):
            if m[0]:
                loop1()
        elif rect2.collidepoint(x, y):
            if m[0]:
                loop2()
        elif rect4.collidepoint(x, y):
            if m[0]:
                run = False
                pygame.quit()
        elif rect3.collidepoint(x,y):
            if m[0]:
                loop3()

        pygame.display.flip()

def main():
    menu()

main()

