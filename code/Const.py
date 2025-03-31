import pygame

# C

C_WHITE = (245,245,245)
C_YELLOW = (255,255,0)
C_GREEN = (0,128,0)
C_CYAN = (0,128,128)

# E

ENTITY_DAMAGE = {
    'Levelbg0' : 0,
    'Levelbg1' : 0,
    'Levelbg2' : 0,
    'Levelbg3' : 0,
    'Levelbg4' : 0,
    'Player1' : 1,
    'Player1Shot': 25,
    'Player2' : 1,
    'Player2Shot': 25,
    'Enemy1' : 100,
    'Enemy1Shot': 25,
    'Enemy2' : 100,
    'Enemy2Shot': 50,
    'Enemy3' : 100,
    'Enemy3Shot': 100,
    'Asteroid' : 300,
}

ENTITY_HEALTH = {
    'Levelbg0' : 999,
    'Levelbg1' : 999,
    'Levelbg2' : 999,
    'Levelbg3' : 999,
    'Levelbg4' : 999,
    'Player1' : 500,
    'Player1Shot': 1,
    'Player2' : 500,
    'Player2Shot': 1,
    'Enemy1' : 25,
    'Enemy1Shot': 1,
    'Enemy2' : 75,
    'Enemy2Shot': 1,
    'Enemy3' : 125,
    'Enemy3Shot': 1,
    'Asteroid' : 999,

}

ENTITY_SCORE = {
    'Levelbg0' : 0,
    'Levelbg1' : 0,
    'Levelbg2' : 0,
    'Levelbg3' : 0,
    'Levelbg4' : 0,
    'Player1' : 0,
    'Player1Shot': 0,
    'Player2' : 0,
    'Player2Shot': 0,
    'Enemy1' : 10,
    'Enemy1Shot': 0,
    'Enemy2' : 50,
    'Enemy2Shot': 0,
    'Enemy3' : 100,
    'Enemy3Shot' : 0,
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

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
    'Enemy1' : 3,
    'Enemy1Shot': 4,
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

# S
SCORE_POS = {'Title': (160, 40),
             'EnterName': (WIN_WIDTH / 2, 60),
             'Label': (WIN_WIDTH / 2, 80),
             'Name': (WIN_WIDTH / 2, 100),
             0: (WIN_WIDTH / 2, 100),
             1: (WIN_WIDTH / 2, 120),
             2: (WIN_WIDTH / 2, 140),
             3: (WIN_WIDTH / 2, 160),
             4: (WIN_WIDTH / 2, 180),
             5: (WIN_WIDTH / 2, 200),
             6: (WIN_WIDTH / 2, 220),
             7: (WIN_WIDTH / 2, 240),
             8: (WIN_WIDTH / 2, 260),
             9: (WIN_WIDTH / 2, 280),
             }