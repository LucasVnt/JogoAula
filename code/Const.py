# E
import pygame

ENTITY_HEALTH = {
    'Levelbg0' : 999,
    'Levelbg1' : 999,
    'Levelbg2' : 999,
    'Levelbg3' : 999,
    'Levelbg4' : 999,
    'Player1' : 10,
    'Player1Shot': 1,
    'Player2' : 10,
    'Player2Shot': 1,
    'Enemy1' : 1,
    'Enemy1Shot': 1,
    'Enemy2' : 3,
    'Enemy2Shot': 3,
    'Enemy3' : 5,
    'Enemy3Shot': 5,
    'Asteroid' : 999,

}

EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Levelbg0' : 0,
    'Levelbg1' : 1,
    'Levelbg2' : 2,
    'Levelbg3' : 3,
    'Levelbg4' : 4,
    'Player1' : 4,
    'Player1Shot': 8,
    'Player2' : 4,
    'Player2Shot': 8,
    'Enemy1' : 4,
    'Enemy1Shot': 12,
    'Enemy2' : 2,
    'Enemy2Shot': 3,
    'Enemy3' : 1,
    'Enemy3Shot' : 2,

}

ENTITY_SHOT_DELAY = {
    'Player1' : 15,
    'Player2' : 15,
    'Enemy1': 60,
    'Enemy2': 80,
    'Enemy3': 100,
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