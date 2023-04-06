import pygame
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

SCORE = 0

# Snake step size & growth rate
STEP_SIZE = 10

clock = pygame.time.Clock()
color = (0,255,0)

class Snake(pygame.sprite.Sprite):
    global STEP_SIZE
    def __init__(self,x,y):
        super().__init__()
        self.length = 1
        self.x = x
        self.y = y
        self.path = []
        self.path.append((self.x,self.y))
    def grow(self):
        self.length += 1
    def draw(self):
        global screen
        for x,y in self.path:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(x, y, 5, 5))
    def processPath(self):
         if len(self.path) > self.length:
              self.path.pop(0)
    def moveUp(self):
        self.y -= STEP_SIZE
        self.path.append((self.x,self.y))
        self.processPath()
    def moveDown(self):
        self.y += STEP_SIZE
        self.path.append((self.x,self.y))
        self.processPath()
    def moveRight(self):
        self.x += STEP_SIZE
        self.path.append((self.x,self.y))
        self.processPath()
    def moveLeft(self):
        self.x -= STEP_SIZE
        self.path.append((self.x,self.y))
        self.processPath()
    def position(self):
         return self.x,self.y

class Food(pygame.sprite.Sprite):
    def __init__(self):
        #self.circle = pygame.draw.circle(screen, (255,0,0), (200,200), 20, 5)
        super().__init__()
        
        # Load image
        image = pygame.image.load('coin.png')
        image = pygame.transform.scale(image, (30,30))

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 20)

    def reset(self):
       self.rect.top = 0
       self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 20)           

snake = Snake(10,10)
food = Food()

#Creating Sprites Groups
foods = pygame.sprite.Group()
foods.add(food)

all_sprites = pygame.sprite.Group()
all_sprites.add(snake)
all_sprites.add(food)

pygame.mixer.music.load("bite.mp3")

while not done:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        done = True
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            snake.moveUp()
            snake.draw()
        if pressed[pygame.K_DOWN]: 
            snake.moveDown()
            snake.draw()
        if pressed[pygame.K_LEFT]:
            snake.moveLeft()
            snake.draw()
        if pressed[pygame.K_RIGHT]:
            snake.moveRight()
            snake.draw()

        screen.fill((0, 0, 0))

        #Re-draws all Sprites
        for entity in foods:
            #entity.move()
            screen.blit(entity.image, entity.rect)

        #To be run if collision occurs between Snake and Food
        #if pygame.sprite.spritecollideany(snake, food):
        if pygame.Rect.collidepoint(food.rect, snake.position()):
            # Play eat sound
            pygame.mixer.music.play()
            SCORE += 1
            snake.grow()  
            # for coin in coins:
            #     coin.reset()        
            #pygame.display.update()

            food.reset()
            screen.blit(food.image, food.rect)
        
        

        #pygame.draw.rect(screen, color, pygame.Rect(x, y, 15, 15))
        snake.draw()
        
        pygame.display.flip()
        clock.tick(60)