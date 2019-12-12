import pygame
import os

pygame.init()
win = pygame.display.set_mode((440, 500))
pygame.display.set_caption("PaperMc")

x = 50
y = 340
width = 40
height = 80
vel = 15
isJump = False
jumpCount = 10
run = True

_image_library = {}

f= open("world.txt","w+")

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 400 - vel:
        x += vel

    if not (isJump):
        if keys[pygame.K_DOWN] and y < 400 - height - vel:
            y += vel

        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.25
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    win.fill((255, 255, 255))
    win.blit(get_image('grass.jpg'), (0, 420))
    win.blit(get_image('grass.jpg'), (40, 420))
    win.blit(get_image('grass.jpg'), (80, 420))
    win.blit(get_image('grass.jpg'), (120, 420))
    win.blit(get_image('grass.jpg'), (160, 420))
    win.blit(get_image('grass.jpg'), (200, 420))
    win.blit(get_image('grass.jpg'), (240, 420))
    win.blit(get_image('grass.jpg'), (280, 420))
    win.blit(get_image('grass.jpg'), (320, 420))
    win.blit(get_image('grass.jpg'), (360, 420))
    win.blit(get_image('grass.jpg'), (400, 420))

    win.blit(get_image('stone.png'), (0, 460))
    win.blit(get_image('stone.png'), (40, 460))
    win.blit(get_image('stone.png'), (80, 460))
    win.blit(get_image('stone.png'), (120, 460))
    win.blit(get_image('stone.png'), (160, 460))
    win.blit(get_image('stone.png'), (200, 460))
    win.blit(get_image('stone.png'), (240, 460))
    win.blit(get_image('stone.png'), (280, 460))
    win.blit(get_image('stone.png'), (320, 460))
    win.blit(get_image('stone.png'), (360, 460))
    win.blit(get_image('stone.png'), (400, 460))

    win.blit(get_image('log.jpg'), (320, 380))
    win.blit(get_image('log.jpg'), (320, 340))
    win.blit(get_image('leaves.jpg'), (320, 300))
    win.blit(get_image('leaves.jpg'), (320, 260))
    win.blit(get_image('leaves.jpg'), (280, 300))
    win.blit(get_image('leaves.jpg'), (360, 300))
    


    
    

    win.blit(get_image('player.jpg'), (x, y))
    pygame.display.update()

pygame.quit()


