# E
import pygame

ENTITY_SPEED = {
    'Levelbg0' : 0,
    'Levelbg1' : 1,
    'Levelbg2' : 2,
    'Levelbg3' : 3,
    'Levelbg4' : 4,
    'Player1' : 4,
    'Player2' : 4,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P',
               'SCOREBOARD',
               'EXIT')
# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                 'Player2': pygame.K_LCTRL}

# W
WIN_WIDTH = 320
WIN_HEIGHT = 320