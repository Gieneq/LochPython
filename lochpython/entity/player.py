# import pygame
# from core.settings import TILESIZE
#
# from core.debug import Debugger
# from entity.entity import Entity
#
#
# class Player(Entity):
#     def __init__(self, starting_pos, world, visible=True):
#         super().__init__(world=world)
#         self.image = pygame.image.load('./data/graphics/player.png').convert_alpha()
#         self.rect = pygame.Rect(starting_pos, (TILESIZE, TILESIZE))
#         self.hitbox = self.rect.inflate(0, -26)
#         # self.add(self.world.entities)
#         world.entities.append(self)
#         self.set_visible(visible)
#         self.draw_rect = pygame.Rect((0,0),  (TILESIZE, TILESIZE)) #todo meh not DRY
#
#         self.direction = pygame.math.Vector2()
#         self.speed = 300
#         self.cooldown = 0
#         self.cooldown_start_time = 0
#
#     def input(self):
#         keys = pygame.key.get_pressed()
#
#         # movement
#         if keys[pygame.K_w]:
#             self.direction.y = -1
#         elif keys[pygame.K_s]:
#             self.direction.y = 1
#         else:
#             self.direction.y = 0
#
#         if keys[pygame.K_a]:
#             self.direction.x = -1
#         elif keys[pygame.K_d]:
#             self.direction.x = 1
#         else:
#             self.direction.x = 0
#
#     def update(self, dt, *args, **kwargs):
#         super().update(*args, **kwargs)
#         Debugger.print(f"Player_center: {self.rect.center}")
#         self.input()
#         self.move(self.speed, dt, self.direction)
