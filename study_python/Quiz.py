''' 
Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오.

[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS는 30으로 고정

[게임 이미지]
1. 배경 : 640 * 480 (세로 가로) - backround.png
2. 캐릭터 : 70 * 70 - character.png
3. 똥 : 70 * 70 - enemy.png
'''

import pygame
import random

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 둥)

pygame.init()
# 화면 크기 설정
screen_width = 480
screen_hight = 640
screen = pygame.display.set_mode((screen_width, screen_hight))

# 화면 타이틀 설정
pygame.display.set_caption("Bright HEE's Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/USER/Desktop/Git-PythonWorkspace/study_python/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/USER/Desktop/Git-PythonWorkspace/study_python/character.png")
character_size = character.get_rect().size 
character_width = character_size[0]
character_hight = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_hight - character_hight

# 이동할 좌표
to_x = 0

# 이동 속도
character_speed = 0.6


# 적 enemy 캐릭터
enemy = pygame.image.load("C:/Users/USER/Desktop/Git-PythonWorkspace/study_python/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0] 
enemy_hight = enemy_size[1]
enemy_x_pos = screen_width == 0
enemy_y_pos = screen_hight == 0

# 이벤트 루프
running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    to_x -= character_speed
                elif event.key == pygame.K_RIGHT:
                    to_x += character_speed


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0

    character_x_pos += to_x * dt

     # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리
   
    # 5. 화면에 그리기

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) 


    pygame.display.update()

pygame.quit()