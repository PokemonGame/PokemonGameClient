import login
import playgame
import pickle
import random
import client_server
from random import *

login.login()


with open('game_state', 'rb') as file:   
    pokemon_exe = pickle.load(file)

print("시작 전 :", pokemon_exe)

if pokemon_exe == "ok":
    playgame.work()