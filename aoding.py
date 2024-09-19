pip install pygame
import pygame
import sys

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置游戏标题
pygame.display.set_caption("简化版超级玛丽")

# 加载资源（例如角色、背景、障碍物等）
mary_image = pygame.image.load('mary.png').convert_alpha()
enemy_image = pygame.image.load('enemy.png').convert_alpha()

# 角色和障碍物类（简化版）
class Character:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# 创建角色和障碍物实例
mary = Character(100, 500, mary_image)
enemy = Character(700, 300, enemy_image)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 清除屏幕
    screen.fill((255, 255, 255))

    # 绘制角色和障碍物
    mary.draw(screen)
    enemy.draw(screen)

    # 更新屏幕显示
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(60)

# 退出pygame
pygame.quit()
sys.exit()
