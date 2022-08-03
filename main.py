import pygame
import subprocess
import sys


def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

copy2clip("wsg")
pygame.init()



font = pygame.font.SysFont('Arial', 10)

objects = []


fps = 60
fpsClock = pygame.time.Clock()

color = (255 ,255,255)
favicon = pygame.image.load('resources/images/favicon.png')



pygame.display.set_icon(favicon)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("FastMachine: Gotta Go Fast")


exit = False
class Button():
    
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)
def VaultBasic():
    copy2clip("V3;2P;2P;{(0(3n.)h)08}ddd(2O(2D)}}}$})05h(2O(2E)t}}(5u)8(2O(2D)9r}}h(5r)6}(2O(2D)dhv}9(2N)6D(2O(2E)vf}d}7}}}}3(2O(2F)vNd)07N(3Eh(3n=)(0(q{);The Machine Box V1.2;;0")
    
customButton = Button(30, 30, 160, 40, 'Copy Basic Vault', VaultBasic)

while True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for object in objects:
        object.process()

    pygame.display.flip()
    fpsClock.tick(fps)
