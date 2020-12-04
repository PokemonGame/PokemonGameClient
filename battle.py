import pygame
import os
import time
import pickle
import random
import client_server
import playgame

# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
currunt_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
image_path = os.path.join(currunt_path, "image")  # inages 폴더 위치 반환
# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "battle\\background.PNG"))
# 버튼 만들기
btn1 = pygame.image.load(os.path.join(image_path, "battle\\공격.png"))
btn1_2 = pygame.image.load(os.path.join(image_path, "battle\\공격2.png"))
btn2 = pygame.image.load(os.path.join(image_path, "battle\\스킬.png"))
btn2_2 = pygame.image.load(os.path.join(image_path, "battle\\스킬2.png"))
btn3 = pygame.image.load(os.path.join(image_path, "battle\\회복.png"))
btn3_2 = pygame.image.load(os.path.join(image_path, "battle\\회복2.png"))
btn4 = pygame.image.load(os.path.join(image_path, "battle\\도망.png"))
btn4_2 = pygame.image.load(os.path.join(image_path, "battle\\도망2.png"))

# 폰트 설정
textFont = pygame.font.SysFont( "나눔고딕", 25, True, False)
BLACK = ( 0, 0, 0 )
infoFont = pygame.font.SysFont( "나눔고딕", 20, True, False)

# 서버에서 받은 포켓몬 영어 이름을 한글로 반환해주는 함수
def pokemon_name(x):
    return {"isanghaessi" : "이상해씨", "pairi" : "파이리","kkobugi" : "꼬부기","pikachu" : "피카츄","gugu" : "구구","kkoret" : "꼬렛","minyong" : "미뇽","geunyukmon" : "근육몬",
            "gyaradoseu" : "갸라도스", "koppuri" : "코뿌리", "konchi" : "콘치", "ttogaseu" : "또가스", "tangguri" : "탕구리", "kingkeuraep" : "킹크랩",
            "rongseuton" : "롱스톤", "koil" : "코일", "yadon" : "야돈", "yadoran" : "야돈", "ponita" : "포니타", "kkomadol" : "꼬마돌", "modapi" : "모다피",
            "gangchaengi" : "강챙이", "gadi" : "가디", "nyaong" : "냐옹", "digeuda" : "디그다","jubet" : "쥬뱃","ibeui" : "이브이"}.get(x, "피카츄")

# 전역변수를 위한 변수 초기화
name = "?"
hp = 999
hp_full = 999
atk = 100
lv = 0
item = 5
money = 1000
user_id = "abc"

my_pokemon_name = "피카츄"
my_pokemon_hp = 999
my_pokemon_hp_full = 999
my_pokemon_atk = 100
my_pokemon_lv = 0
my_pokemon_item = 5
my_pokemon_money = 1000
my_pokemon_id = "abc"
my_pokemon_image = pygame.image.load(os.path.join(image_path, "pokemon\\" + my_pokemon_name +".png"))
my_pokemon_pos = [80, 230]

wild_pokemon_lv = 2
wild_pokemon_hp_full = 100
wild_pokemon_hp = wild_pokemon_hp_full
wild_pokemon_atk = 10
wild_pokemon_name = pokemon_name("gugu")
wild_pokemon_image = pygame.image.load(os.path.join(image_path, "pokemon\\" + wild_pokemon_name +".png"))
wild_pokemon_pos = [670, 20]




# 메인 실행 함수
def mainmenu():
    ###########################################################################################
    # 화면 크기 설정
    screen_width = 900  # 가로 크기
    screen_height = 600  # 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))
    # 화면 타이틀 설정
    pygame.display.set_caption("Battle")
    # FPS
    clock = pygame.time.Clock()
    ###########################################################################################

    global lv, atk
    # 값 꺼내기
    with open('user_info', 'rb') as file:   
        name = pickle.load(file)
        hp = pickle.load(file)
        hp_full = pickle.load(file)
        atk = int(pickle.load(file))
        lv = int(pickle.load(file))
        item = pickle.load(file)
        money = pickle.load(file)
        user_id = pickle.load(file)

    global my_pokemon_name, my_pokemon_hp, my_pokemon_hp_full, my_pokemon_atk, my_pokemon_lv, my_pokemon_item, my_pokemon_money ,my_pokemon_id
    my_pokemon_name = pokemon_name(name)
    my_pokemon_hp = int(hp)
    my_pokemon_hp_full = int(hp_full)
    my_pokemon_atk = int(atk)
    my_pokemon_lv = (lv // 100) + 1
    my_pokemon_item = int(item)
    my_pokemon_money = int(money)
    my_pokemon_id = user_id
    my_pokemon_image = pygame.image.load(os.path.join(image_path, "pokemon\\" + my_pokemon_name +".png"))


    global wild_pokemon_lv, wild_pokemon_hp_full, wild_pokemon_hp, wild_pokemon_atk, wild_pokemon_name, wild_pokemon_image
    # 서버에서 야생포켓몬의 정보 값 받기
    wild_name, hp, atk = client_server.battle()
    hp = int(float(hp))
    atk = int(float(atk))
    wild_pokemon_lv = random.randint(my_pokemon_lv - 2, my_pokemon_lv + 2)
    if my_pokemon_lv < 4 : 
        wild_pokemon_lv = random.randint(my_pokemon_lv - 1, my_pokemon_lv + 1)
    if wild_pokemon_lv < 1:
        wild_pokemon_lv = 1
    wild_pokemon_hp_full = hp + ((wild_pokemon_lv-1) * random.randint(20, 30))
    wild_pokemon_hp = wild_pokemon_hp_full
    wild_pokemon_atk = atk + ((wild_pokemon_lv-1) * random.randint(5, 8))
    wild_pokemon_name = pokemon_name(wild_name)
    wild_pokemon_image = pygame.image.load(os.path.join(image_path, "pokemon\\" + wild_pokemon_name +".png"))
    
    # bgm 실행
    pygame.mixer.music.load( "image/bgm/battle.mp3" )
    pygame.mixer.music.play(-1)


    # 버튼위에 마우스가 있으면 이미지 변경 없으면 다시 변경
    # 클릭시 각각의 함수를 실행하는 객체
    class Button:
        def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
            mouse = pygame.mouse.get_pos() # 마우스 좌표 저장
            click = pygame.mouse.get_pressed() # 클릭시
            if x + width > mouse[0] > x and y + height > mouse[1] > y: # 이미지 안에 있으면
                screen.blit(img_act, (x_act, y_act)) # 클릭 이미지 로드
                if click[0] and action != None:
                    action()        # 지정 함수 호출
            else:
                screen.blit(img_in, (x,y)) # 마우스가 이미지 바깥이면 일반 이미지 로드

    # 공격 버튼 클릭시 실행 함수
    def attack():
        
        def attack_turn(attack_pokemon_name, hit_pokemon, attack_pokemon_atk):
            pokemon_screen_update()
            pygame.display.update()

            global my_pokemon_hp, wild_pokemon_hp, lv, my_pokemon_money, my_pokemon_lv, my_pokemon_hp_full, my_pokemon_atk, lv

            # 플레이어의 공격 텍스트를 띄운다
            text_screen_update(attack_pokemon_name + "의 공격!")

            # 맞는 포켓몬이 내 포켓몬
            if hit_pokemon == "my":
                
                my_pokemon_hp -= attack_pokemon_atk
                
                # 내 포켓몬의 체력이 0이면 
                if my_pokemon_hp <= 0:
                    my_pokemon_hp = 0
                    pokemon_screen_update()
                    text_screen_update(my_pokemon_name + "는(은) 쓰러졌다.")

                    pokemon_screen_update()
                    text_screen_update("플레이어는 배틀에서 패배했다...")

                    # 파일에 유저 정보 저장
                    with open('user_info', 'wb') as file:
                        pickle.dump(name, file)
                        pickle.dump(1, file)
                        pickle.dump(my_pokemon_hp_full, file)
                        pickle.dump(my_pokemon_atk, file)
                        pickle.dump(lv, file)
                        pickle.dump(my_pokemon_item, file)
                        pickle.dump(money, file)
                        pickle.dump(user_id, file)

                    playgame.work()

            # 맞는 포켓몬이 야생 포켓몬일 때
            elif hit_pokemon == "wild":
         
                wild_pokemon_hp -= attack_pokemon_atk

                # 야생포켓몬의 체력이 0이면 
                if wild_pokemon_hp <= 0:
                    wild_pokemon_hp = 0

                    # 100~300 랜덤 돈 저장
                    random_money = random.randint(100, 300)
                    # 40~70 랜덤 경험치 저장
                    random_lv = random.randint(40, 70)

                    pokemon_screen_update()
                    text_screen_update("플레이어는 배틀에서 승리했다!")

                    # 변수에 랜덤한 값을 각각 저장
                    lv += random_lv
                    my_pokemon_money += random_money

                    pokemon_screen_update()
                    text_screen_update(attack_pokemon_name + "는(은) "+ str(random_lv)  +"의 경험치를 얻었다!")
                    
                   # 레벨업 시
                    if my_pokemon_lv < (lv // 100) + 1:
                        hp_full_plus = random.randint(20, 30)
                        atk_plus = random.randint(5, 8)
                        my_pokemon_hp_full += hp_full_plus
                        my_pokemon_atk += atk_plus
                        my_pokemon_hp = my_pokemon_hp_full
                        my_pokemon_lv += 1

                        pokemon_screen_update()
                        text_screen_update("레벨업!")

                        pokemon_screen_update()
                        text_screen_update(str(hp_full_plus) + "의 체력과 " + str(atk_plus) + "의 공격력이 증가했다!")

                    pokemon_screen_update()
                    text_screen_update("플레이어는 " + str(random_money) + "의 돈을 얻었다!")

                    # 파일에 유저 정보 저장
                    with open('user_info', 'wb') as file:
                        pickle.dump(name, file)
                        pickle.dump(my_pokemon_hp, file)
                        pickle.dump(my_pokemon_hp_full, file)
                        pickle.dump(my_pokemon_atk, file)
                        pickle.dump(lv, file)
                        pickle.dump(my_pokemon_item, file)
                        pickle.dump(my_pokemon_money, file)
                        pickle.dump(user_id, file)

                    # 바로 종료
                    #pygame.quit()
                    playgame.work()

            pokemon_screen_update()
            pygame.display.update()

            if hit_pokemon == "my":
                text_screen_update(str(attack_pokemon_atk) + "의 피해를 받았다.")
            elif hit_pokemon == "wild":
                text_screen_update(str(attack_pokemon_atk) + "의 피해를 줬다.")

        attack_turn(my_pokemon_name, "wild", my_pokemon_atk)
        attack_turn(wild_pokemon_name, "my", wild_pokemon_atk)

    # 스킬 버튼 클릭시 실행 함수
    def skill():
        # 1~3 을 랜덤으로 돌려 66% 확률로 스킬 시전 성공
        skill_random = random.randint(1,3)

        def attack_turn(attack_pokemon_name, hit_pokemon, attack_pokemon_atk):
            pokemon_screen_update()
            pygame.display.update()

            global my_pokemon_hp, wild_pokemon_hp, lv, my_pokemon_money, my_pokemon_lv, my_pokemon_hp_full, my_pokemon_atk, lv

            # 맞는 포켓몬이 내 포켓몬
            if hit_pokemon == "my":
                text_screen_update(attack_pokemon_name + "의 공격!")
                my_pokemon_hp -= attack_pokemon_atk

                # 내 포켓몬의 체력이 0이면 
                if my_pokemon_hp <= 0:
                    my_pokemon_hp = 0
                    pokemon_screen_update()
                    text_screen_update(my_pokemon_name + "는(은) 쓰러졌다.")

                    pokemon_screen_update()
                    text_screen_update("플레이어는 배틀에서 패배했다...")

                    # 파일에 유저 정보 저장
                    with open('user_info', 'wb') as file:
                        pickle.dump(name, file)
                        pickle.dump(1, file)
                        pickle.dump(my_pokemon_hp_full, file)
                        pickle.dump(my_pokemon_atk, file)
                        pickle.dump(lv, file)
                        pickle.dump(my_pokemon_item, file)
                        pickle.dump(money, file)
                        pickle.dump(user_id, file)

                    playgame.work()
            # 맞는 포켓몬이 야생 포켓몬이고 스킬 시전에 성공 시
            elif hit_pokemon == "wild" and skill_random != 2:
                text_screen_update(attack_pokemon_name + "의 스킬 시전!")
                wild_pokemon_hp -= attack_pokemon_atk * 2

                if wild_pokemon_hp <= 0:
                    wild_pokemon_hp = 0

                    random_money = random.randint(100, 300)
                    random_lv = random.randint(40, 70)

                    pokemon_screen_update()
                    text_screen_update("플레이어는 배틀에서 승리했다!")

                    lv += random_lv
                    my_pokemon_money += random_money

                    pokemon_screen_update()
                    text_screen_update(attack_pokemon_name + "는(은) "+ str(random_lv)  +"의 경험치를 얻었다!")
                    
                    if my_pokemon_lv < (lv // 100) + 1:
                        hp_full_plus = random.randint(20, 30)
                        atk_plus = random.randint(5, 8)
                        my_pokemon_hp_full += hp_full_plus
                        my_pokemon_atk += atk_plus
                        my_pokemon_hp = my_pokemon_hp_full
                        my_pokemon_lv += 1

                        pokemon_screen_update()
                        text_screen_update("레벨업!")

                        pokemon_screen_update()
                        text_screen_update(str(hp_full_plus) + "의 체력과 " + str(atk_plus) + "의 공격력이 증가했다!")

                    pokemon_screen_update()
                    text_screen_update("플레이어는 " + str(random_money) + "의 돈을 얻었다!")

                    # 파일에 유저 정보 저장
                    with open('user_info', 'wb') as file:
                        pickle.dump(name, file)
                        pickle.dump(my_pokemon_hp, file)
                        pickle.dump(my_pokemon_hp_full, file)
                        pickle.dump(my_pokemon_atk, file)
                        pickle.dump(lv, file)
                        pickle.dump(my_pokemon_item, file)
                        pickle.dump(my_pokemon_money, file)
                        pickle.dump(user_id, file)

                    playgame.work()
            # 스킬 시전에 실패 했을 시
            else:
                text_screen_update(attack_pokemon_name + "의 스킬 시전!")
                pokemon_screen_update()
                pygame.display.update()
                text_screen_update(attack_pokemon_name + "은 스킬시전에 실패했다..")

            pokemon_screen_update()
            pygame.display.update()

            # 내가 받고 준 피해를 출력
            if hit_pokemon == "my":
                text_screen_update(str(attack_pokemon_atk) + "의 피해를 받았다.")
            elif hit_pokemon == "wild" and skill_random != 2:
                text_screen_update(str(attack_pokemon_atk * 2) + "의 피해를 줬다.")
            else:
                pass
            
        # 공격하는 포켓몬의 이름, 피격 당하는 포켓몬, 공격하는 포켓몬의 공격력을 보낸다
        attack_turn(my_pokemon_name, "wild", my_pokemon_atk)
        attack_turn(wild_pokemon_name, "my", wild_pokemon_atk)

    # 포션 버튼 클릭시 실행 함수
    def posion():
        global my_pokemon_item, my_pokemon_hp, my_pokemon_hp_full

        pokemon_screen_update()
        if my_pokemon_item < 1:
            text_screen_update("포션이 없다..")
        else:
            my_pokemon_item -= 1
            # 회복은 최대 체력의 30%이다
            heal = int((my_pokemon_hp_full / 10) * 3)
            if my_pokemon_hp + heal > my_pokemon_hp_full:
                heal = my_pokemon_hp_full - my_pokemon_hp

            my_pokemon_hp += heal 

            text_screen_update(str(heal) + "만큼 회복했다.")


    # 도망 버튼 클릭시 실행 함수
    def escape():
        # 화면에 배경, 포켓몬 띄우기
        pokemon_screen_update()

        # 텍스트를 화면에 띄우는 함수
        text_screen_update("성공적으로 도망쳤다!")

        # 파일에 유저 정보 저장
        with open('user_info', 'wb') as file:
            pickle.dump(name, file)
            pickle.dump(my_pokemon_hp, file)
            pickle.dump(hp_full, file)
            pickle.dump(my_pokemon_atk, file)
            pickle.dump(lv, file)
            pickle.dump(my_pokemon_item, file)
            pickle.dump(money, file)
            pickle.dump(user_id, file)

        # 종료
        #pygame.quit()
        playgame.work()

    def text_screen_update(text):
        text_Title= textFont.render(text, True, BLACK)
        screen.blit(text_Title, [50, 455])
        pygame.display.update()
        Wait_seconds(2)

    # 배경, 포켓몬을 화면에 띄우는 함수
    def pokemon_screen_update():
        # 배경 띄우기
        screen.blit(background, (0, 0))

        # 변수 선언
        exp = int(lv) % 100

        # 야생포켓몬 정보 띄우기
        screen.blit(wild_pokemon_image, wild_pokemon_pos)
        wild_pokemon_name_text = infoFont.render(wild_pokemon_name + " Lv: " + str(wild_pokemon_lv), True, BLACK)
        screen.blit(wild_pokemon_name_text, [100, 60])
        wild_pokemon_hp_text = infoFont.render("HP : " + str(wild_pokemon_hp) + " / " + str(wild_pokemon_hp_full), True, BLACK)
        screen.blit(wild_pokemon_hp_text, [100, 100])
        wild_pokemon_atk_text = infoFont.render("ATK : " + str(wild_pokemon_atk), True, BLACK)
        screen.blit(wild_pokemon_atk_text, [300, 100])

        # 내 포켓몬 띄우기
        screen.blit(my_pokemon_image, my_pokemon_pos)
        my_pokemon_name_text = infoFont.render(my_pokemon_name + " Lv: " + str(my_pokemon_lv) + "          exp: " + str(exp) + " / 100" , True, BLACK)
        screen.blit(my_pokemon_name_text, [500, 325])
        my_pokemon_hp_text = infoFont.render("HP : " + str(my_pokemon_hp) + " / " + str(my_pokemon_hp_full), True, BLACK)
        screen.blit(my_pokemon_hp_text, [500, 365])
        my_pokemon_atk_text = infoFont.render("ATK : " + str(my_pokemon_atk), True, BLACK)
        screen.blit(my_pokemon_atk_text, [700, 365])

    # 시간 대기하기 위한 함수
    def Wait_seconds(second):
        # 함수를 실행한 당시의 시간을 가져옴
        time = pygame.time.get_ticks()

        # 매개변수로 받은 초만큼 대기하기 위해 함수를 실행한 시간이 매개변수로 받은 초만큼이 되기 전까지 돌린다
        while pygame.time.get_ticks() - time <= second * 1000 :
            continue

    text_turn = 1

    menu = True
    while menu:
        clock.tick(15)
        # 실행하고 지난 시간을 가져옴
        times = pygame.time.get_ticks()
        # 오른쪽 위 X 버튼 클릭 시 끝내기 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # 실행하고 3초동안 1번째 메세지 출력 (1초는 실행시간으로 더함)
        if text_turn == 1:
            # 배경 띄우기
            screen.blit(background, (0, 0))
            # 야생포켓몬 정보 띄우기
            screen.blit(wild_pokemon_image, wild_pokemon_pos)
            wild_pokemon_name_text = infoFont.render(wild_pokemon_name + " Lv: " + str(wild_pokemon_lv), True, BLACK)
            screen.blit(wild_pokemon_name_text, [100, 60])
            wild_pokemon_hp_text = infoFont.render("HP : " + str(wild_pokemon_hp) + " / " + str(wild_pokemon_hp_full), True, BLACK)
            screen.blit(wild_pokemon_hp_text, [100, 100])
            wild_pokemon_atk_text = infoFont.render("ATK : " + str(wild_pokemon_atk), True, BLACK)
            screen.blit(wild_pokemon_atk_text, [300, 100])
            text_Title= textFont.render("야생의 "+ wild_pokemon_name +"가(이) 나타났다.", True, BLACK)
            screen.blit(text_Title, [50, 455])
            text_turn = 2
            Wait_seconds(3)
            
            
        # 실행하고 4초가 지나면 2번째 메세지 출력
        elif text_turn == 2:
            # 화면에 배경, 포켓몬 띄우기
            pokemon_screen_update()
            text_Title= textFont.render("가랏! "+ my_pokemon_name + "!", True, BLACK)
            screen.blit(text_Title, [50, 455])
            text_turn = 3
            Wait_seconds(3)
            
        elif text_turn == 3:
            # 화면에 배경, 포켓몬 띄우기
            pokemon_screen_update()
            text_Title= textFont.render(my_pokemon_name + "는(은) 무엇을 할까?", True, BLACK)
            screen.blit(text_Title, [50, 455])
            
            # 각각 클래스 객체로 (이미지1, x, y, width, height, 이미지2, x, y, 실행함수) 를 보낸다
            # 버튼은 기본적인 텍스트가 끝난 후 표시
            attack_Button = Button(btn1,630,455,91,31,btn1_2,630,455,attack)
            skill_Button = Button(btn2,750,455,91,31,btn2_2,750,455,skill)
            posion_Button = Button(btn3,630,520,91,31,btn3_2,630,520,posion)
            escape_Button = Button(btn4,750,520,91,31,btn4_2,750,520,escape)
        # 화면 업데이트
        pygame.display.update()