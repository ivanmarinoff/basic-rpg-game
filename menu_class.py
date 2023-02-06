import pygame

from mage_character import Mage
from warrior_character import Warrior


class Menu:
    arrow = [pygame.image.load(f'images/menu/arrow/({i}).png') for i in range(1, 9)]
    arrow_pos = ((225, 80), (900, 80))

    pygame.mixer.init()
    pygame.mixer.music.load("images/menu/music.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)

    buttons_x, buttons_y = 1920 / 2 - 100, 1080 / 1.01 - 210
    menu_image = pygame.image.load('images/menu/make_character.jpg')

    button_play = pygame.image.load('images/menu/play.png')
    is_ready_to_start = False
    button_play_rect = button_play.get_rect()
    button_play_rect.x = buttons_x
    button_play_rect.y = buttons_y

    fake_start = pygame.image.load('images/menu/fake_start.png')

    button_quit = pygame.image.load('images/menu/exit.png')
    button_quit_rect = button_quit.get_rect()
    button_quit_rect.x = buttons_x
    button_quit_rect.y = buttons_y + 123

    platform = pygame.image.load('images/menu/platform.png')

    heroes_x_y = [(120, 240), (790, 240)]

    warrior_rect = Warrior().idle_animation().get_rect()
    warrior_rect.x = heroes_x_y[0][0]
    warrior_rect.y = heroes_x_y[0][1]

    mage_rect = Mage().idle_animation().get_rect()
    mage_rect.x = heroes_x_y[1][0]
    mage_rect.y = heroes_x_y[1][1]

    WIDTH, HEIGHT = (1920, 1080)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    selected = {"Warrior": False, "Mage": False, }

    index = 0
    see_arrow = arrow[int(index) % len(arrow)]

    chosen_hero = ""
    class_names = ["Warrior", "Mage"]

    def __init__(self, ):
        self.main_menu = True
        self.warrior = Warrior()
        self.mage = Mage()

    def menu(self, ):
        while self.main_menu:
            self.screen.blit(self.menu_image, (0, 0))

            self.screen.blit(self.button_quit, self.button_quit_rect)
            self.screen.blit(self.platform, (70, 600))
            self.screen.blit(self.platform, (750, 600))
            self.screen.blit(self.platform, (1400, 600))

            if not self.is_ready_to_start:
                self.screen.blit(self.fake_start, self.button_play_rect)

            self.screen.blit(self.warrior.idle_animation(), (self.heroes_x_y[0][0], self.heroes_x_y[0][1]))
            self.screen.blit(self.mage.idle_animation(), (self.heroes_x_y[1][0], self.heroes_x_y[1][1]))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.is_ready_to_start:
                        chosen_hero = self.chosen_hero
                        start = eval(chosen_hero)
                        end = start()
                        if self.button_play_rect.collidepoint(mouse_pos):
                            for _ in range(300):
                                self.screen.blit(self.menu_image, (0, 0))
                                self.screen.blit(end.jump_animation(), (650, 200))
                                pygame.display.update()
                            self.main_menu = False

                    if self.warrior_rect.collidepoint(mouse_pos):
                        self.selected['Warrior'] = True
                        self.selected['Mage'] = False
                        self.button_play_rect.x = 150

                    elif self.mage_rect.collidepoint(mouse_pos):
                        self.selected['Warrior'] = False
                        self.selected['Mage'] = True
                        self.button_play_rect.x = self.buttons_x

                    elif self.button_quit_rect.collidepoint(mouse_pos):
                        quit()

            i = 0
            for key, value in self.selected.items():
                self.index += 0.13
                if value:
                    see_arrow = self.arrow[int(self.index) % len(self.arrow)]
                    self.screen.blit(see_arrow, (self.arrow_pos[i][0], self.arrow_pos[i][1]))

                    self.is_ready_to_start = True
                    self.screen.blit(self.button_play, self.button_play_rect)

                    self.chosen_hero = key

                i += 1
            pygame.display.flip()


menu = Menu()
menu.menu()
