from code.Background import Background
from code.Const import WIN_WIDTH


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