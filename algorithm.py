from settings import *
import copy

def get_zero(state):
    pos = [0,0]
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                pos = [i,j]
                break
    return pos

def neighpours(state, curr_path , fronter):
    x,y = get_zero(state)
    if x>=1 :  #up
        temp = copy.deepcopy (state)
        temp[x][y] , temp[x-1][y] = temp[x-1][y] , temp[x][y]
        fronter.append((temp , curr_path+["down"]))
    if x<=1 : #down
        temp  = copy.deepcopy (state)
        temp[x+1][y] , temp[x][y] = temp[x][y] , temp[x+1][y]
        fronter.append((temp , curr_path+["up"]))
    if y>=1 : # left
        temp = copy.deepcopy (state)
        temp[x][y-1] , temp[x][y] = temp[x][y] , temp[x][y-1]
        fronter.append((temp , curr_path+["right"]))
    if y<=1: # right
        temp = copy.deepcopy (state)
        temp[x][y+1] , temp[x][y] = temp[x][y] , temp[x][y+1]
        fronter.append((temp , curr_path+["left"]))

def DO(start , goal,type):
    vistited = []
    fronter = [(start , [])] #the queue of tuple
    while len(fronter) > 0 :
        curr_state , curr_path = fronter.pop(type)
        if curr_state == goal:
            return curr_path
        if curr_state not in vistited:
            vistited.append(curr_state)
            neighpours(curr_state, curr_path , fronter)
    return "No solution found!"

def Solve(type,game):
    path=DO(start,goal,type)
    return path