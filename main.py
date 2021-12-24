# Complete your game here
import pygame
from random import *

clock = pygame.time.Clock()
fps=60
font = "calibri.ttf"
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(240, 30, 30)
green=(30, 50, 200)
blue=(85, 150, 220)
yellow=(255, 225, 10)

class MyGame:
    def __init__(self):
        pygame.init()
    
        self.level=1
        self.win=0
        self.load_images()
        self.window_height = 480
        self.window_width = 640
        self.new_game()
        # self.height = len(self.map)
        # self.width = len(self.map[0])
        # self.scale = list(self.imagesDict.values())[0].get_width()
        # self.block_width = list(self.imagesDict.values())[0].get_width()
        # self.block_height = list(self.imagesDict.values())[0].get_height()
        # self.camera_offsety = self.window_height/self.block_height
        # self.camera_offsetx = self.window_width/self.block_width

        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        # self.initial_stuff()
        
        pygame.display.set_caption("Meco Game")

        self.main_menu()

    def load_images(self):
        self.imagesDict = {'wall': pygame.image.load('Wood_Block_Tall.png'),
                        'floor': pygame.image.load('Plain_Block.png'),
                        'grass': pygame.image.load('Grass_Block.png'),
                        'boy': pygame.image.load('boy.png'),
                        'girl': pygame.image.load('princess.png'),
                        'rock': pygame.image.load('Rock.png'),
                        'monster': pygame.image.load('monster.png'),
                        'goal_c': pygame.image.load('Selector.png'),
                        'goal_o': pygame.image.load('RedSelector.png')}

        self.ground = {'g': self.imagesDict['grass'],
                    'f': self.imagesDict['floor']}

        self.block = {'w': self.imagesDict['wall'],}

        self.objects = {'x': self.imagesDict['rock']}

        self.players = {'p': self.imagesDict['boy']}

        self.enimies = {'m': self.imagesDict['monster']}

        self.goal = {'0': self.imagesDict['goal_c'],
                    '1': self.imagesDict['goal_o']}

    def new_game(self):
        self.map = []
        linemap = []
        
        with open(f"{self.level}.txt") as new_file:
            for line in new_file:
                line = line.replace("\n", "")
                linemap.append(line)

        # Find the longest row in the map.
        maxWidth = -1
        for i in range(len(linemap)):
            if len(linemap[i]) > maxWidth:
                maxWidth = len(linemap[i])
        # Add spaces to the ends of the shorter rows. This ensures the map will be rectangular.
        for i in range(len(linemap)):
            linemap[i] += 'w' * (maxWidth - len(linemap[i]))

        # Create map file
        for line in linemap:
            a = []
            for char in line:
                a.append(char)
            self.map.append(a)

        self.timePassed = 0
        self.passed = False

        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = list(self.imagesDict.values())[0].get_width()
        self.block_width = list(self.imagesDict.values())[0].get_width()
        self.block_height = list(self.imagesDict.values())[0].get_height()
        self.camera_offsety = self.window_height/self.block_height
        self.camera_offsetx = self.window_width/self.block_width
        initp = self.find_player()
        self.initial_camera=[-self.camera_offsety/2+initp[0],-self.camera_offsetx/2+initp[1]]
        self.camera=[-self.camera_offsety/2+initp[0],-self.camera_offsetx/2+initp[1]]
        self.background_static = self.background()

    # def initial_stuff(self):
    #     # initb = self.find_ball()
    #     initp = self.find_player()
    #     self.initial_camera=[-self.camera_offsety/2+initp[0],-self.camera_offsetx/2+initp[1]]
    #     self.camera=[-self.camera_offsety/2+initp[0],-self.camera_offsetx/2+initp[1]]
    #     self.background_static = self.background()

    def foreground(self):
        self.objectmap = []
        for y in range(self.height):
            a = []
            for x in range(self.width):
                square = self.map[y][x]
                if square in self.players.keys() or square in self.objects.keys() or square in self.block.keys():
                    a.append(square)
                else:
                    a.append(" ")
            self.objectmap.append(a)

    def background(self):
        self.background_static = []
        for y in range(self.height):
            a = []
            for x in range(self.width):
                square = self.map[y][x]
                if square in self.ground.keys() or square in self.block.keys() or square in self.goal.keys():
                    a.append(square)
                else:
                    a.append("f")
            self.background_static.append(a)
        return self.background_static

    def draw_background(self,dy,dx):
        for y in range(self.height):
            for x in range(self.width):
                square = self.background_static[y][x]
                if square in self.ground.keys():
                    self.window.blit(self.ground[square], ((x-dx) * self.scale, (y-dy) * self.scale))
                elif square in self.block.keys():
                    self.window.blit(self.block[square], ((x-dx) * self.scale, (y-dy) * self.scale))
                # elif square in self.goal.keys():
                #     self.window.blit(self.goal[square], ((x-dx) * self.scale, (y-dy) * self.scale))
                else:
                    self.window.blit(self.ground["f"], ((x-dx) * self.scale, (y-dy) * self.scale))

    def draw_window(self):
        self.draw_background(self.camera[0],self.camera[1])
        dy=self.camera[0]
        dx=self.camera[1]
        for y in range(self.height):
            for x in range(self.width):
                square = self.map[y][x]
                if square in self.players.keys():
                    self.window.blit(self.players[square], ((x-dx) * self.scale, (y-dy) * self.scale))
                if square in self.objects.keys():
                    self.window.blit(self.objects[square], ((x-dx) * self.scale, (y-dy) * self.scale))
                if square in self.enimies.keys():
                    self.window.blit(self.enimies[square], ((x-dx) * self.scale, (y-dy) * self.scale))
                if square in self.goal.keys():
                    self.window.blit(self.goal[square], ((x-dx) * self.scale, (y-dy) * self.scale))
        self.draw_counter()
        pygame.display.flip()

    def draw_counter(self):
        if len(self.find_enemy()) > 0:
            counter=self.text_format(f"Enimies alive: {len(self.find_enemy())}", font, 18, black)
            title_rect=counter.get_rect()
            pygame.draw.rect(self.window, (white), (0,self.window_height-25, 140, 50))
            pygame.draw.rect(self.window, (black), (0,self.window_height-25, 140, 50), 2)
            self.window.blit(counter, (10, self.window_height-20))
        else:
            counter=self.text_format(f"Go to the exit", font, 18, black)
            title_rect=counter.get_rect()
            pygame.draw.rect(self.window, (white), (0,self.window_height-25, 140, 50))
            pygame.draw.rect(self.window, (black), (0,self.window_height-25, 140, 50), 2)
            self.window.blit(counter, (10, self.window_height-20))


    def draw_hint(self):
        nextlevel = True

        hint=self.text_format("Try pushing the ball to the water. It bounces!", font, 20, blue)
        title_rect=hint.get_rect()
        pygame.draw.rect(self.window, (white), (100,self.window_height/2-25, self.window_width-200, 100))
        pygame.draw.rect(self.window, (black), (100,self.window_height/2-25, self.window_width-200, 100), 2)
        self.window.blit(hint, (self.window_width/2 - (title_rect[2]/2), 255))
        pygame.display.update()

        while nextlevel == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_h:
                        nextlevel = False
        
        self.draw_window()

    
    def text_format(self, message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
        return newText

    def main_menu(self):
        menu = True
        selected="start"
        self.level = 1

        while menu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        selected="start"
                    elif event.key==pygame.K_DOWN:
                        selected="quit"
                    if event.key==pygame.K_RETURN:
                        if selected=="start":
                            self.window.fill((0, 0, 0))
                            self.main_loop()
                        if selected=="quit":
                            pygame.quit()
                            quit()
                        
            # Main Menu UI
            self.window.fill(gray)
            title=self.text_format("Meco Game", font, 100, blue)
            if selected=="start":
                text_start=self.text_format("START", font, 75, white)
            else:
                text_start = self.text_format("START", font, 75, black)
            if selected=="quit":
                text_quit=self.text_format("QUIT", font, 75, white)
            else:
                text_quit = self.text_format("QUIT", font, 75, black)
            text_inst=self.text_format("Buttons: UP, DOWN, LEFT, RIGHT, H (hint)", font, 26, yellow)
    
            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            inst_rect=text_inst.get_rect()
            quit_rect=text_quit.get_rect()
    
            # Main Menu Text
            self.window.blit(title, (self.window_width/2 - (title_rect[2]/2), 80))
            self.window.blit(text_start, (self.window_width/2 - (start_rect[2]/2), 200))
            self.window.blit(text_quit, (self.window_width/2 - (quit_rect[2]/2), 260))
            self.window.blit(text_inst, (self.window_width/2 - (inst_rect[2]/2), 360))
            pygame.display.update()
            clock.tick(fps)   


    def main_loop(self):
        while True:
            self.timePassed = self.timePassed + clock.tick()
            if self.timePassed > 2000:
                self.enemy_move()
                self.timePassed = 0
            # print(self.timePassed)
            self.check_events()
            self.draw_window()
            if self.win==1:
                self.win=0
                self.win_text()
                self.window.fill((0, 0, 0))
                self.next_level()
            

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    self.players = {'p': self.imagesDict['boy']}
                    self.move(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.players = {'p': self.imagesDict['boy']}
                    self.move(0, 1)
                if event.key == pygame.K_UP:
                    self.players = {'p': self.imagesDict['girl']}
                    self.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.players = {'p': self.imagesDict['girl']}
                    self.move(1, 0)
                if event.key == pygame.K_h:
                    self.draw_hint()

            if event.type == pygame.QUIT:
                exit()

    def find_player(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in ["p"]:
                    return (y, x)

    def find_ball(self):
            for y in range(self.height):
                for x in range(self.width):
                    if self.map[y][x] in ["x"]:
                        return (y, x)

    def find_enemy(self):
        position=[]
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in ["m"]:
                    position.append((y, x))
        return position

    def find_goal(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in ["0"]:
                    return (y, x)

    def enemy_move(self):
        listEnemies = self.find_enemy()
        if len(listEnemies) == 0:
            return
        for enemy in listEnemies:
            enemy_old_y, enemy_old_x = enemy
            move_ey = randint(-1,1)
            if move_ey == 0:
                move_ex = randrange(-1,2,2)
            else:
                move_ex = 0
            
            enemy_new_y = enemy_old_y + move_ey
            enemy_new_x = enemy_old_x + move_ex

            if self.map[enemy_new_y][enemy_new_x] not in ["w","x","m","0","1"]:
                if self.map[enemy_new_y][enemy_new_x] in ["p"]:
                    self.death()
                    return

                self.map[enemy_old_y][enemy_old_x] = " "
                self.map[enemy_new_y][enemy_new_x] = "m"
        
        self.draw_window()

    def next_level(self):
        self.level = self.level + 1
        nextlevel = False
        while nextlevel == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        nextlevel = True
                if event.type == pygame.QUIT:
                    exit()
        self.new_game()
        
    def death(self):
        dead=self.text_format("Well...you're dead", font, 60, red)
        title_rect=dead.get_rect()
        pygame.draw.rect(self.window, (white), (0,self.window_height/2-25, self.window_width, 100))
        pygame.draw.rect(self.window, (black), (0,self.window_height/2-25, self.window_width, 100), 2)
        self.window.blit(dead, (self.window_width/2 - (title_rect[2]/2), 240))
        pygame.display.update()
        clock.tick(fps)
        startanew = False
        while startanew == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        startanew = True
                if event.type == pygame.QUIT:
                    exit()
        self.new_game()
        self.main_menu()

    def win_text(self):
        win=self.text_format("Well Done", font, 60, blue)
        title_rect=win.get_rect()
        pygame.draw.rect(self.window, (white), (0,self.window_height/2-25, self.window_width, 100))
        pygame.draw.rect(self.window, (black), (0,self.window_height/2-25, self.window_width, 100), 2)
        self.window.blit(win, (self.window_width/2 - (title_rect[2]/2), 240))
        pygame.display.update()
        clock.tick(fps)

    def move(self, move_y, move_x):
        player_old_y, player_old_x = self.find_player()
        player_new_y = player_old_y + move_y
        player_new_x = player_old_x + move_x
        bounce = 0

        if self.map[player_new_y][player_new_x] in ["w","0"]:
            return

        if self.map[player_new_y][player_new_x] in ["x"]:
            object_new_y = player_new_y + move_y
            object_new_x = player_new_x + move_x

            if self.map[object_new_y][object_new_x] in ["w","x","0","1"]:
                self.map[player_new_y][player_new_x] = "p"
                self.map[player_old_y][player_old_x] = "x"
                bounce = 1
            else: 
                self.map[player_new_y][player_new_x] = "p"
                self.map[object_new_y][object_new_x] = "x"

        if self.map[player_new_y][player_new_x] in ["m"]:
            self.death()
            return

        if self.map[player_new_y][player_new_x] in ["1"]:
            self.win=1

        if len(self.find_enemy()) == 0 and self.passed == False:
            goal_y, goal_x = self.find_goal()
            if self.map[goal_y][goal_x] == "0":
                self.map[goal_y][goal_x] = "1"
            self.passed = True

        if bounce == 0:
            self.map[player_old_y][player_old_x] = " "
        elif bounce == 1:
            bounce = 0
        self.map[player_new_y][player_new_x] = "p"
        movement = [move_y,move_x]
        self.camera = [a+b for a,b in zip(self.camera,movement)]

if __name__ == "__main__":
    MyGame()