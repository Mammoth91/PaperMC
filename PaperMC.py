#================= Libraries ==========================
import pygame
import os
import math
from playsound import playsound

#================= PyGame Initialize ==========================
pygame.init()
win = pygame.display.set_mode((1500, 800)) #1200,800
pygame.display.set_caption("PaperMc")

#================= Global Variables ==========================
x = 0
y = 160
playerY = 80
width = 40
height = 80
vel = 40
isJump = False
jumpCount = 10
flightCount = 1
run = True

blockNumber = 1
playerBlockNumber = 1

playerBlock = 1
abovePlayerBlock = 1
belowPlayerBlock = 1
leftLowPlayerBlock = 1
leftHighPlayerBlock = 1
rightLowPlayerBlock = 1
rightHighPlayerBlock = 1

mouseBlock = 1
breakCounter = 1

#placeBlockType = 0

goUp = True
goLeft = True
goRight = True

_image_library = {}

#================= World Files ==========================
world1 = open("world.txt", "r").readlines()[0]
world2 = open("world.txt", "r").readlines()[1]
world3 = open("world.txt", "r").readlines()[2]
world4 = open("world.txt", "r").readlines()[3]
world5 = open("world.txt", "r").readlines()[4]
world6 = open("world.txt", "r").readlines()[5]
world7 = open("world.txt", "r").readlines()[6]
world8 = open("world.txt", "r").readlines()[7]
world9 = open("world.txt", "r").readlines()[8]
world10 = open("world.txt", "r").readlines()[9]
world11 = open("world.txt", "r").readlines()[10]
world12 = open("world.txt", "r").readlines()[11]
world13 = open("world.txt", "r").readlines()[12]
world14 = open("world.txt", "r").readlines()[13]
world15 = open("world.txt", "r").readlines()[14]
world16 = open("world.txt", "r").readlines()[15]
world17 = open("world.txt", "r").readlines()[16]
world18 = open("world.txt", "r").readlines()[17]
world19 = open("world.txt", "r").readlines()[18]
world20 = open("world.txt", "r").readlines()[19]

player_world1 = list(world1)
player_world2 = list(world2)
player_world3 = list(world3)
player_world4 = list(world4)
player_world5 = list(world5)
player_world6 = list(world6)
player_world7 = list(world7)
player_world8 = list(world8)
player_world9 = list(world9)
player_world10 = list(world10)
player_world11 = list(world11)
player_world12 = list(world12)
player_world13 = list(world13)
player_world14 = list(world14)
player_world15 = list(world15)
player_world16 = list(world16)
player_world17 = list(world17)
player_world18 = list(world18)
player_world19 = list(world19)
player_world20 = list(world20)

#================= Image Prep ==========================
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

#================= World Loading ==========================
def load_world():
    win.fill((255, 255, 255))
    placePosX = 0
    placePosY = 0
    countX = 0
    countY = 0
    while True:
        if countX == 30:
            countY = countY + 1
            placePosY = placePosY + 40
            countX = 0
            placePosX = 0
        if countY == 20:
            break

        if countY == 0:
            layerGet = player_world1
        elif countY == 1:
            layerGet = player_world2
        elif countY == 2:
            layerGet = player_world3
        elif countY == 3:
            layerGet = player_world4
        elif countY == 4:
            layerGet = player_world5
        elif countY == 5:
            layerGet = player_world6
        elif countY == 6:
            layerGet = player_world7
        elif countY == 7:
            layerGet = player_world8
        elif countY == 8:
            layerGet = player_world9
        elif countY == 9:
            layerGet = player_world10
        elif countY == 10:
            layerGet = player_world11
        elif countY == 11:
            layerGet = player_world12
        elif countY == 12:
            layerGet = player_world13
        elif countY == 13:
            layerGet = player_world14
        elif countY == 14:
            layerGet = player_world15
        elif countY == 15:
            layerGet = player_world16
        elif countY == 16:
            layerGet = player_world17
        elif countY == 17:
            layerGet = player_world18
        elif countY == 18:
            layerGet = player_world19
        elif countY == 19:
            layerGet = player_world20

        if layerGet[countX] == "1":
            win.blit(get_image('textures/bedrock.png'), (placePosX, placePosY))
        elif layerGet[countX] == "2":
            win.blit(get_image('textures/stone.png'), (placePosX, placePosY))
        elif layerGet[countX] == "3":
            win.blit(get_image('textures/grass.jpg'), (placePosX, placePosY))
        elif layerGet[countX] == "4":
            win.blit(get_image('textures/log.jpg'), (placePosX, placePosY))
        elif layerGet[countX] == "5":
            win.blit(get_image('textures/leaves.jpg'), (placePosX, placePosY))
        elif layerGet[countX] == "6":
            win.blit(get_image('textures/chest.jpg'), (placePosX, placePosY))
        elif layerGet[countX] == "7":
            win.blit(get_image('textures/crafting_table.png'), (placePosX, placePosY))
        elif layerGet[countX] == "8":
            win.blit(get_image('textures/furnace_on.png'), (placePosX, placePosY))
        elif layerGet[countX] == "9":
            win.blit(get_image('textures/furnace_off.png'), (placePosX, placePosY))

        countX = countX + 1
        placePosX = placePosX + 40

#================= Inventory Loading ==========================
#def inv_load():


#================= Block State Check ==========================
def check_block(blockNumber):
    difference = 0
    layerNum = 0

    if 0 < blockNumber < 31:
        layerNum = player_world1
        difference = 1
    elif 30 < blockNumber < 61:
        layerNum = player_world2
        difference = 31
    elif 60 < blockNumber < 91:
        layerNum = player_world3
        difference = 61
    elif 90 < blockNumber < 121:
        layerNum = player_world4
        difference = 91
    elif 120 < blockNumber < 151:
        layerNum = player_world5
        difference = 121
    elif 150 < blockNumber < 181:
        layerNum = player_world6
        difference = 151
    elif 180 < blockNumber < 211:
        layerNum = player_world7
        difference = 181
    elif 210 < blockNumber < 241:
        layerNum = player_world8
        difference = 211
    elif 240 < blockNumber < 271:
        layerNum = player_world9
        difference = 241
    elif 270 < blockNumber < 301:
        layerNum = player_world10
        difference = 271
    elif 300 < blockNumber < 331:
        layerNum = player_world11
        difference = 301
    elif 330 < blockNumber < 361:
        layerNum = player_world12
        difference = 331
    elif 360 < blockNumber < 391:
        layerNum = player_world13
        difference = 361
    elif 390 < blockNumber < 421:
        layerNum = player_world14
        difference = 391
    elif 420 < blockNumber < 451:
        layerNum = player_world15
        difference = 421
    elif 450 < blockNumber < 481:
        layerNum = player_world16
        difference = 451
    elif 480 < blockNumber < 511:
        layerNum = player_world17
        difference = 481
    elif 510 < blockNumber < 541:
        layerNum = player_world18
        difference = 511
    elif 540 < blockNumber < 571:
        layerNum = player_world19
        difference = 541
    elif 570 < blockNumber < 601:
        layerNum = player_world20
        difference = 571

    arrayNum = blockNumber - difference
    block = layerNum[arrayNum]
    return block

# ================= Set Block ==========================
def set_block(setBlockNumber, blockType):
    difference = 0

    if 0 < setBlockNumber < 31:
        difference = setBlockNumber - 1
        player_world1[difference] = blockType
    elif 30 < setBlockNumber < 61:
        difference = setBlockNumber - 31
        player_world2[difference] = blockType
    elif 60 < setBlockNumber < 91:
        difference = setBlockNumber - 61
        player_world4[difference] = blockType
    elif 90 < setBlockNumber < 121:
        difference = setBlockNumber - 91
        player_world4[difference] = blockType
    elif 120 < setBlockNumber < 151:
        difference = setBlockNumber - 121
        player_world5[difference] = blockType
    elif 150 < setBlockNumber < 181:
        difference = setBlockNumber - 151
        player_world6[difference] = blockType
    elif 180 < setBlockNumber < 211:
        difference = setBlockNumber - 181
        player_world7[difference] = blockType
    elif 210 < setBlockNumber < 241:
        difference = setBlockNumber - 211
        player_world8[difference] = blockType
    elif 240 < setBlockNumber < 271:
        difference = setBlockNumber - 241
        player_world9[difference] = blockType
    elif 270 < setBlockNumber < 301:
        difference = setBlockNumber - 271
        player_world10[difference] = blockType
    elif 300 < setBlockNumber < 331:
        difference = setBlockNumber - 301
        player_world11[difference] = blockType
    elif 330 < setBlockNumber < 361:
        difference = setBlockNumber - 331
        player_world12[difference] = blockType
    elif 360 < setBlockNumber < 391:
        difference = setBlockNumber - 361
        player_world13[difference] = blockType
    elif 390 < setBlockNumber < 421:
        difference = setBlockNumber - 391
        player_world14[difference] = blockType
    elif 420 < setBlockNumber < 451:
        difference = setBlockNumber - 421
        player_world15[difference] = blockType
    elif 450 < setBlockNumber < 481:
        difference = setBlockNumber - 451
        player_world16[difference] = blockType
    elif 480 < setBlockNumber < 511:
        difference = setBlockNumber - 481
        player_world17[difference] = blockType
    elif 510 < setBlockNumber < 541:
        difference = setBlockNumber - 511
        player_world18[difference] = blockType
    elif 540 < setBlockNumber < 571:
        difference = setBlockNumber - 541
        player_world19[difference] = blockType
    elif 570 < setBlockNumber < 601:
        difference = setBlockNumber - 571
        player_world20[difference] = blockType

# ================= Player Pos Calculations ==========================
def player_pos():
    playerX = x + 20
    playerY = y + 60
    checkPlayerX = 0
    checkPlayerXP = 40
    checkPlayerY = 0
    checkPlayerYP = 40
    playerBlockNumber = 1
    while True:
        if checkPlayerXP == 1240:
            checkPlayerY = checkPlayerY + 40
            checkPlayerYP = checkPlayerYP + 40
            checkPlayerX = 0
            checkPlayerXP = 40
        if checkPlayerYP == 840:
            break
        if x == 0 or x == 40 or x == 80 or x == 120 or x == 160 or x == 200 or x == 240 or x == 280 or x == 320 or x == 360 or x == 400 or x == 440 or x == 480 or x == 520 or x == 560 or x == 600 or x == 640 or x == 680 or x == 720 or x == 760 or x == 800 or x == 840 or x == 880 or x == 920 or x == 960 or x == 1000 or x == 1040 or x == 1080 or x == 1120 or x == 1160 or x == 1200:
            if checkPlayerX < playerX < checkPlayerXP and checkPlayerY < playerY < checkPlayerYP:
                global belowPlayerBlock
                belowPlayerBlock = playerBlockNumber + 30
                global abovePlayerBlock
                abovePlayerBlock = playerBlockNumber - 60
                global leftLowPlayerBlock
                leftLowPlayerBlock = playerBlockNumber - 1
                global leftHighPlayerBlock
                leftHighPlayerBlock = playerBlockNumber - 31
                global rightLowPlayerBlock
                rightLowPlayerBlock = playerBlockNumber + 1
                global rightHighPlayerBlock
                rightHighPlayerBlock = playerBlockNumber - 29
                global playerBlock
                playerBlock = playerBlockNumber
                break

        checkPlayerX = checkPlayerX + 40
        checkPlayerXP = checkPlayerXP + 40
        playerBlockNumber = playerBlockNumber + 1

#================= Mouse Pos Calculations ==========================
def mouse_pos():
    mouse = pygame.mouse.get_pos()
    mouseX = mouse[0]
    mouseY = mouse[1]
    checkX = 0
    checkXP = 40
    checkY = 0
    checkYP = 40
    blockNumber = 1

    while True:
        if checkXP == 1240:
            checkY = checkY + 40
            checkYP = checkYP + 40
            checkX = 0
            checkXP = 40
        if checkYP == 840:
            break
        if checkX < mouseX < checkXP and checkY < mouseY < checkYP:
            global mouseBlock
            mouseBlock = blockNumber
            return mouseBlock
            break
        checkX = checkX + 40
        checkXP = checkXP + 40
        blockNumber = blockNumber + 1

#================= Break Block ==========================
def break_block():
    mouse = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    mouseX = mousePos[0]
    mouseY = mousePos[1]
    canBreak = False

    if mouseX < x:
        xDiff = x - mouseX
    elif mouseX > x:
        xDiff = mouseX - x
    elif mouseX == x:
        xDiff = 0
    if mouseY < y:
        yDiff = y - mouseY
    elif mouseY > y:
        yDiff = mouseY - y
    elif mouseY == y:
        yDiff = 0

    lineLength = round(math.sqrt(xDiff * xDiff + yDiff * yDiff), 2)
    if lineLength > 250:
        canBreak = False
        global breakCounter
        breakCounter = 0
        color = 255, 0, 0
    elif lineLength <= 250:
        canBreak = True
        color = 0, 255, 0

    if check_block(mouseBlock) == "1":
        canBreak = False
    elif check_block(mouseBlock) == "0":
        canBreak = False
    elif check_block(mouseBlock) != "0" or check_block(mouseBlock) != "1":
        canBreak = True

    pygame.draw.line(win, color, (mouseX, mouseY), (x + 20, y + 40), 2)

    if mouse[0] == 1 and canBreak == True:
        breakCounter = breakCounter + 1
    elif mouse[0] == 0:
        breakCounter = 0

    if breakCounter == 5 and canBreak == True:
        print("break!")
        set_block(mouseBlock, "0")
        breakCounter = 0

#================= Place Block ==========================
def place_block(placeBlockType):
    mouse = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    mouseX = mousePos[0]
    mouseY = mousePos[1]
    placeBlockType = str(placeBlockType)
    canPlace = False

    if mouseX < x:
        xDiff = x - mouseX
    elif mouseX > x:
        xDiff = mouseX - x
    elif mouseX == x:
        xDiff = 0
    if mouseY < y:
        yDiff = y - mouseY
    elif mouseY > y:
        yDiff = mouseY - y
    elif mouseY == y:
        yDiff = 0

    lineLength = round(math.sqrt(xDiff * xDiff + yDiff * yDiff), 2)
    if lineLength > 250:
        canPlace = False
    elif lineLength <= 250:
        canPlace = True

    if mouse[2] == 1 and check_block(mouseBlock) == "0" and canPlace == True:
        set_block(mouseBlock, placeBlockType)
        print("place!")

#================= Quit ==========================
while run:
    pygame.time.delay(75)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #================= Functions ==========================
    #inv_load()
    load_world()
    win.blit(get_image('textures/inventory/inventory_smallchest.png'), (1200, 0))
    mouse_pos()
    player_pos()
    break_block()
    place_block("A")

    # ================= Collisions ==========================
    goUp = True
    goLeft = True
    goRight = True

    if check_block(leftHighPlayerBlock) != "0" or check_block(leftLowPlayerBlock) != "0":
        goLeft = False
    else:
        goLeft = True
    if check_block(rightHighPlayerBlock) != "0" or check_block(rightLowPlayerBlock) != "0":
        goRight = False
    else:
        goRight = True
    if check_block(abovePlayerBlock) != "0":
        goUp = False
    else:
        goUp = True

    # ================= Movement ==========================
    keys = pygame.key.get_pressed()
    if isJump == True and keys[pygame.K_w] and keys[pygame.K_a]:
        goLeft = False
    elif isJump == True and keys[pygame.K_w] and keys[pygame.K_d]:
        goRight = False

    if keys[pygame.K_a] and x > 0 and goLeft == True:
        x -= vel

    if keys[pygame.K_d] and x < 1200 - width and goRight == True:
        x += vel

    if not isJump:
        if keys[pygame.K_w] and goUp == True:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.1
            jumpCount -= 4
        else:
            jumpCount = 10
            isJump = False

    if keys[pygame.K_w] and isJump == True and check_block(belowPlayerBlock) != "0":
        y = y - 40
    elif isJump == False and check_block(playerBlock) != "0":
        y = y - 40
    elif isJump == False and check_block(belowPlayerBlock) == "0":
        y = y + 40

    # ================= Debug ==========================
    #print(isJump,run,mouseX,mouseY)
    #print(playerX,playerY)
    #print(playerBlock, belowPlayerBlock, abovePlayerBlock, leftHighPlayerBlock, leftLowPlayerBlock, rightHighPlayerBlock,rightLowPlayerBlock)
    #print(mouseBlock)
    #print(check_block(belowPlayerBlock))
    #print(isJump, jumpCount)

    # ================= Display ==========================
    win.blit(get_image('textures/player.png'), (x, y))
    pygame.display.update()

pygame.quit()