import pygame
import os
from random import *
import pickle
import battle
import client_server
walkcount = 0

def work():
    ###########################################################################################

    # 기본 초기화 (반드시 해야 하는 것들)
    pygame.init()

    # 화면 크기 설정
    screen_width = 900  # 가로 크기
    screen_height = 600  # 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 화면 타이틀 설정
    pygame.display.set_caption("")

    # FPS
    clock = pygame.time.Clock()
    ###########################################################################################

    # bgm 실행
    pygame.mixer.music.load( "image/bgm/playgame.mp3" )
    pygame.mixer.music.play(-1)

    # 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
    currunt_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
    image_path = os.path.join(currunt_path, "image")  # inages 폴더 위치 반환

    # 배경 만들기
    background = pygame.image.load(
        os.path.join(image_path, "map\\background.PNG"))

    # 캐릭터 아래 이동 이미지
    character_down = [
        pygame.image.load(os.path.join(image_path, "character/down1.png")),
        pygame.image.load(os.path.join(image_path, "character/down2.png")),
        pygame.image.load(os.path.join(image_path, "character/down3.png")),
        pygame.image.load(os.path.join(image_path, "character/down4.png"))]

    # 캐릭터 위 이동 이미지
    character_up = [
        pygame.image.load(os.path.join(image_path, "character/up1.png")),
        pygame.image.load(os.path.join(image_path, "character/up2.png")),
        pygame.image.load(os.path.join(image_path, "character/up3.png")),
        pygame.image.load(os.path.join(image_path, "character/up4.png"))]

    # 캐릭터 왼쪽 이동 이미지
    character_left = [
        pygame.image.load(os.path.join(image_path, "character/left1.png")),
        pygame.image.load(os.path.join(image_path, "character/left2.png")),
        pygame.image.load(os.path.join(image_path, "character/left3.png")),
        pygame.image.load(os.path.join(image_path, "character/left4.png"))]

    # 캐릭터 오른쪽 이동 이미지
    character_right = [
        pygame.image.load(os.path.join(image_path, "character/right1.png")),
        pygame.image.load(os.path.join(image_path, "character/right2.png")),
        pygame.image.load(os.path.join(image_path, "character/right3.png")),
        pygame.image.load(os.path.join(image_path, "character/right4.png"))]

    # 포션의 이미지 경로
    posion = pygame.image.load(os.path.join(image_path, "posion/pokemon_posion.png"))

    # 캐릭터의 사이즈 구하기 (대표 이미지 1개만)
    character_size = character_right[1].get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]

    # 캐릭터 이동속도
    character_speed = 10
    # 캐릭터의 좌표
    x = 450
    y = 600 - character_height

    # 누르고 있는 키의 값을 True로 하여 값이 True이면 이미지를 계속 변경
    left = False
    right = False
    up = False
    down = False

    # 한 방향의 이미지 4개를 4번씩 총 16번의 이미지를 보여준다
    # 카운트를 세면서 이미지를 바꿔준다
    #walkcount = 0
    # 캐릭터가 멈췄을 때 바라보는 방향
    stopd = "up"

    # 전역변수를 사용하기 위한 초기화 
    my_pokemon_name = "1"
    my_pokemon_hp = 0
    my_pokemon_hp_full = 0 
    my_pokemon_atk = 0
    my_pokemon_lv = 0
    my_pokemon_item = 0
    my_pokemon_money = 0
    my_pokemon_user_id = "1" 
    

    # 이동시 캐릭터 이미지 변화 함수
    def redrawG():
        global walkcount, my_pokemon_name, my_pokemon_hp, my_pokemon_hp_full, my_pokemon_atk, my_pokemon_lv, my_pokemon_item, my_pokemon_money, my_pokemon_user_id
        
        
        if walkcount >= 16:
            walkcount = 0
        # walk right
        if right:
            # count를 4로 나눠 몫의 값으로 배열이미지 0,1,2,3 출력
            screen.blit(character_right[walkcount//4], (x, y))
            walkcount += 1
        #walk left
        elif left:
            screen.blit(character_left[walkcount//4], (x, y))
            walkcount += 1
        # walk up
        elif up:
            screen.blit(character_up[walkcount//4], (x, y))
            walkcount += 1
        # walk down
        elif down:
            screen.blit(character_down[walkcount//4], (x, y))
            walkcount += 1
        else:
            # 오른쪽을 바라보다가 멈췄을 경우 오른쪽을 보며 서있는 이미지를 변수에 저장
            if stopd == "right":
                stop = pygame.image.load(os.path.join(
                    image_path, "character/right1.png"))
            elif stopd == "left":
                stop = pygame.image.load(os.path.join(
                    image_path, "character/left1.png"))
            elif stopd == "down":
                stop = pygame.image.load(os.path.join(
                    image_path, "character/down1.png"))
            elif stopd == "up":
                stop = pygame.image.load(os.path.join(
                    image_path, "character/up1.png"))

            screen.blit(stop, (x, y))
            pass
        pygame.display.update()

    # 파일을 읽어서 변수에 값을 저장한다
    with open('user_info', 'rb') as file:   
        my_pokemon_name = pickle.load(file)
        my_pokemon_hp = pickle.load(file)
        my_pokemon_hp_full = pickle.load(file)
        my_pokemon_atk = pickle.load(file)
        my_pokemon_lv = pickle.load(file)
        my_pokemon_item = pickle.load(file)
        my_pokemon_money = pickle.load(file)
        my_pokemon_user_id = pickle.load(file)

    # 회면에 띄워지는 포션과 돈의 양의 폰트
    textFont = pygame.font.SysFont( "나눔고딕", 20, True, False)
    BLACK = ( 0, 0, 0 )

    running = True
    while running:
        clock.tick(24)

        #화면에 바탕과 포션 개수 보유 돈을 띄운다
        screen.blit(background, (0, 0))
        text_Title= textFont.render("포션 개수: " + str(my_pokemon_item) + ", 보유 돈: " + str(my_pokemon_money), True, BLACK)
        screen.blit(text_Title, [20, 560])
        pygame.display.update()

        for event in pygame.event.get():
            # 나가기 버튼시 나가진다
            if event.type == pygame.QUIT:
                running = False
            # 이미지의 집에 들어가서 마우스를 클릭시 포션 구매
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 560< x < 789 and 211 < y < 330:
                    my_pokemon_money = int(my_pokemon_money)
                    my_pokemon_item = int(my_pokemon_item)
                    if my_pokemon_money >= 200:
                        my_pokemon_money -= 200
                        my_pokemon_item += 1 

                    # 포션 구매 시 파일에 유저 정보 저장
                    with open('user_info', 'wb') as file:
                        pickle.dump(my_pokemon_name, file)
                        pickle.dump(my_pokemon_hp, file)
                        pickle.dump(my_pokemon_hp_full, file)
                        pickle.dump(my_pokemon_atk, file)
                        pickle.dump(my_pokemon_lv, file)
                        pickle.dump(my_pokemon_item, file)
                        pickle.dump(my_pokemon_money, file)
                        pickle.dump(my_pokemon_user_id, file)

            if event.type == pygame.KEYUP:
                if right:
                    right = False
                    stopd = "right"
                if left:
                    left = False
                    stopd = "left"
                if down:
                    down = False
                    stopd = "down"
                if up:
                    up = False
                    stopd = "up"
                pass
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if x > screen_width - character_width:
                x = screen_width - character_width
            x += character_speed
            right = True
            left = False
        elif keys[pygame.K_LEFT]:
            if x < 0:
                x = 0
            x -= character_speed
            right = False
            left = True
        elif keys[pygame.K_DOWN]:
            if y > screen_height - character_height:
                y = screen_height - character_height
            y += character_speed
            down = True
            up = False
        elif keys[pygame.K_UP]:
            # 맵 위에 있는 나무의 크기 60px
            if y < 60:
                y = 60
            y -= character_speed
            down = False
            up = True
        elif keys[pygame.K_p]:
            print("save버튼 누름")
            client_server.save()
        
        # 플레이어가 풀숲에 들어갔을 시 2%의 확률로 배틀 시작
        if (-20 < x < 260 and 0 < y < 360) or (560 < x < 900 and 0 < y < 210) or (790 < x < 900 and 0 < y < 330) or (530 < x < 900 and 500 < y < 600): # 왼쪽 위 풀
            i = randint(1, 50) # i = 5 ~ 50번 사이의 랜덤 숫자를 저장
            if i == 5:
                battle.mainmenu()
                
                # 배틀 끝나고 화면에 띄우는 아이템개수와 돈을 위해 다시 읽어 온다
                with open('user_info', 'rb') as file:   
                    pickle.load(file)
                    pickle.load(file)
                    pickle.load(file)
                    pickle.load(file)
                    pickle.load(file)
                    my_pokemon_item = pickle.load(file)
                    my_pokemon_money = pickle.load(file)

        # 플레이어가 집위에 있다면 화면에 포션구매 이미지 띄우기
        if  560< x < 789 and 211 < y < 330:
            screen.blit(posion, (330, 150))

        redrawG()

    pygame.quit()