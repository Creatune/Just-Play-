import pygame
import time
import random
pygame.init()
screen_width = 800
screen_height = 600
screenSize = (screen_width,screen_height)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("car game")
pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
grey = (211,211,211)
green = (0,200,0)
midnight_blue = (25,25,112)
pink = (255, 105, 180)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
yellow = (255,255,0)
lst_colors = [black, white, red, green, pink]
block_colors = random.choice(lst_colors)
car_width = 61
carImg = pygame.image.load('red-car-top-view.png')
diamIMG = pygame.image.load('diamond.png')
diam_height = 41
diam_width = 38

def rules():
    pass

def diamonds(x,y):
    pass


def things_dodged(dodge_count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(dodge_count), True, pink)
    screen.blit(text, (0,0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(screen, color, [thingx, thingy, thingw, thingh])


def car(x,y):
    screen.blit(carImg, (x,y))


def Text_objects(text, font):
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = Text_objects(text, largeText)
    TextRect.center = ((screen_width/2), (screen_height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_intro()


def crash():
    message_display('You Crashed')


def quit_game():
    pygame.quit()
    quit()


def button(msg, x, y, w, h, ic, ac, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect = Text_objects(msg, smallText)
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    screen.blit(TextSurf, TextRect)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(midnight_blue)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = Text_objects("Just Play!", largeText)
        TextRect.center = ((screen_width/2), (screen_height/2))
        screen.blit(TextSurf, TextRect)
        button("Play!", 150, 450, 100, 50, green, bright_green, game_loop)
        #button("Rules", 350, 450, 100, 50, white, grey, rules)   I will code this part later..
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)
        pygame.display.update()


def game_loop():
    x = (screen_width * 0.45)
    y = (screen_height * 0.8)
    x_change = 0
    thing_startx = random.randrange(0, screen_width)
    thing_starty = -600
    thing_speed = 0.75
    thing_width = 100
    thing_height = 100
    gameExit = False
    dodge_count = 0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -1.5
                if event.key == pygame.K_RIGHT:
                    x_change = 1.5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        screen.fill(midnight_blue)
        car(x,y)
        things_dodged(dodge_count)
        if thing_starty > screen_height:
            thing_starty = 0 - screen_height
            thing_startx = random.randrange(0, (screen_width - 100))
            dodge_count += 1
            thing_speed += 0.25
            #thing_width += dodge_count * 1.1
        things(thing_startx, thing_starty, thing_width, thing_height, block_colors)
        thing_starty += thing_speed
        if x > screen_width - car_width or x < 0:
            crash()
        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()
        pygame.display.update()


game_intro()
game_loop()
pygame.quit()
