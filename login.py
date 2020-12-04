from tkinter import *
import socket
import client_server
import pickle
import join
import random
import os

# 클래스 화 __init__
def login(): # 함수화 시킴

    login_value = "no" # login_value 값을 no로 시작
    with open('game_state', 'wb') as file:
        pickle.dump(login_value, file)

    root = Tk()

    root.title("Nado GUI") # 제목
    root.geometry("640x480") # 가로 x 세로
    root.resizable(0, 0) # 크기 변경 불가
    currunt_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
    image_path = os.path.join(currunt_path, "image")  # inages 폴더 위치 반환  

    # 배경화면 지정
    image = PhotoImage(file= image_path + "\\map\\po.PNG")
    label0 = Label(root, image=image)
    label0.pack()

    # 아이디 Page text
    label10 = Label(root, text="아이디, 비밀번호를 입력하세요.")
    label10.pack()
    label10.place(x=250, y=450) # 위치 지정

    # ID : 
    label1 = Label(root, text = "ID : ") # 라벨 위젯
    label1.pack()
    label1.place(x=200, y=350) # 위치 지정

    # PW : 
    label2 = Label(root, text = "PW : ") # 라벨 위젯
    label2.pack()
    label2.place(x=193, y=370) # 위치 지정

    # ID를 입력하는 입력 박스 세팅
    txt = Entry(root, width=30)
    txt.insert(0, "Enter your ID")
    def clear(event): # 입력박스 클릭 시 지정되어 있는 텍스트 지우기
        if txt.get() == "Enter your ID": # Enter your ID를 초기로 텍스트에 지정
            txt.delete(0, len(txt.get()))
    txt.bind("<Button-1>", clear) # 왼쪽 마우스 클릭 시 텍스트 clear
    txt.pack()
    txt.place(x=230, y=350) # 위치 설정
    txt.insert(0, "")

    # PW를 입력하는 입력 박스 세팅
    e = Entry(root, width=30) # 줄바꿈 X
    e.config(show = "*") # 텍스트 입력 시 *로 처리
    e.pack(pady=3)
    e.place(x=230, y=370) # 위치 지정
    e.insert(0, "")

    # 로그인창 함수 설정
    def client_login():
        # 내용 출력
        id = txt.get() # 로그인 입력박스에 적은 값을 id에 저장
        pwd = e.get() # 비밀번호 입력박스에 적은 값을 pwd에 저장
        # 로그인 조건 코드
        if len(id) < 5 or len(id) > 20:
            # 아이디가 조건에 안 맞을 시 하단 텍스트를 바꿈
            print("아이디는 5~20자 이여야 합니다.")
            finish = "아이디는 5~20자 이여야 합니다."
            label10.config(text=finish)
        elif len(pwd) < 8 or len(pwd) > 16:
            # 비밀번호가 조건에 안 맞을 시 하단 텍스트를 바꿈
            print("비밀번호는 8~16자 이여야 합니다.")
            finish = "비밀번호는 8~16자 이여야 합니다."
            label10.config(text=finish)
        else:
            # 값 서버로 보내기
            print("서버로 값 보내기 실행")
            login_value = client_server.login(id, pwd) # login_value에 client_server의 return값 반환
            # login_value = "ok" or "no"

            # login_value가 ok라면 gam_state 파일을 만들고 그 파일에 ok 값을 넣어줌
            if login_value == "ok":
                with open('game_state', 'wb') as file:
                    pickle.dump(login_value, file)
                root.destroy() # 창 닫기
            # login_value가 no라면
            else:
                finish = "로그인 실패 (다시 시도하세요)."
                label10.config(text=finish)
                # 하단 텍스트를 로그인 실패로 바꿈

    # join.py의 join_main()을 불러옴
    def client_join():
        join.join_main()
    
    # 야생 포켓몬 값 받기 - client_server에서
    # name, HP, ATK = client_server.battle()
    # HP = int(float(HP))
    # ATK = int(float(ATK))
    # print(name, HP, ATK)
    # print(type(name), type(HP), type(ATK))
    # 로그인 버튼
    btn = Button(root, text="로그인", command=client_login) # 로그인 버튼을 클릭 시 client_login 함수 컴파일
    btn.pack()
    btn.place(x=260, y=395) # 위치 지정
    #비밀번호 버튼
    btn1 = Button(root, text="회원가입", command=client_join)# 로그인 버튼을 클릭 시 client_join 함수 컴파일
    btn1.pack()
    btn1.place(x=350, y=395) # 위치 지정
    

    root.mainloop()