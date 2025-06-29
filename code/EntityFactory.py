from code.Background import Background
from code.Const import WIN_WIDTH, GROUND_Y
from code.Obstacle import Obstacle
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg =[]
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('PlayerJump', (40, GROUND_Y))
            case 'Obstacle1':
                # Obstáculo começa fora da tela à direita (WIN_WIDTH + uma margem)
                # e na altura do chão (GROUND_Y)
                obstacle_x = WIN_WIDTH + 50  # 50 pixels fora da tela para dar espaço
                return Obstacle('Obstacle1', (obstacle_x, GROUND_Y))
            case _:
                print(f"Aviso: Entidade desconhecida solicitada: {entity_name}")
                return []
