#! /usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import client_server
import random
import os


def join_main():

    root = Toplevel()
    root.title("JOIN") # 제목
    root.geometry("640x480") # 가로 x 세로
    root.resizable(0, 0) # 크기 변경 불가
    currunt_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
    image_path = os.path.join(currunt_path, "image")  # inages 폴더 위치 반환  

    # 배경화면 지정
    image = PhotoImage(file= image_path + "\\map\\po.PNG")
    label110 = Label(root, image=image)
    label110.pack()

    # 비밀번호 Page text
    label1 = Label(root, text="아이디:5~20자, 비밀번호:8~16자")
    label1.pack()
    label1.place(x=236, y=450 )# 위치 지정

    # ID :
    label11 = Label(root, text = "ID : ") # 라벨 위젯
    label11.pack()
    label11.place(x=200, y=350) # 위치 지정

    # PW :
    label12 = Label(root, text = "PW : ") # 라벨 위젯
    label12.pack()
    label12.place(x=193, y=370) # 위치 지정

    # PW OK :
    label13 = Label(root, text = "PW OK : ") # 라벨 위젯
    label13.pack()
    label13.place(x=172, y=390) # 위치 지정

    # ID를 입력하는 입력 박스 세팅
    txt1 = Entry(root, width=30)
    txt1.pack()
    txt1.place(x=230, y=350) # 위치 지정
    txt1.insert(0, "")

    # PW를 입력하는 입력 박스 세팅
    e2 = Entry(root, width=30) # 줄바꿈 X
    e2.pack(pady=3)
    e2.place(x=230, y=370) # 위치 지정
    e2.insert(0, "")

    # PW OK를 입력하는 입력 박스 세팅
    e3 = Entry(root, width=30) # 줄바꿈 X
    e3.pack(pady=3)
    e3.place(x=230, y=390) # 위치 지정
    e3.insert(0, "")

    # 회원가입창 함수 설정
    def a_join():
        id = txt1.get() # 로그인 입력박스에 적은 값을 id에 저장
        pwd = e2.get() # 비밀번호 입력박스에 적은 값을 pwd에 저장
        pwd_ok = e3.get() # 비밀번호 확인 입력박스에 적은 값을 pwd_ok에 저장
        
        if len(id) < 5 or len(id) > 20:
            # 아이디가 조건에 안 맞을 시 하단 텍스트를 바꿈
            print("아이디는 5~20자 이여야 합니다.")
            label1.config(text="아이디는 5~20자 이여야 합니다.")
        elif len(pwd) < 8 or len(pwd) > 16:
            # 비밀번호가 조건에 안 맞을 시 하단 텍스트를 바꿈
            print("비밀번호는 8~16자 이여야 합니다.")
            label1.config(text="비밀번호는 8~16자 이여야 합니다.")
        elif pwd != pwd_ok:
            # 비밀번호 확인이 조건에 안 맞을 시 하단 텍스트를 바꿈
            print("비밀번호가 동일하지 않습니다.")
            label1.config(text="비밀번호가 동일하지 않습니다.")
        else:
            # 값 서버로 보내기
            print("서버로 값 보내기 실행")
            
            join_value = client_server.join(id, pwd) # join_value에 client_server의 return값 반환
            # join_value = "ok" or "no"

            # join_value가 ok라면 하단 텍스트를 회원가입이 완료되었습니다로 바꿔줌
            if join_value == "ok":
                finish = "회원가입이 완료되었습니다."
                label1.config(text=finish)
                root.destroy() # 창 닫기
            # join_value가 no라면 하단 텍스트를 이미 있는 아이디입니다로 바꿔줌
            else:
                finish = "이미 있는 아이디입니다."
                label1.config(text=finish)

            print("버튼 값 :",join_value)

    # 회원가입 버튼
    btn = Button(root, text="회원가입 확인", command=a_join) # 회원가입 버튼 클릭 시 a_join 함수 실행
    btn.pack()
    btn.place(x=285, y=415) # 위치 선정
    root.mainloop()