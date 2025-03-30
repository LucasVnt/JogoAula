import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Player import Player
from code.Enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Levelbg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Levelbg{i}', (0, 0)))
                    list_bg.append(Background(f'Levelbg{i}', (0, -320)))
                return list_bg
            case 'Player1':
                return Player('Player1', (110, 270))
            case 'Player2':
                return Player('Player2', (170, 270))
            case 'Enemy1':
                return Enemy('Enemy1', (random.randint(10, WIN_WIDTH - 40), - 160))
            case 'Enemy2':
                return Enemy('Enemy2', (random.randint(10, WIN_WIDTH - 40), - 160))
