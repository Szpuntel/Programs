import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init() # Init game (creates game)
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) # Creates window
        self.clock = pygame.time.Clock() # Frame rate
        self.running = True
        self.font = pygame.font.Font('arcade_font.TTF', 32)

        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet = Spritesheet('img/enemy.png')
        self.intro_background = pygame.image.load('img/introbackground.png')
        self.go_background = pygame.image.load('img/gameover.png')




    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)
                if column == "E":
                    Enemy(self, j, i)



    def new(self): #new game
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates() # Where All sprites are stored
        self.blocks = pygame.sprite.LayeredUpdates() # Where All walls are stored
        self.enemies = pygame.sprite.LayeredUpdates() # Contains all enemies
        self.attacks = pygame.sprite.LayeredUpdates() # contains all attacks
        
        self.createTilemap()

    def event(self): # Game loop events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False


    def update(self): 
        self.all_sprites.update() # Calls update method on every sprite in the group

    def draw(self):
        self.screen.fill(BLACK)  # fills screen with black
        self.all_sprites.draw(self.screen) # looks throu every singe sprite in all_sprites find image and rect of player/enemy and draws it on window
        self.clock.tick(FPS)  # How often draws are updated 
        pygame.display.update()

    def main(self):  # Game loop

        while self.playing:
            self.event()  # Contains every key pressed event
            self.update()  # Basicly updates the game so its not just static image
            self.draw()  # Puts all enemies walls, player on map


    def game_over(self):
        text = self.font.render('GAME OVER', True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))

        restart_button = Button(10, WIN_HEIGHT -60, 120,50, WHITE, BLACK, 'Restart', 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()

            self.screen.blit(self.go_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()


    def intro_screen(self):
        intro = True

        title = self.font.render('Literally        Black        Ninja', True, BLACK)
        title_rect = title.get_rect(x=10, y=10)

        play_button = Button(10, 50, 100, 50, WHITE, BLACK, 'Play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
                
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(self.intro_background,(0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

g = Game()

g.intro_screen()

g.new()

while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
