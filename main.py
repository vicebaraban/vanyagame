import pygame
import sys
from enum import Enum, auto
import random


_all_sprites = pygame.sprite.Group()
_main_menu_sprites = pygame.sprite.Group()
_pause_menu_sprites = pygame.sprite.Group()
_playing_sprites = pygame.sprite.Group()
_lose_menu_sprites = pygame.sprite.Group()
_label_sprites = pygame.sprite.Group()


FPS = 60

count_items = 0
lose = False
health = 0


images = {'player': pygame.transform.scale(pygame.image.load('images/player2.png'), (168, 272)),
          'player2': pygame.transform.scale(pygame.image.load('images/player3.png'), (168, 272)),
          'player3': pygame.transform.scale(pygame.image.load('images/player4.png'), (168, 272)),
          'pena0': pygame.transform.scale(pygame.image.load('images/hard_player.png'), (210, 272)),
          'vano1': pygame.transform.scale(pygame.image.load('images/vano1.png'), (168, 272)),
          'vano2': pygame.transform.scale(pygame.image.load('images/vano2.png'), (168, 272)),
          'vano3': pygame.transform.scale(pygame.image.load('images/vano3.png'), (168, 272)),
          'vano4': pygame.transform.scale(pygame.image.load('images/vano4.png'), (168, 272)),
          'vano5': pygame.transform.scale(pygame.image.load('images/vano5.png'), (168, 272)),
          'vano6': pygame.transform.scale(pygame.image.load('images/vano6.png'), (168, 272)),
          'background_main_menu': pygame.transform.scale(pygame.image.load('images/background_main_menu.jpg'),
                                                         (800, 600)),
          'background_lose_menu': pygame.transform.scale(pygame.image.load('images/background_lose_menu.jpeg'),
                                                         (800, 600)),
          'background_wings': pygame.transform.scale(pygame.image.load('images/background_playing_wings.png'),
                                                     (800, 600)),
          'background_engine': pygame.transform.scale(pygame.image.load('images/background_playing_engine.png'),
                                                      (800, 600)),
          'background_jungle': pygame.transform.scale(pygame.image.load('images/background_playing_jungle.jpeg'),
                                                      (800, 600)),
          'background_hard': pygame.transform.scale(pygame.image.load('images/background_hard.jpg'), (800, 600)),
          'cursor': pygame.transform.scale(pygame.image.load('images/cursor.png'), (60, 60)),
          'button_jungle': pygame.transform.scale(pygame.image.load('images/button_jungle.png'), (280, 70)),
          'button_jungle_on': pygame.transform.scale(pygame.image.load('images/button_jungle_on.png'), (280, 70)),
          'button_engine': pygame.transform.scale(pygame.image.load('images/button_engine.png'), (280, 70)),
          'button_engine_on': pygame.transform.scale(pygame.image.load('images/button_engine_on.png'), (280, 70)),
          'button_wings': pygame.transform.scale(pygame.image.load('images/button_wings.png'), (280, 70)),
          'button_wings_on': pygame.transform.scale(pygame.image.load('images/button_wings_on.png'), (280, 70)),
          'button_exit': pygame.transform.scale(pygame.image.load('images/button_exit.png'), (60, 60)),
          'button_exit_on': pygame.transform.scale(pygame.image.load('images/button_exit_on.png'), (60, 60)),
          'button_play': pygame.transform.scale(pygame.image.load('images/button_play.png'), (60, 60)),
          'button_play_on': pygame.transform.scale(pygame.image.load('images/button_play_on.png'), (60, 60)),
          'button_clear': pygame.transform.scale(pygame.image.load('images/button_clear.png'), (60, 60)),
          'item_jungle': pygame.transform.scale(pygame.image.load('images/item_jungle.png'), (150, 160)),
          'banana_hard': pygame.transform.scale(pygame.image.load('images/banana_hard.png'), (180, 160)),
          'hard1': pygame.transform.scale(pygame.image.load('images/hard-mode-1.jpg'), (800, 600)),
          'hard2': pygame.transform.scale(pygame.image.load('images/hard-mode-2.jpg'), (800, 600)),
          'hard3': pygame.transform.scale(pygame.image.load('images/hard-mode-3.jpg'), (800, 600)),
          'hard4': pygame.transform.scale(pygame.image.load('images/hard-mode-4.jpg'), (800, 600)),
          'hard5': pygame.transform.scale(pygame.image.load('images/hard-mode-5.jpg'), (800, 600)),
          'hard6': pygame.transform.scale(pygame.image.load('images/hard-mode-6.jpg'), (800, 600)),
          'hard7': pygame.transform.scale(pygame.image.load('images/hard-mode-7.jpg'), (800, 600)),
          'hard8': pygame.transform.scale(pygame.image.load('images/hard-mode-8.jpg'), (800, 600)),
          'hard9': pygame.transform.scale(pygame.image.load('images/hard-mode-9.jpg'), (800, 600)),
          'hard10': pygame.transform.scale(pygame.image.load('images/hard-mode-10.jpg'), (800, 600)),
          'hard11': pygame.transform.scale(pygame.image.load('images/hard-mode-11.jpg'), (800, 600)),
          'pena1': pygame.transform.scale(pygame.image.load('images/pena1.png'), (210, 272)),
          'pena2': pygame.transform.scale(pygame.image.load('images/pena2.png'), (210, 272)),
          'pena3': pygame.transform.scale(pygame.image.load('images/pena3.png'), (210, 272)),
          'pena4': pygame.transform.scale(pygame.image.load('images/pena4.png'), (210, 272)),
          'pena5': pygame.transform.scale(pygame.image.load('images/pena5.png'), (210, 272)),
          'lose_hard_1': pygame.transform.scale(pygame.image.load('images/lose1.png'), (210, 272)),
          'lose_hard_2': pygame.transform.scale(pygame.image.load('images/lose2.png'), (210, 272)),
          'lose_hard_3': pygame.transform.scale(pygame.image.load('images/lose3.png'), (210, 272)),
          'lose_hard_4': pygame.transform.scale(pygame.image.load('images/lose4.png'), (210, 272)),
          'lose_hard_5': pygame.transform.scale(pygame.image.load('images/lose5.png'), (210, 272)),
          'lose_hard_6': pygame.transform.scale(pygame.image.load('images/lose6.png'), (210, 272)),
          'lose_hard_7': pygame.transform.scale(pygame.image.load('images/lose7.png'), (210, 272)),
          'lose_hard_8': pygame.transform.scale(pygame.image.load('images/lose8.png'), (210, 272)),
          'lose_hard_9': pygame.transform.scale(pygame.image.load('images/lose9.png'), (210, 272))}


pygame.mixer.init()
sounds = {'player_eat': pygame.mixer.Sound('sounds/player_eat.mp3'),
          'hard_player_eat': pygame.mixer.Sound('sounds/hard_player_eat.mp3'),
          'hard_pass': pygame.mixer.Sound('sounds/hard_pass.mp3'),
          'hard_label': pygame.mixer.Sound('sounds/hard_label.mp3'),
          'hard_lose': pygame.mixer.Sound('sounds/hard_lose.mp3'),
          'lose_menu': pygame.mixer.Sound('sounds/lose_menu.mp3'),
          'button': pygame.mixer.Sound('sounds/button.mp3'),
          'button_on': pygame.mixer.Sound('sounds/button_on.mp3'),
          'normal_lose': pygame.mixer.Sound('sounds/lose_normal.mp3'),
          'hard': pygame.mixer.Sound('sounds/hard.mp3'),
          'engine': pygame.mixer.Sound('sounds/engine.mp3'),
          'jungle': pygame.mixer.Sound('sounds/jungle.mp3'),
          'wings': pygame.mixer.Sound('sounds/wings.mp3'),
          'normal_pass': pygame.mixer.Sound('sounds/normal_pass.mp3'),
          'main_menu': pygame.mixer.Sound('sounds/main_menu.mp3')}


def draw_text(surf, text, size, color, x, y):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class GameState(Enum):
    MAIN_MENU = auto()
    PLAYING = auto()
    PAUSE = auto()
    LOSE = auto()


class Game:
    def __init__(self):
        pygame.init()
        self.running = False
        self._init_screen()
        self.clock = pygame.time.Clock()
        self.game_state = GameState.MAIN_MENU
        pygame.mouse.set_visible(False)
        self._init_main_menu()
        self.playing_mode = 0
        self._animator = Animator()

    def run(self):
        self.running = True
        while self.running:
            self._main_loop()
        self._terminate()

    def _main_loop(self):
        global lose
        # _all_sprites.update()
        if lose:
            lose = False
            self.game_state = GameState.MAIN_MENU
            self._init_main_menu()
        self._process_events()
        self._render_screen()
        self.clock.tick(FPS)

    def _process_events(self):
        self._events = pygame.event.get()
        if self.game_state == GameState.MAIN_MENU:
            self._main_menu_process_events(self._events)
        elif self.game_state == GameState.PLAYING:
            self._playing_process_events(self._events)
        elif self.game_state == GameState.PAUSE:
            self._pause_menu_process_events(self._events)
        elif self.game_state == GameState.LOSE:
            self._lose_menu_process_events(self._events)

    def _main_menu_process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self._terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._button_exit.in_mouse():
                    self._terminate()
                if self._button_jungle.in_mouse():
                    pygame.mixer.Channel(3).play(sounds['button_on'])
                    self.game_state = GameState.PLAYING
                    self.playing_mode = 0
                    self._init_playing()
                if self._button_engine.in_mouse():
                    pygame.mixer.Channel(3).play(sounds['button_on'])
                    self.game_state = GameState.PLAYING
                    self.playing_mode = 1
                    self._init_playing()
                if self._button_wings.in_mouse():
                    pygame.mixer.Channel(3).play(sounds['button_on'])
                    self.game_state = GameState.PLAYING
                    self.playing_mode = 2
                    self._init_playing()

    def _pause_menu_process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self._terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._button_play.in_mouse():
                    pygame.mixer.Channel(3).play(sounds['button_on'])
                    self.game_state = GameState.PLAYING
                    _pause_menu_sprites.update(kill=True)
                if self._button_menu.in_mouse():
                    pygame.mixer.Channel(3).play(sounds['button_on'])
                    self.game_state = GameState.MAIN_MENU
                    self._init_main_menu()

    def _lose_menu_process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self._terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._button_menu.in_mouse():
                    pygame.mixer.Channel(3).play(sounds['button_on'])
                    self.game_state = GameState.MAIN_MENU
                    self._init_main_menu()

    def _playing_process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self._terminate()
            if event.type in (pygame.KEYUP, pygame.KEYDOWN):
                if event.key in (pygame.K_ESCAPE, pygame.K_SPACE):
                    self.game_state = GameState.PAUSE
                    self._init_pause_menu()

    def _init_screen(self):
        self._screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('vanyagame')

    def _init_pause_menu(self):
        self._button_play = Button(images['button_play'], images['button_play_on'], (320, 300), _pause_menu_sprites)
        self._button_menu = Button(images['button_exit'], images['button_exit_on'], (400, 300), _pause_menu_sprites)

    def _init_lose_menu(self, hard=False):
        pygame.mixer.Channel(5).stop()
        if not hard:
            self._lose_animation = Animation(self._player, 1.5, [images[f'vano{i}'] for i in range(1, 7)])
            pygame.mixer.Channel(1).play(sounds['normal_lose'])
        else:
            self._lose_animation = Animation(self._player, 2.2, [images[f'lose_hard_{i}'] for i in range(1, 10)])
            pygame.mixer.Channel(1).play(sounds['hard_lose'])
        self._end_animation = False
        self._animator.add_animation(self._lose_animation)
        self._button_menu = Button(images['button_exit'], images['button_exit_on'], (370, 400), _lose_menu_sprites)

    def _init_main_menu(self):
        _all_sprites.update(kill=True)
        self._button_jungle = Button(images['button_jungle'], images['button_jungle_on'], (250, 185),
                                     _main_menu_sprites)
        self._button_engine = Button(images['button_engine'], images['button_engine_on'], (250, 265),
                                     _main_menu_sprites)
        self._button_wings = Button(images['button_wings'], images['button_wings_on'], (250, 350), _main_menu_sprites)
        self._button_exit = Button(images['button_exit'], images['button_exit_on'], (720, 20), _main_menu_sprites)
        pygame.mixer.Channel(5).play(sounds['main_menu'], -1)

    def _init_playing(self):
        global count_items, health
        health = 0
        count_items = 0
        self.cd = self.gcd = 0
        _all_sprites.update(kill=True)
        Item(images['item_jungle'], random.randint(6, 12), _playing_sprites)
        self._player = Player((images['player'], images['player2'], images['player3']), _playing_sprites)
        self._button_clear = Button(images['button_clear'], images['button_clear'], (700, 40), _playing_sprites)
        pygame.mixer.Channel(5).play([sounds['jungle'], sounds['engine'], sounds['wings']][self.playing_mode], -1)

    def _init_hard_playing(self):
        global health
        health = 0
        self.cd = self.gcd = 0
        self.playing_mode = 3
        _all_sprites.update(kill=True)
        pygame.mixer.Channel(5).stop()
        self._player = Player([images[f'pena{i}'] for i in range(6)], _playing_sprites)
        self._button_clear = Button(images['button_clear'], images['button_clear'], (700, 40), _playing_sprites)
        self._hard_label = Button(images['hard1'], images['hard1'], (0, 0), _label_sprites)
        self._end_animation = False
        self._hard_label_animation = Animation(self._hard_label, 2, [images[f'hard{i}'] for i in range(2, 12)])
        self._animator.add_animation(self._hard_label_animation)
        pygame.mixer.Channel(1).play(sounds['hard_label'])

    def _render_playing(self):
        global health, count_items
        if count_items == 1 and self.playing_mode != 3:
            _playing_sprites.update()
            self._init_hard_playing()
        elif self.playing_mode == 3:
            if self._hard_label_animation in self._animator.urn:
                self._end_animation = True
                self._hard_label.kill()
                pygame.mixer.Channel(5).play(sounds['hard'], -1)
            if self._end_animation:
                _playing_sprites.update()
                if health == 6:
                    health = 0
                    self.game_state = GameState.LOSE
                    self._init_lose_menu(hard=True)
                if self.cd == 0:
                    self.gcd = random.randint(20, 50)
                    self.cd = 1
                elif self.cd == self.gcd:
                    self.cd = 0
                    Item(images['banana_hard'], 1, random.randint(14, 20), _playing_sprites)
                else:
                    self.cd += 1
            self._screen.blit(images['background_hard'], (0, 0))
            _playing_sprites.draw(self._screen)
            draw_text(self._screen, str(count_items), 56, (150, 75, 0), 730, 36)
            _label_sprites.draw(self._screen)
        else:
            _playing_sprites.update()
            if health == 3:
                health = 0
                self.game_state = GameState.LOSE
                self._init_lose_menu()
            if self.cd == 0:
                self.gcd = random.randint(60, 140)
                self.cd = 1
            elif self.cd == self.gcd:
                self.cd = 0
                Item(images['item_jungle'], 0, random.randint(6, 12), _playing_sprites)
            else:
                self.cd += 1
            background = ['background_jungle', 'background_engine', 'background_wings'][self.playing_mode]
            self._screen.blit(images[background], (0, 0))
            _playing_sprites.draw(self._screen)
            draw_text(self._screen, str(count_items), 56, (150, 75, 0), 730, 36)

    def _terminate(self):
        pygame.quit()
        sys.exit()

    def _render_screen(self):
        # self._screen.blit()
        self._animator.update()
        if self.game_state == GameState.MAIN_MENU:
            self._render_main_menu()
        elif self.game_state == GameState.PLAYING:
            self._render_playing()
        elif self.game_state == GameState.PAUSE:
            self._render_pause_menu()
        elif self.game_state == GameState.LOSE:
            self._render_lose_menu()
        pygame.display.flip()

    def _render_lose_menu(self):
        if self._lose_animation in self._animator.urn:
            self._end_animation = True
            pygame.mixer.Channel(5).play(sounds['lose_menu'])
        if self._end_animation:
            _lose_menu_sprites.update()
            self._screen.blit(images['background_lose_menu'], (0, 0))
            _lose_menu_sprites.draw(self._screen)
            draw_text(self._screen, str(count_items), 80, (255, 0, 0), 400, 100)
            if pygame.mouse.get_focused():
                self._screen.blit(images['cursor'], pygame.mouse.get_pos())
        else:
            background = ['background_jungle', 'background_engine',
                          'background_wings', 'background_hard'][self.playing_mode]
            self._screen.blit(images[background], (0, 0))
            _playing_sprites.draw(self._screen)
            draw_text(self._screen, str(count_items), 56, (155, 75, 0), 730, 36)

    def _render_main_menu(self):
        _main_menu_sprites.update()
        self._screen.blit(images['background_main_menu'], (0, 0))
        _main_menu_sprites.draw(self._screen)
        if pygame.mouse.get_focused():
            self._screen.blit(images['cursor'], pygame.mouse.get_pos())

    def _render_pause_menu(self):
        _pause_menu_sprites.update()
        background = ['background_jungle', 'background_engine',
                      'background_wings', 'background_hard'][self.playing_mode]
        self._screen.blit(images[background], (0, 0))
        _pause_menu_sprites.draw(self._screen)
        if pygame.mouse.get_focused():
            self._screen.blit(images['cursor'], pygame.mouse.get_pos())


class Animator:
    def __init__(self):
        self.storage_animations = []
        self.urn = []

    def update(self):
        self.urn = []
        for animation in self.storage_animations:
            if animation.update() == 0:
                self.urn.append(animation)
        if self.storage_animations and self.urn:
            for animation in self.urn:
                self.storage_animations.remove(animation)

    def add_animation(self, animation):
        self.storage_animations.append(animation)


class Animation:
    def __init__(self, obj, time: float, anim_images):
        self.images = anim_images
        self.obj = obj
        self.time = int(FPS * time)
        self.speed = self.time // len(self.images) + (1 if self.time % len(self.images) != 0 else 0)
        self.counter = 0

    def update(self):
        if self.counter % self.speed == 0:
            self.obj.change_image(self.images[self.counter // self.speed])
        self.counter += 1
        if self.counter == self.time - 1:
            return 0
        return 1


class Player(pygame.sprite.Sprite):
    def __init__(self, sprites, *groups):
        super().__init__(_all_sprites, *groups)
        self.x, self.y = 10, 0
        self.sprites = sprites
        self._init_sprite(sprites[0])

    def _init_sprite(self, sprite_img):
        self.image = sprite_img
        self.rect = self.image.get_rect().move(self.x, self.y)

    def change_image(self, img):
        self.image = img

    def update(self, kill=False):
        global health
        if kill:
            self.kill()
        self.image = self.sprites[health]
        self.y = pygame.mouse.get_pos()[1]
        self.rect = self.image.get_rect().move(self.x, self.y)


class Item(pygame.sprite.Sprite):
    def __init__(self, sprite_img, mode, speed, *groups):
        super().__init__(_all_sprites, *groups)
        self.x, self.y = 680, random.randint(10, 440)
        self._init_sprite(sprite_img)
        self.speed = speed
        self.mode = mode
        self.out = False

    def _init_sprite(self, sprite_img):
        self.image = sprite_img
        self.rect = self.image.get_rect().move(self.x, self.y)

    def change_image(self, img):
        self.image = img

    def update(self, kill=False):
        global count_items, lose, health
        if kill:
            self.kill()
        else:
            if self.x <= -150:
                self.kill()
            self.rect = self.image.get_rect().move(self.x - self.speed, self.y)
            self.x, self.y = self.rect.x, self.rect.y
            player_y = pygame.mouse.get_pos()[1]
            if self.x <= 140 and not self.out:
                if self.y in range(player_y - 100, player_y - 20) and not self.out:
                    self.kill()
                    if self.mode == 0:
                        pygame.mixer.Channel(0).play(sounds['player_eat'])
                    else:
                        pygame.mixer.Channel(0).play(sounds['hard_player_eat'])
                    count_items += 1
                elif self.x <= -100:
                    if self.mode == 0:
                        pygame.mixer.Channel(0).play(sounds['normal_pass'])
                    else:
                        pygame.mixer.Channel(1).play(sounds['hard_pass'])
                    health += 1
                    self.out = True


class Button(pygame.sprite.Sprite):
    def __init__(self, sprite_img, sprite_image_on, pos, *groups):
        super().__init__(_all_sprites, *groups)
        self.image = sprite_img
        self.x1, self.y1 = pos[0], pos[1]
        self.x2, self.y2 = pos[0] + self.image.get_rect().bottomright[0], pos[1] + self.image.get_rect().bottomright[1]
        self.sprite_img = sprite_img
        self.sprite_img_on = sprite_image_on
        self._init_sprite(self.sprite_img)
        self.active = False

    def _init_sprite(self, sprite_img):
        self.image = sprite_img
        self.rect = self.image.get_rect().move(self.x1, self.y1)

    def change_image(self, img):
        self.image = img

    def in_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()[0] + 30, pygame.mouse.get_pos()[1]
        if self.x1 <= mouse_x <= self.x2 and self.y1 <= mouse_y <= self.y2:
            return True
        return False

    def update(self, kill=False):
        if kill:
            self.kill()
        if self.in_mouse() and not self.active:
            self._init_sprite(self.sprite_img_on)
            self.active = True
            pygame.mixer.Channel(1).play(sounds['button'])
        elif self.active and not self.in_mouse():
            self._init_sprite(self.sprite_img)
            self.active = False


if __name__ == '__main__':
    app = Game()
    app.run()
