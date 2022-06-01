import pygame
from support import import_folder   

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,surface,create_jump_particles):
        super().__init__()
        self.import_charactar_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animation['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)