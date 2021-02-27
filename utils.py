from serv import discovery_protocol
from constants import *
import random


def write_text(t, pos, size, pygame, screen,
               font='fonts/static/RobotoMono-MediumItalic.ttf', color=(0, 0, 0)):
    # print(pygame)
    font = pygame.font.Font(font, size)
    text = font.render(f'{t}', 1, color)
    screen.blit(text, (pos))


class Button():
    def __init__(self, x, y, w, h):
        self.btn = (x, y, w, h)

    def draw(self, t, size, pygame, screen):
        pygame.draw.rect(screen, WHITE, self.btn)
        write_text(
            t,
            (self.btn[0] + 10,
             self.btn[1] + 10),
            size,
            pygame=pygame,
            screen=screen)

    def is_clicked(self, pos):
        if self.btn[0] <= pos[0] <= self.btn[0] + \
                self.btn[2] and self.btn[1] <= pos[1] <= self.btn[1] + self.btn[3]:
            return True
        else:
            return False


def connect(result, index):
    pid = random.getrandbits(64)
    info = discovery_protocol.DiscoveryProtocol(pid, 37020).run()
    if result[index] == 'stoped':
        return {"error": "hello"}
    result[index] = {"my": pid, "enemy": info}


def check_in_the_first_part(coords, width):
    return coords[0] < width / 2
