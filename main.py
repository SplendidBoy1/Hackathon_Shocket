import pygame
from random import randint
import time

card_width = pygame.image.load('id_card.png').get_width() // 3.2
card_height = pygame.image.load('id_card.png').get_height() // 3.2


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height) #rectangle
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def outline(self, frame_color, thickness): #outline of an existing rectangle
        pygame.draw.rect(window, frame_color, self.rect, thickness)   
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)      

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Card(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (card_width, card_height))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x 
        self.rect.y = y 

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Deck():
    def __init__(self):
        self.cards = []

    def shuffle(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.init_dect()

    def init_dect(self):
        init_pos = width // 2 - card_width // 2 * 2 - 100
        id_card = Card(init_pos, height - card_height // 2 + 30, pygame.image.load('id_card.png'))
        medical_card = Card(init_pos + card_width // 2 + 30, height - card_height // 2 + 30, pygame.image.load('medical_record.png'))
        payment_card = Card(init_pos + card_width // 2 * 2 + 30 * 2, height - card_height // 2 + 30, pygame.image.load('payment.png'))
        white_card = Card(init_pos + card_width // 2 * 3 + 30 * 3, height - card_height // 2 + 30, pygame.image.load('white_hat.png'))
        self.hand.append(id_card)
        self.hand.append(medical_card)
        self.hand.append(payment_card)
        self.hand.append(white_card)

    def draw(self, window):
        for card in self.hand:
            card.draw(window)

    def update(self):
        pass

    def play(self):
        pass

pygame.init()
window = pygame.display.set_mode((800, 360), pygame.RESIZABLE)
pygame.display.set_caption('STOP LEAKING DATA')
#background = transform.scale(image.load(), (800, 360))
clock = pygame.time.Clock()

running = True

width = window.get_width()
height = window.get_height()

player1 = Player('Player1')

prev_card = None

deck_card = Card(width // 2 - card_width // 2 - 200, height // 2 - card_width // 2, pygame.image.load('back.png'))
deck_card.resize(card_width // 2, card_height // 2)

choose_card = False

start_time = time.time()
curr_time = start_time

duration = 15

timer = Label(0, 0, 100, 50, (255, 255, 255))
timer.set_text(str(duration), 130, (255, 0, 0))


while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            if deck_card.rect.collidepoint(x, y):
                    print(randint(1, 6))
                    if prev_card:
                        prev_card.rect.y += card_height // 2
                        prev_card = None
                    break
            for card in player1.hand:
                if card.rect.collidepoint(x, y):
                    card.rect.y -= card_height // 2

                    if prev_card:
                        prev_card.rect.y += card_height // 2
                    prev_card = card 
                    choose_card = True
                    break                                                   

    window.fill((255, 255, 255))

    for card in player1.hand:
        if card != prev_card and prev_card:
            card.draw(window)
        else:
            card.draw(window)
    if prev_card:
        prev_card.draw(window)

    # Draw timer
    new_time = time.time()
    if int(new_time - start_time) <= duration:
        timer.set_text(str(duration - int(new_time - start_time)), 130, (255, 0, 0))
        curr_time = new_time
    else:
        timer.set_text('Other\'s turn', 50, (255, 0, 0))

    timer.draw(width // 2, height // 2 - 100)        
    deck_card.draw(window)
    pygame.display.update()
    clock.tick(60)