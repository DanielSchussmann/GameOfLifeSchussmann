from main import *

#-Name: Simkin glider gun
#-Source: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
Ex1 = GameOfLife()
Ex1.n = 40
with open('ex_1.pkl', 'rb') as f:
    inp = pickle.load(f)

print(inp)
Ex1.output(inp)

