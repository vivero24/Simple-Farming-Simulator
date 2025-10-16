import pygame
import sys
from tilemap import Tilemap
from player import Player
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Farming simulator")
        self.screen_res = (640, 480)
        self.screen = pygame.display.set_mode(self.screen_res)
        self.clock = pygame.time.Clock()
        self.tilemap = Tilemap(self, tile_size = 32)
        self.background = pygame.image.load("images/grassy_background.png").convert()
        self.background = pygame.transform.scale(self.background, (self.screen_res))

        self.player = Player(self, (100, 400))
        self.movement = [False, False, False, False] 
        self.current_collision = False
        self.collided = False

        self.cursor = pygame.image.load("images/flowerPot.png").convert()
        self.cursor.set_colorkey((0, 0, 0))
        pygame.mouse.set_visible(False)
        self.mouse_click = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.movement[2] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = True
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_UP:
                        self.movement[2] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_click = True     

            self.player.update((self.movement[1] - self.movement[0], self.movement[3] - self.movement[2]))
            self.current_collision = False

            for key, value in self.tilemap.tilemap.items():  

                if self.mouse_click and value['rect'].collidepoint(pygame.mouse.get_pos()):
                    print("Clicked")
                    if value['type'] == 'seed':
                        value['timer'] = pygame.time.get_ticks()
                        value['type'] = 'seed_growing'
                    elif value['type']  == 'sprout':
                        value['timer'] = pygame.time.get_ticks()
                        value['type'] = 'sprout_growing'

                    self.mouse_click = False
                
                if value['type'] == 'seed_growing':
                    elapsed_time =  pygame.time.get_ticks()- value['timer'] 
                    if elapsed_time >= 3000:
                        value['type'] = 'sprout'
                elif value['type'] == 'sprout_growing':
                    elapsed_time =  pygame.time.get_ticks()- value['timer'] 
                    if elapsed_time >= 3000:
                        value['type'] = 'grown'
                    
                if self.player.rect.colliderect(value['rect']): # player collision 
                    self.current_collision = True
                    if not self.collided:
                        print("Collided")
                        if value['type'] == 'seed' or value['type'] == 'sprout':
                            print("Already planted")
                        elif value['type'] == 'grown':
                            value['type'] = 'dirt'
                        else:
                            value['type'] = 'seed'

            if not self.current_collision and self.collided:
                print("Collision ended")


            self.collided = self.current_collision
            self.mouse_click = False
            
            self.screen.fill((0, 0 , 155))
            self.screen.blit(self.background, (0, 0))
            self.tilemap.render(self.screen)
            self.player.render(self.screen)
            cursor_pos = pygame.mouse.get_pos()
            self.screen.blit(self.cursor, cursor_pos)
            
            pygame.display.update()
            self.clock.tick(60)