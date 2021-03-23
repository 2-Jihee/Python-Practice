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
############################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()  # 초기화 (반드시 필요한 작업)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_hight = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_hight))

# 화면 타이틀 설정
pygame.display.set_caption("Bright HEE's Game")  # 게임이름

# FPS
clock = pygame.time.Clock()
############################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 둥)

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리
   
    # 5. 화면에 그리기

    pygame.display.update()

pygame.quit()