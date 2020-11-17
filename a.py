from b import *
import sys
import pygame
from pygame.locals import QUIT

def isCollision(Rect1, Rect2):
    if(pygame.Rect.colliderect(Rect1, Rect2)):
        return True
    return False

def resetGame():
    global game_mode,dx, dy,score
    game_mode = 0
    score = 0
    dx = BALL_SPEED
    dy = -BALL_SPEED

SCREEN_SIZEX = 800
SCREEN_SIZEY = 600
SCREEN_COLOR = (0,0,0)
clock = pygame.time.Clock()

pygame.init()

window_surface = pygame.display.set_mode((SCREEN_SIZEX,SCREEN_SIZEY))
window_surface.fill(SCREEN_COLOR)

paddle_x = 0
paddle_y = (SCREEN_SIZEY - 48)
paddle = Paddle(window_surface, [paddle_x, paddle_y, 100, 6])

BALL_SPEED = 8
dx = BALL_SPEED
dy = -BALL_SPEED

score = 0
pygame.font.init()
text = pygame.font.SysFont("None", 25)


ball_x = paddle_x
ball_y = paddle_y
ball = Ball(window_surface, [ball_x, ball_y], 8)
qq = pygame.image.load('qq.png')
qq = pygame.transform.scale(qq, (100, 130))

pygame.display.update()



# 鼠標 鎖定 和 隱藏
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)
resetGame()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        
        if event.type == pygame.MOUSEMOTION:
            paddle_x = pygame.mouse.get_pos()[0] - 50        
        if event.type == pygame.MOUSEBUTTONDOWN:
                if(game_mode == 0):
                    game_mode = 1  
                    

    
    window_surface.fill(SCREEN_COLOR)
    qq_size = qq.get_size()
    qq_rect = window_surface.blit(qq,(SCREEN_SIZEX/2 - qq_size[0]/2,SCREEN_SIZEY/2 - qq_size[1]/2-100))
    #文字渲染成塗層
    scoreboard = text.render("Score = " + str(score), 1, (255,25,255))
#在畫面上繪製
    window_surface.blit(scoreboard,(10,10))

    paddle.rect[0] = paddle_x
    if(isCollision(ball.rect, paddle.rect)):
        dy = -dy

    if game_mode==0:
        ball.pos[0] = ball_x = paddle.rect[0] + ((paddle.rect[2] - ball.radius)>>1)
        ball.pos[1] = ball_y = paddle.rect[1] - ball.radius
    elif score>=5:
        resetGame()
    else:
       
    #判斷死亡.
        if(ball_y + dy > SCREEN_SIZEY - ball.radius):
            resetGame()
            game_mode=0
    # 右牆或左牆碰撞.
        if(ball_x + dx > SCREEN_SIZEX - ball.radius or ball_x + dx < ball.radius):
            dx = -dx
        # 下牆或上牆碰撞
        if(ball_y + dy < -ball.radius):
            dy = -dy
        if(isCollision(qq_rect, ball.rect)):
            score+=1
            if ball.pos[1] > qq_rect[1]+qq_rect[3] or ball.pos[1] < qq_rect[1]:
                dy = - dy
            else:
                dx = - dx
        ball_x += dx
        ball_y += dy
        ball.pos[0] = ball_x
        ball.pos[1] = ball_y


    paddle.update()
    ball.update()
    pygame.display.update()
    clock.tick(60)
    

