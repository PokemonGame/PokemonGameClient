#! /usr/bin/python
# -- coding: utf-8 --
import random
import socket
import pickle


HOST = '192.168.137.65' # 호스트 ip값
PORT = 8888 # 포트 설정
# 로그인 함수
def login(id, pw): # login.py에서 받은 id와 pw 값을 받아옴
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        # server의 while문 바깥으로 login 값 보냄
        state = "login"
        s.send(state.encode(encoding='utf_8', errors='strict'))

        s.recv(100) # ok값 받음

        # server로 id와 pw값 보냄
        s.send(id.encode(encoding='utf_8', errors='strict'))
        print(id)
        s.send(pw.encode(encoding='utf_8', errors='strict'))
        print(pw)
        
        data = s.recv(100) # data에 ok or no를 받아옴

        abc = s.recv(1000) # abc값 받아옴

        data = data.decode() # decode를 이용해 온전한 값으로 변환
        abc = abc.decode() # decode를 이용해 온전한 값으로 변환
        abc = abc.split("(") # abc를 list형태로하여 (단위로 자름

        print('result: ' + data)
        print('sum: ' + abc[0])
        
        
        s.close() # 소켓 닫기
        # abc라는 list형태의 변수에 저장된 값들을 각각 변수에 저장
        pokemonNAME = abc[0]
        MAX_HP = abc[2]
        MONEY = abc[6]
        HP = abc[1]
        EXPERIENCE = abc[4]
        ITEM = abc[5]
        ATK = abc[3]
        user_id = abc[7]

        print('pokemonNAME: ' + pokemonNAME)
        print('MAX_IP: ' + MAX_HP)
        print('MONEY: ' + MONEY)
        print('HP: ' + HP)
        print('EXPERIENCE: ' + EXPERIENCE)
        print('ITEM: ' + ITEM)
        print('ATK: ' + ATK)
        print('user_id: ' + user_id)

        # user_info 파일을 만들고 그 파일에 포켓몬 정보 값들을 넣어줌
        with open('user_info', 'wb') as file:
            pickle.dump(pokemonNAME, file)
            pickle.dump(HP, file)
            pickle.dump(MAX_HP, file)
            pickle.dump(ATK, file)
            pickle.dump(EXPERIENCE, file)
            pickle.dump(ITEM, file)
            pickle.dump(MONEY, file)
            pickle.dump(user_id, file)
        # return data.decode(), pokemonNAME.decode(), MONEY.decode(), HP.decode(), EXPERIENCE.decode(), ITEM.decode(), AT.decode()

        return data

    except:
        print("error")
# 회원가입 함수
def join(id, pw):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        # server의 while문 바깥으로 join 값 보냄
        state = "join"
        s.send(state.encode(encoding='utf_8', errors='strict'))

        s.recv(1024) # data에 ok or no를 받아옴

        # server로 id와 pw값 보냄
        s.send(id.encode(encoding='utf_8', errors='strict'))
        s.send(pw.encode(encoding='utf_8', errors='strict'))

        data = s.recv(1024) # ok 또는 no 값을 받아옴 - server.py에서
        print ('result: ' + data.decode())

        s.close()

        return data.decode()

    except:
        print("error")
# 야생 포켓몬 배틀 함수
def battle():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        # server의 while문 바깥으로 battle 값 보냄
        state = "battle"
        s.send(state.encode(encoding='utf_8', errors='strict'))

        s.recv(2) # data에 ok or no를 받아옴

        print('ok받음')
        # 야생 포켓몬 값 받기 - server에서
        name = s.recv(100) # name에 server에서 보낸 name값 받기
        s.send(state.encode(encoding='utf_8', errors='strict')) # byte단위로 분류하면 0번 방에 값이 다 들어가기 때문에 지정
        HP = s.recv(100) # HP에 server에서 보낸 HP값 받기
        s.send(state.encode(encoding='utf_8', errors='strict'))
        ATK = s.recv(100) # ATK에 server에서 보낸 ATK값 받기
        s.close()
        
        return name.decode(), HP.decode(), ATK.decode()

    except:
        print("error")
# 저장 함수
def save():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))

        state = "save"
        s.send(state.encode(encoding='utf_8', errors='strict'))

        s.recv(1024) # data에 ok를 받아옴
        # user_info의 파일 값을 읽어옴 - 읽어온 값들을 각각 변수에 저장
        with open('user_info', 'rb') as file:
            pokemonNAME = pickle.load(file)
            MAX_HP = pickle.load(file)
            MONEY = pickle.load(file)
            HP = pickle.load(file)
            EXPERIENCE = pickle.load(file)
            ITEM = pickle.load(file)
            ATK = pickle.load(file)
            user_id = pickle.load(file)

        # 받아온 값들을 문자열로 변환
        MAX_HP = str(MAX_HP)
        MONEY = str(MONEY)
        HP = str(HP)
        EXPERIENCE = str(EXPERIENCE)
        ITEM = str(ITEM)
        ATK = str(ATK)
        # sum_info라는 변수에 받아온 포켓몬 회원 정보들을 하나의 변수로 저장 - (를 쓴 이유 : split 조건을 만들기 위해서
        sum_info = pokemonNAME+"("+HP+"("+MAX_HP+"("+ATK+"("+EXPERIENCE+"("+ITEM+"("+MONEY+"("+user_id
        

        print("type:",type(sum_info))
        # sever로 sum_info값 전달
        s.send(sum_info.encode(encoding='utf_8', errors='strict'))
        
        s.close()
        
        # return pokemonNAME.decode(), MAX_HP.decode(), MONEY.decode(), HP.decode(),
        # EXPERIENCE.decode(), ITEM.decode(), ATK.decode()

    except:
        print("error")