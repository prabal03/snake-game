import pygame
import random

pygame.init()
# creating window
screen_width = 600
screen_height = 400
pygame.mixer.init()
# colors
white = (255, 255, 255)
red1 = (255, 0, 0)
red = (0, 200, 200)
black = (0, 0, 0)
gameWindow = pygame.display.set_mode((screen_width, screen_height))
# inserting image
image = pygame.image.load("snake2.jpeg")
image1 = pygame.image.load("snake1.jpeg")
image = pygame.transform.scale(image, (screen_width, screen_height)).convert_alpha()
image1 = pygame.transform.scale(image1, (screen_width, screen_height)).convert_alpha()
# Game title
pygame.display.set_caption('Snake Game')
pygame.display.update()

# handling score inside the screen
font = pygame.font.SysFont('comicsansms', 20)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snake_lst, snake_size):
    for x, y in snake_lst:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])


def welcome():
    clock = pygame.time.Clock()
    exit_game = True
    while exit_game:

        gameWindow.blit(image1, (0, 0))

        text_screen("Welcome To The Snake Game ! !", white, 70, 20)
        text_screen("press spacebar to continue", white, 70, 70)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("On My Way.mp3")
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()
        clock.tick(10)


# event handling
def game_loop():
    with open("HighScore.txt", "r") as f:
        HighScore = f.read()
    # game variables
    score = 0
    exit_game = True
    game_over = False
    game_win = False
    snake_x = 40
    snake_y = 55
    snake_size = 8
    food_size = 5
    food_radius = 6
    fps = 15
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(6, screen_width)
    food_y = random.randint(6, screen_height)
    # creating clock
    clock = pygame.time.Clock()

    snake_lst = []
    snake_len = 1


    while exit_game:
        if game_win:
            gameWindow.fill(white)
            text_screen("YOU WIN!! Press ENTER To Play Again", black, 100, 150)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = False
        elif game_over:
            with open("HighScore.txt", "w") as f:
                f.write(str(HighScore))
            gameWindow.fill(black)
            text_screen("GAME OVER Press ENTER To Continue", white, 100, 150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        welcome()
                        pygame.quit()
                        quit()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = False
                if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    velocity_x = 9
                    velocity_y = 0
                if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    velocity_y = 9
                    velocity_x = 0
                if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    velocity_x = -9
                    velocity_y = 0
                if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    velocity_y = -9
                    velocity_x = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs((food_x - snake_x)) < 10 and abs((food_y - snake_y)) < 10:
                score += 10
                snake_len += 4
                food_x = random.randint(250, screen_width)
                food_y = random.randint(10, screen_height)
            if score == 50 :
                fps = 25
            if score == 100 :
                fps = 35

            if score > int(HighScore):
                HighScore = score


            # window color

            gameWindow.blit(image, (0, 0))
            text_screen("score is: " + str(score), black, 5, 5)
            text_screen("High Score : " + str(HighScore), black, 200, 5)

            pygame.draw.circle(gameWindow, red1, [food_x, food_y], food_radius, food_size)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_lst.append(head)

            if len(snake_lst) > snake_len:
                del snake_lst[0]
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height or head in snake_lst[
                                                                                                          :-1]:
                game_over = True
                pygame.mixer.music.load("Strong.mp3")
                pygame.mixer.music.play()
            if score == 25:
                game_win = True
            # ploting snake in game window
            plot_snake(gameWindow, red1, snake_lst, snake_size)

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


welcome()
