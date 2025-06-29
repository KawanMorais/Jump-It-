import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, SCORE_FILE
from code.Level import Level
from code.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('JumpIt')
        self.high_score = self.load_high_score()

    def load_high_score(self):
        # Carrega o high score de um arquivo.
        try:
            with open(SCORE_FILE, 'r') as f:
                score = int(f.read().strip())
                return score
        except (FileNotFoundError, ValueError):
            return 0  # Retorna 0 se o arquivo não existir ou o conteúdo não for um número

    def save_high_score(self):
        # Salva o high score atual no arquivo.
        with open(SCORE_FILE, 'w') as f:
            f.write(str(self.high_score))

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run(self.high_score)

            if menu_return == MENU_OPTION[0]:
                while True:
                    level = Level(self.window, 'level1')
                    level_return = level.run()

                    if level.score > self.high_score:
                        self.high_score = level.score
                        self.save_high_score()
                        print(f"Novo High Score: {self.high_score}")

                    if level_return == "restart":
                        continue
                    elif level_return == "menu":
                        break
                    else:
                        break
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
            else:
                pass

