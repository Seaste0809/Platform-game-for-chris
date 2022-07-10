import pygame
from pygame import *
from pygame import mixer
import pygame.freetype
import time
import sys
from Button import Button

SCREEN_SIZE = pygame.Rect((0, 0, 1280, 720))
TILE_SIZE = 32
Map_border = (1000, 500)
GRAVITY = pygame.Vector2((0, 0.4))


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)


def Levels():
    while True:
        LEVELS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        LEVEL1_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(320, 100),
                             text_input="LeveL 1", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL2_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(320, 250),
                                text_input="LeveL 2", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL3_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(320, 400),
                             text_input="LeveL 3", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL4_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(320, 550),
                               text_input="LeveL 4", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL5_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(950, 100),
                               text_input="LeveL 5", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL6_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(950, 250),
                               text_input="LeveL 6", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL7_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(950, 400),
                               text_input="LeveL 7", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(950, 550),
                               text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")


        for button in [LEVEL1_BUTTON, LEVEL2_BUTTON, LEVEL3_BUTTON, LEVEL4_BUTTON, LEVEL5_BUTTON, LEVEL6_BUTTON, LEVEL7_BUTTON, BACK_BUTTON]:
            button.changeColor(LEVELS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL1_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    map_choice(level=1)
                    pygame.display.update()
                if LEVEL2_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    map_choice(level=2)
                    pygame.display.update()
                if LEVEL3_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    map_choice(level=3)
                if LEVEL4_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    map_choice(level=4)
                    pygame.display.update()
                if LEVEL5_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    map_choice(level=5)
                    pygame.display.update()
                if LEVEL6_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    map_choice(level=6)
                if LEVEL7_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    map_choice(level=7)
                    pygame.display.update()
                if BACK_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    main_menu()

        pygame.display.update()



def Credits():
    while True:
        SCREEN.fill("black")
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()
        CREDIT_TEXT = get_font(150).render("CREDITS", True, "#b68f40")
        CREDIT_RECT = CREDIT_TEXT.get_rect(center=(640, 100))
        INFO_TEXT = get_font(40).render("Made by Sean Steinberg", True, "#b68f40")
        INFO_RECT = CREDIT_TEXT.get_rect(center=(750, 380))
        SCREEN.blit(CREDIT_TEXT, CREDIT_RECT)
        SCREEN.blit(INFO_TEXT,INFO_RECT)
        BACK_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(950, 550),
                             text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        BACK_BUTTON.changeColor(CREDITS_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()

        pygame.display.update()




def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        LEVELS_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(640, 250),
                             text_input="Levels", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        CREDITS_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(640, 400),
                                text_input="Credits", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [LEVELS_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVELS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Levels()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()




class CameraAwareLayeredUpdates(pygame.sprite.LayeredUpdates):
    def __init__(self, target, world_size):
        super().__init__()
        self.target = target
        self.cam = pygame.Vector2(0, 0)
        self.world_size = world_size
        if self.target:
            self.add(target)

    def update(self, *args):
        super().update(*args)
        if self.target:
            x = -self.target.rect.center[0] + SCREEN_SIZE.width / 2
            y = -self.target.rect.center[1] + SCREEN_SIZE.height / 2
            self.cam += (pygame.Vector2((x, y)) - self.cam) * 0.5
            self.cam.x = max(-(self.world_size.width - SCREEN_SIZE.width), min(0, self.cam.x))
            self.cam.y = max(-(self.world_size.height - SCREEN_SIZE.height), min(0, self.cam.y))

    def draw(self, surface):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        init_rect = self._init_rect
        for spr in self.sprites():
            rec = spritedict[spr]
            newrect = surface_blit(spr.image, spr.rect.move(self.cam))
            if rec is init_rect:
                dirty_append(newrect)
            else:
                if newrect.colliderect(rec):
                    dirty_append(newrect.union(rec))
                else:
                    dirty_append(newrect)
                    dirty_append(rec)
            spritedict[spr] = newrect
        return dirty

def map_choice(level):
    if level == 1:
        main(Map = (open("maps/map.txt")))
    if level == 2:
        main(Map = (open("maps/map2.txt")))
    if level == 3:
        main(Map = (open("maps/map.txt")))
    if level == 4:
        main(Map = (open("maps/map2.txt")))
    if level == 5:
        main(Map = (open("maps/map.txt")))
    if level == 6:
        main(Map = (open("maps/map2.txt")))
    if level == 7:
        main(Map = (open("maps/map.txt")))



def main(Map):
    Music()
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    pygame.display.set_caption("Good Luck")
    timer = pygame.time.Clock()

    platforms = pygame.sprite.Group()
    player = Player(platforms, (TILE_SIZE, TILE_SIZE))
    level_width = Map_border[0] * TILE_SIZE
    level_height = Map_border[1] * TILE_SIZE
    entities = CameraAwareLayeredUpdates(player, pygame.Rect(0, 0, level_width, level_height))

    # build the map_border
    x = y = 0
    for row in Map:
        for col in row:
            if col == "P":
                PlatBasic((x, y), platforms, entities)
            if col == "E":
                PlatExit((x, y), platforms, entities)
            if col == "S":
                PlatSpeedH((x, y), platforms, entities)
            if col == "M":
                PlatSpeedM((x, y), platforms, entities)
            if col == "L":
                PlatSpeedL((x, y), platforms, entities)
            if col == "N":
                PlatNorm((x, y), platforms, entities)
            if col == "J":
                PlatJumpH((x, y), platforms, entities)
            if col == "G":
                PlatJumpM((x, y), platforms, entities)
            if col == "2":
                PlatLevel2((x, y), platforms, entities)
            x += TILE_SIZE
        y += TILE_SIZE
        x = 0

    while 1:

        for e in pygame.event.get():
            if e.type == QUIT:
                return
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return

        entities.update()

        screen.fill((0, 0, 0))
        entities.draw(screen)
        pygame.display.update()
        timer.tick(60)


class Entity(pygame.sprite.Sprite):
    def __init__(self, color, pos, *groups):
        super().__init__(*groups)
        self.image = Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)


class Player(Entity):
    def __init__(self, platforms, pos, *groups):
        super().__init__(Color("#5aa2e0"), pos)
        self.image = pygame.image.load("SpriteBasic.png").convert()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.vel = pygame.Vector2((0, 0))
        self.onGround = False
        self.platforms = platforms
        self.speed = 8
        self.jump_strength = 10

    def update(self):
        pressed = pygame.key.get_pressed()
        up = pressed[K_SPACE]
        left = pressed[K_LEFT]
        right = pressed[K_RIGHT]
        running = pressed[K_UP]
        quit = pressed[K_ESCAPE]

        if quit:
            pygame.quit()
            sys.exit()
        if up:
            # only jump if on the ground
            if self.onGround: self.vel.y = -self.jump_strength
        if left:
            self.vel.x = -self.speed
        if right:
            self.vel.x = self.speed
        if running:
            self.vel.x *= 1.5
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.vel += GRAVITY
            # max falling speed
            if self.vel.y > 100: self.vel.y = 100
        if not (left or right):
            self.vel.x = 0
        # increment in x direction
        self.rect.left += self.vel.x
        # do x-axis collisions
        self.collide(self.vel.x, 0, self.platforms)
        # increment in y direction
        self.rect.top += self.vel.y
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.vel.y, self.platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, PlatExit):
                    time.sleep(0.3)
                    SCREEN.fill((255, 0, 0))
                    my_font = pygame.font.SysFont('Comic Sans MS', 250)
                    font_render = my_font.render('WASTED', False, (0, 0, 0))
                    SCREEN.blit(font_render,(100,150))
                    pygame.display.update()
                    time.sleep(1.5)
                    Levels()

                if isinstance(p, PlatLevel2):
                    map_choice(level=2)
                    pygame.display.update()

                if isinstance(p, PlatSpeedH):
                    self.speed = 50
                if isinstance(p, PlatSpeedM):
                    self.speed = 16
                if isinstance(p, PlatSpeedL):
                    self.speed = 5



                if isinstance(p, PlatNorm):
                    self.speed = 8
                    self.jump_strength = 10

                if isinstance(p, PlatJumpH):
                    self.jump_strength = 30

                if isinstance(p, PlatJumpM):
                    self.jump_strength = 15



                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.vel.y = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

class PlatLevel2(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)


class PlatBasic(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#10eb93"), pos, *groups)


class PlatExit(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#c40c0c"), pos, *groups)


class PlatSpeedH(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)

class PlatSpeedM(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)

class PlatSpeedL(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)


class PlatNorm(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)


class PlatJumpH(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)

class PlatJumpM(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)

class PlatImmune(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)


class Music():
    mixer.init()
    mixer.music.load('bensound-summer_ogg_music.ogg')
    mixer.music.play()


if __name__ == "__main__":
    main_menu()
