import pygame
import time
import random
from settings import *
from sprite import *
pygame.mixer.init()


class Game:
    def __init__(self):
        pygame.init()
        self.game_sound=pygame.mixer.Sound('../ICY_Tower_Puzzle/sound/IcyTower.mp3')
        self.amazing=pygame.mixer.Sound('../ICY_Tower_Puzzle/sound/amazing.mp3')
        self.wow=pygame.mixer.Sound('../ICY_Tower_Puzzle/sound/wow.mp3')
        self.game_sound.play(-1)
        self.screen=pygame.display.set_mode((width,hight))
        pygame.display.set_caption(title)
        self.clock=pygame.time.Clock()
        self.BFS=False
        self.DFS=False
        self.reset=False

    def create_game(self,state):
        start=[
            [1,2,3],
            [7,4,5],
            [0,8,6]
        ]
        goal=[
            [1,2,3],
            [4,5,6],
            [7,8,0]
        ]
        grid=start
        if state=='goal' : grid=goal

        return grid
    
    def draw_tile(self,delay=0):
        self.tiles=[]
        for row,x in enumerate(self.tile_grid):
            self.tiles.append([])
            for col,tile in enumerate(x):              
                self.tiles[row].append(Tile(self,col,row,tile))
            
      
    
                
    def Draw_Button(self):
        self.paly_bfs=Button(right_pos+75,150,250,60,red,hover,"PLAY WITH BFS",yellwo,25)
        self.paly_bfs.draw_rect(self.screen)
        self.paly_dfs=Button(right_pos+75,230,250,60,red,hover,"PLAY WITH DFS",yellwo,25)
        self.paly_dfs.draw_rect(self.screen)
        self.reset=Button(right_pos+125,350,150,60,lightGray,hover,"RESET",white,25)
        self.reset.draw_ellipse(self.screen)
            
    def new(self):
        self.all_sprite=pygame.sprite.Group()
        self.tile_grid=self.create_game(start)
        self.tile_grid_complete=self.create_game(goal)
        self.ind=0
        self.draw()
        self.path=[]
        self.draw_tile()

    def run(self):
        self.palying=True
        while self.palying:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()

    def update(self):
        if self.BFS== True:
            self.move(self.path[self.ind])
            self.draw_tile()
            self.ind+=1
            if self.ind>=len(self.path):
                self.amazing.play() 
                self.BFS=False   
            
        if self.DFS:
            self.move(self.path[self.ind])
            self.draw_tile()
            self.ind+=1
            if self.ind >= len(self.path):
                self.wow.play()
                self.DFS=False
                
                
            
        self.all_sprite.update()
        

    def move(self,mov):
        row,col=get_zero(self.tile_grid)
        if mov == "up":
            self.tile_grid[row][col],self.tile_grid[row+1][col]=self.tile_grid[row+1][col],self.tile_grid[row][col]
        elif mov == "down":
            self.tile_grid[row][col],self.tile_grid[row-1][col]=self.tile_grid[row-1][col],self.tile_grid[row][col]

        elif mov == "right":
            self.tile_grid[row][col],self.tile_grid[row][col-1]=self.tile_grid[row][col-1],self.tile_grid[row][col]

        elif mov == "left":
            self.tile_grid[row][col],self.tile_grid[row][col+1]=self.tile_grid[row][col+1],self.tile_grid[row][col]
        pygame.time.delay(300)
           
            
            
   
    def draw(self):
        self.screen.fill(paige)
        self.all_sprite.draw(self.screen)
        self.Draw_Button()
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            # close window
           
            if event.type==pygame.QUIT:
                pygame.quit()
                quit(0)
            # sliding tiles when click on it
            if event.type==pygame.MOUSEBUTTONDOWN: 
                mouse_x,mouse_y=pygame.mouse.get_pos()
                if self.paly_bfs.click(mouse_x,mouse_y):
                    self.ind=0
                    self.path=Solve(0,game)
                    self.BFS=True
                if self.paly_dfs.click(mouse_x,mouse_y):
                    self.ind=0
                    self.path=Solve(-1,game)
                    self.DFS=True
                if self.reset.click(mouse_x,mouse_y):
                    self.new()
                      

game=Game()
while True:
    game.new()
    game.run()

