import pygame
import math
import random
import sys

pygame.init()
pygame.font.init()
pygame.display.set_caption('3분_우주방어')

width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

how_controlimg = pygame.image.load('resource/how_control.png')
user = pygame.image.load('resource/user.png')
userCoreimg = pygame.image.load('resource/user_core.png')
earth = pygame.image.load('resource/earth.png')
space = pygame.image.load('resource/space2.png')
spaceStars = pygame.image.load('resource/space3.png')
star01 = pygame.image.load('resource/star01.png')
missileimg = pygame.image.load('resource/missile.png')
missileCoreimg = pygame.image.load('resource/missile_core.png')
yamatoimg = pygame.image.load('resource/yamato.png')
yamatoCoreimg = pygame.image.load('resource/yamato_core.png')
yamatoScrimg = pygame.image.load('resource/yamatoScr.png')
ghostimg = pygame.image.load('resource/ghost.png')
ghostCoreimg = pygame.image.load('resource/ghost_core.png')
monsterimg = pygame.image.load('resource/mon01.png')
monsterCoreimg = pygame.image.load('resource/mon01_core.png')
stoneimg = pygame.image.load('resource/stone.png')
stoneCoreimg = pygame.image.load('resource/stone_core.png')
healthbar = pygame.image.load('resource/healthbar.png')
health = pygame.image.load('resource/health.png')
health_red = pygame.image.load('resource/health_red.png')
gameover = pygame.image.load('resource/gameover.png')
youwin = pygame.image.load('resource/youwin.png')
level01img = pygame.image.load('resource/level01.png')
level02img = pygame.image.load('resource/level02.png')
level03img = pygame.image.load('resource/level03.png')
scvimg = pygame.image.load('resource/scv.png')

mon_death = pygame.mixer.Sound('resource/death.wav')
mon_death.set_volume(0.2)
repair01 = pygame.mixer.Sound('resource/repair01.wav')
repair01.set_volume(1)
yamatosnd = pygame.mixer.Sound('resource/yamato.wav')
yamatosnd.set_volume(1)
nuclearReady = pygame.mixer.Sound('resource/nuclearReady.wav')
nuclearReady.set_volume(0.2)
colliderect01 = pygame.mixer.Sound('resource/colliderect01.wav')
colliderect01.set_volume(0.5)
shoot01 = pygame.mixer.Sound('resource/shoot01.wav')
shoot01.set_volume(0.1)

while 1:
    # Playing bgm
    pygame.mixer.music.stop()
    pygame.mixer.music.load('resource/bgm_play.wav')
    pygame.mixer.music.play(2, 0.0)
    pygame.mixer.music.set_volume(0.25)

    # game time init
    time = 0
    time2 = 0

    # User position init
    userPos = [600, 750]
    userCorePos = [570, 720]

    # check W, A, S, D
    keys = [False, False, False, False]

    # backgroud img
    space01 = [[0, -4000]]

    # def health
    healthvalue = 484

    # def missile
    missiles = []

    # def stars
    starTimer = 100
    starTimer1 = 0
    starpos = [[random.randint(100, 1100), random.randint(100, 700)]]

    # def monster
    monTimer = 100
    monTimer1 = 0
    monster = [[random.randint(100, 1100), -100]]

    # def stone
    stoneTimer = 100
    stoneTimer1 = 0
    stone = [[random.randint(100, 1100), -100]]

    # def scv
    scvTimer = 1000
    scvTimer1 = 0

    scv = [[random.randint(100, 1100), -100]]
    scvTime = random.randint(30, 60)

    # def ghost
    ghostTimer = 1400
    ghostTimer1 = 0
    ghost = [[random.randint(100, 1100), -100]]
    ghostTime = random.randint(30, 60)

    # nuclear
    nuclearCnt = 0

    # def yamato
    yamato = []
    yamatoScreen = []
    yamatoCore = []


    # def level location
    level01 = [[380, -250]]
    level02 = [[1200, 300]]
    level03 = [[-500, 300]]

    running = 1
    exitcode = 0

    while running:
        try:

            screen.fill((0, 0, 0))

            # background space - start
            for space01Move in space01:
                    space01Move[1] += 0.2

            for space01Move in space01:
                screen.blit(space, space01Move)

            screen.blit(spaceStars, (0, 0))
            # background space - end

            screen.blit(how_controlimg, (790, 0))

            # Draw clock and Set Time - start
            time1 = int(pygame.time.get_ticks() / 1000)

            # check 1 second
            if time1 > time2:
                time2 = time1
                time += 1

            font2 = pygame.font.SysFont('arial', 50)
            text2 = font2.render(str(int((180 - time) / 60)) + ":" + str(int((180 - time) % 60)).zfill(2), True, (255, 255, 0))
            text2Rect = text2.get_rect()
            text2Rect.topright = [1190, 5]
            screen.blit(text2, text2Rect)
            # Draw clock and Set Time - end

            # Draw nuclear Cnt - start
            fontNucle = pygame.font.SysFont('arial', 30)
            textNucle = fontNucle.render("Nuclear " + str(nuclearCnt) + "/3 :", True, (255, 0, 0))
            textNucleRect = textNucle.get_rect()
            textNucleRect.topright = [695, 10]
            screen.blit(textNucle, textNucleRect)
            # Draw nuclear Cnt - end


            # level01 display - start
            indexLev01 = 0
            for level01Move in level01:
                if level01Move[1] > 900:
                    level01.pop(indexLev01)
                else:
                    level01Move[1] += 2

                indexLev01 += 1

            for level01Move in level01:
                screen.blit(level01img, level01Move)
            # level01 display - end

            # level02 display - start
            if time >= 60:
                indexLev02 = 0
                for level02Move in level02:
                    if level02Move[0] < -500:
                        level02.pop(indexLev02)
                    else:
                        level02Move[0] -= 2

                    indexLev02 += 1

                for level02Move in level02:
                    screen.blit(level02img, level02Move)
            # level02 display - end

            # level03 display - start
            if time >= 120:
                indexLev03 = 0
                for level03Move in level03:
                    if level03Move[0] > 1500:
                        level03.pop(indexLev03)
                    else:
                        level03Move[0] += 2

                    indexLev03 += 1

                for level03Move in level03:
                    screen.blit(level03img, level03Move)
            # level03 display - end

            screen.blit(earth, (0, 659))

            # Draw stars - start
            starTimer -= 1
            if starTimer == 0:
                starpos.append([random.randint(10, 1690), random.randint(10, 900)])
                starTimer = 100 - starTimer1
                if starTimer1 >= 50:
                    starTimer1 = 50
                else:
                    starTimer1 += 5

            indexStar = 0
            for starMove in starpos:
                starRect = pygame.Rect(star01.get_rect())
                starRect.left = starMove[0]
                starRect.bottom = starMove[1]

                if starMove[0] < -170 or starMove[1] > 680 or starRect.bottom > 680:
                    starpos.pop(indexStar)
                else:
                    starMove[0] -= 10
                    starMove[1] += 5

                indexStar += 1

            for starMove in starpos:
                screen.blit(star01, starMove)
            # Draw stars - end

            # user position and rotate - start
            position = pygame.mouse.get_pos()
            angle = math.atan2(position[1] - (userPos[1] + 55), position[0] - (userPos[0] + 38))
            userRot = pygame.transform.rotate(user, 360 - angle * 57.29)
            userPos2 = (userPos[0] - userRot.get_rect().width//2, userPos[1] - userRot.get_rect().height//2)
            screen.blit(userRot, userPos2)

            userCorePosRect = pygame.Rect(userCoreimg.get_rect())
            userCorePosRect.left = userCorePos[0]
            userCorePosRect.top = userCorePos[1]
            # user position and rotate - end

            # Draw missile - start
            index = 0
            for m1 in missiles: # missiles <== [각도, 플레이어의 x좌표, 플레이어의 y좌표]
                dx = math.cos(m1[0]) * 20
                dy = math.sin(m1[0]) * 20
                m1[1] += dx
                m1[2] += dy
                if m1[1] < -64 or m1[1] > 1300 or m1[2] < -64 or m1[2] > 900:
                    missiles.pop(index)
                index += 1

            for m2 in missiles:
                missileimg2 = pygame.transform.rotate(missileimg, 360 - m2[0] * 57.29)
                screen.blit(missileimg2, (m2[1], m2[2]))
            # Draw missile - end

            # yamato - start
            indexYamato = 0
            for yamt in yamato:
                if yamt[1] < -100:
                    yamato.pop(indexYamato)
                else:
                    yamt[1] -= 10

                indexYamato += 1

            for yamt in yamato:
                screen.blit(yamatoimg, yamt)

            for yamtScr in yamatoScreen:
                screen.blit(yamatoScrimg, yamtScr)
            # yamato - end

            # Level 1 - Only monster
            # Level 3 - [Monster] & Stone
            if (time >= 3 and time < 60) or (time >= 120):
                monTimer -= 1
                # Draw Monster
                if monTimer == 0:
                    monster.append([random.randint(10, 1100), -100])
                    monTimer = 100 - monTimer1
                    if monTimer1 >= 85:
                        monTimer1 = 85
                    else:
                        monTimer1 += 5

            if time >= 3:
                indexMon = 0
                for mon in monster:
                    mon[1] += 2

                    # Attack earth
                    monCoreRect = pygame.Rect(monsterCoreimg.get_rect())
                    monCoreRect.left = mon[0] + 5
                    monCoreRect.top = mon[1] + 5
                    if monCoreRect.top > 795:
                        healthvalue -= 10
                        monster.pop(indexMon)

                    # Check for collision
                    indexMis = 0
                    for m3 in missiles:
                        missileCoreRect = pygame.Rect(missileCoreimg.get_rect())
                        missileCoreRect.left = m3[1] + 5
                        missileCoreRect.top = m3[2] + 2

                        if monCoreRect.colliderect(missileCoreRect):
                            try:
                                mon_death.play()
                                monster.pop(indexMon)
                                missiles.pop(indexMis)
                            except IndexError:
                                print('Empty the index of Monster and Missile')

                        indexMis += 1

                    for yamt in yamato:
                        yamatoCoreRect = pygame.Rect(yamatoCoreimg.get_rect())
                        yamatoCoreRect.left = yamt[0] + 8
                        yamatoCoreRect.top = yamt[1] + 19

                        if monCoreRect.colliderect(yamatoCoreRect):
                            try:
                                mon_death.play()
                                monster.pop(indexMon)
                            except IndexError:
                                print('Empty the index of Monster and Yamato')

                    indexMon += 1

                for mon in monster:
                    screen.blit(monsterimg, mon)

            # Level 2 - Only stone
            # Level 3 - Monster & [Stone]
            if time >= 60:
                stoneTimer -= 1
                # Draw Stone
                if stoneTimer == 0:
                    stone.append([random.randint(10, 1100), -100])
                    stoneTimer = 100 - (stoneTimer1 * 2)
                    if stoneTimer1 >= 40:
                        stoneTimer1 = 40
                    else:
                        stoneTimer1 += 5

                indexStn = 0
                for stn in stone:
                    if stn[1] > 810:
                        stone.pop(indexStn)
                    else:
                        stn[1] += 2

                    stoneCoreRect = pygame.Rect(stoneCoreimg.get_rect())
                    stoneCoreRect.left = stn[0] + 5
                    stoneCoreRect.top = stn[1] + 5

                    # Check for collision
                    indexMis2 = 0
                    for m4 in missiles:
                        missileCoreRect = pygame.Rect(missileCoreimg.get_rect())
                        missileCoreRect.left = m4[1] + 8
                        missileCoreRect.top = m4[2] + 2
                        if stoneCoreRect.colliderect(missileCoreRect):
                            missiles.pop(indexMis2)
                        indexMis2 += 1

                    if stoneCoreRect.colliderect(userCorePosRect):
                        colliderect01.play()
                        healthvalue -= 20
                        stone.pop(indexStn)

                    for yamt in yamato:
                        yamatoCoreRect = pygame.Rect(yamatoCoreimg.get_rect())
                        yamatoCoreRect.left = yamt[0] + 8
                        yamatoCoreRect.top = yamt[1] + 19
                        if stoneCoreRect.colliderect(yamatoCoreRect):
                            try:
                                colliderect01.play()
                                stone.pop(indexStn)
                            except IndexError:
                                print('Empty the index of Stone and Yamato')

                    indexStn += 1

                for stn in stone:
                    screen.blit(stoneimg, stn)

            # scv repair - start
            if time >= scvTime:
                scvTimer -= 1
                # Draw SCV
                if scvTimer == 0:
                    scv.append([random.randint(10, 1190), 0])
                    scvTimer = 1000 - (scvTimer1 * 2)
                    if scvTimer1 >= 50:
                        scvTimer1 = 50
                    else:
                        scvTimer1 += 5

                indexScv = 0
                for s in scv:
                    if s[1] > 810:
                        scv.pop(indexScv)
                    else:
                        s[1] += 5

                    scvRect = pygame.Rect(scvimg.get_rect())
                    scvRect.left = s[0]
                    scvRect.top = s[1]

                    if scvRect.colliderect(userCorePosRect):
                        repair01.play()
                        if healthvalue + 100 > 484:
                            healthvalue += 484 - healthvalue
                        else:
                            healthvalue += 100
                        scv.pop(indexScv)

                    indexScv += 1

                for s in scv:
                    screen.blit(scvimg, s)
            # scv repair - end

            # ghost - start
            if time >= ghostTime:
                ghostTimer -= 1

                if ghostTimer == 0:
                    ghost.append([random.randint(10, 1190), 0])
                    ghostTimer = 1400 - (ghostTimer1 * 2)
                    if ghostTimer1 >= 50:
                        ghostTimer1 = 50
                    else:
                        ghostTimer1 += 5

                indexGhost = 0
                for gst in ghost:
                    if gst[1] > 810:
                        ghost.pop(indexGhost)
                    else:
                        gst[1] += 5

                    ghostCoreRect = pygame.Rect(ghostCoreimg.get_rect())
                    ghostCoreRect.left = gst[0] + 1
                    ghostCoreRect.top = gst[1]

                    if ghostCoreRect.colliderect(userCorePosRect):
                        nuclearReady.play()
                        ghost.pop(indexGhost)
                        if nuclearCnt == 0:
                            yamatoScreen.append([700, 5])
                            nuclearCnt += 1
                        elif nuclearCnt == 1:
                            yamatoScreen.append([730, 5])
                            nuclearCnt += 1
                        elif nuclearCnt == 2:
                            yamatoScreen.append([760, 5])
                            nuclearCnt += 1

                    indexGhost += 1

                for gst in ghost:
                    screen.blit(ghostimg, gst)
            # ghost - end

            # Draw health bar
            screen.blit(healthbar, (5, 5))
            for health1 in range(healthvalue):
                if healthvalue > 150:
                    screen.blit(health, (health1 + 13, 11))
                else:
                    screen.blit(health_red, (health1 + 13, 11))

            # Display refresh
            pygame.display.flip()

            # game quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                # control
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        keys[0] = True
                    elif event.key == pygame.K_a:
                        keys[1] = True
                    elif event.key == pygame.K_s:
                        keys[2] = True
                    elif event.key == pygame.K_d:
                        keys[3] = True
                    elif event.key == pygame.K_SPACE:
                        if nuclearCnt > 0:
                            yamatosnd.play()
                            for add in range(1, 6):
                                # yamato.append([(add * 100), 900])
                                yamato.append([random.randint(10, 1100), 900])
                            if nuclearCnt == 1:
                                del yamatoScreen[0]
                                nuclearCnt -= 1
                            elif nuclearCnt == 2:
                                del yamatoScreen[1]
                                nuclearCnt -= 1
                            elif nuclearCnt == 3:
                                del yamatoScreen[2]
                                nuclearCnt -= 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        keys[0] = False
                    elif event.key == pygame.K_a:
                        keys[1] = False
                    elif event.key == pygame.K_s:
                        keys[2] = False
                    elif event.key == pygame.K_d:
                        keys[3] = False

                # mouse click and shoot missile - start
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shoot01.play()
                    position = pygame.mouse.get_pos()
                    missiles.append([math.atan2(position[1] - (userPos[1] + 35), position[0] - (userPos[0] + 30)),
                                   userPos2[0] + 35,
                                   userPos2[1] + 35])
                # mouse click and shoot missile - end

            # Move user
            if keys[0]:
                if userPos[1] == 0:
                    pass
                else:
                    userPos[1] -= 10
                    if keys[1]:
                        if userPos[0] == 0:
                            pass
                        else:
                            userPos[0] -= 10
                    elif keys[3]:
                        if userPos[0] == 1200:
                            pass
                        else:
                            userPos[0] += 10
            elif keys[2]:
                if userPos[1] == 800:
                    pass
                else:
                    userPos[1] += 10
                    if keys[1]:
                        if userPos[0] == 0:
                            pass
                        else:
                            userPos[0] -= 10
                    elif keys[3]:
                        if userPos[0] == 1200:
                            pass
                        else:
                            userPos[0] += 10
            elif keys[1]:
                if userPos[0] == 0:
                    pass
                else:
                    userPos[0] -= 10
            elif keys[3]:
                if userPos[0] == 1200:
                    pass
                else:
                    userPos[0] += 10

            # Move userCore
            if keys[0]:
                if userCorePos[1] == -30:
                    pass
                else:
                    userCorePos[1] -= 10
                    if keys[1]:
                        if userCorePos[0] == -30:
                            pass
                        else:
                            userCorePos[0] -= 10
                    elif keys[3]:
                        if userCorePos[0] == 1170:
                            pass
                        else:
                            userCorePos[0] += 10
            elif keys[2]:
                if userCorePos[1] == 770:
                    pass
                else:
                    userCorePos[1] += 10
                    if keys[1]:
                        if userCorePos[0] == -30:
                            pass
                        else:
                            userCorePos[0] -= 10
                    elif keys[3]:
                        if userCorePos[0] == 1170:
                            pass
                        else:
                            userCorePos[0] += 10
            elif keys[1]:
                if userCorePos[0] == -30:
                    pass
                else:
                    userCorePos[0] -= 10
            elif keys[3]:
                if userCorePos[0] == 1170:
                    pass
                else:
                    userCorePos[0] += 10

            # Win/Lose check
            if time >= 180: # sec.
                running = 0
                exitcode = 1
            if healthvalue <= 0:
                running = 0
                exitdcode = 0
        except:
            sys.exit(0)

    if healthvalue < 0:
        lasthealth = 0
    else:
        lasthealth = healthvalue / 484 * 100

    # Win/Lose display
    if exitcode == 0:
        pygame.font.init()
        font = pygame.font.SysFont('arial', 50)
        font2 = pygame.font.SysFont('arial', 200)
        text = font.render('Final health : ' + str(round(lasthealth, 2)) + '%', True, (255, 0, 0))
        text3 = font2.render('You Lose!!', 13, (255, 0, 0))
        text2 = font.render('Regame is SpaceBar of your Keybord.', 13, (255, 255, 255))
        screen.blit(gameover, (0, 0))
        screen.blit(text, (750, 500))
        screen.blit(text2, (400, 700))
        screen.blit(text3, (400, 300))
        pygame.mixer.music.stop()
        pygame.mixer.music.load('resource/bgm_gameover.wav')
        pygame.mixer.music.play(1, 0.0)
        pygame.mixer.music.set_volume(0.5)
    else:
        pygame.font.init()
        font = pygame.font.SysFont('arial', 50)
        font2 = pygame.font.SysFont('arial', 200)
        text = font.render('Final health : ' + str(round(lasthealth, 2)) + '%', True, (29, 219, 22))
        text3 = font2.render('You Win!!', 13, (29, 219, 22))
        text2 = font.render('Regame is SpaceBar of your Keybord.', True, (255, 255, 255))
        screen.blit(youwin, (0, 0))
        screen.blit(text, (750, 500))
        screen.blit(text2, (400, 700))
        screen.blit(text3, (400, 300))
        pygame.mixer.music.stop()
        pygame.mixer.music.load('resource/bgm_win.wav')
        pygame.mixer.music.play(1, 0.0)
        pygame.mixer.music.set_volume(0.25)

    while 1:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        time = 0
                        running = 1
                        break
            if time == 0 and running == 1:
                break
            pygame.display.flip()

        except:
            sys.exit(0)
