import pygame
import Init
import Ball
import Field
import Circle
import CurrentCircle
import NextCircle
import time

def check_game_over(balls, y):
    result = False
    for ball in balls:
        ball_top = ball.body.position[1] + ball.shape.radius
        if(ball_top >= y):
            result = True
            break
    return result

def collide(arbiter, space, data):
    # collided shapes
    a, b = arbiter.shapes
    # collision type
    a_ct = a.collision_type
    b_ct = b.collision_type
    # 衝突処理を実施しない場合を判定
    if(a_ct != b_ct):
        # 異なるBall同士の衝突の場合
        return
    if(a_ct == 11 or b_ct == 11):
        # Ball11同士の衝突の場合
        return
    # 衝突座標を算出
    a_x, a_y = a.body.position
    b_x, b_y = b.body.position
    x = (a_x + b_x) / 2
    y = (a_y + b_y) / 2
    # 削除するBallを求める
    balls_to_remove = []
    for ball in data["balls"]:
        if(ball.shape == a or ball.shape == b):
            balls_to_remove.append(ball)
    # Ballを削除する
    for ball in balls_to_remove:
        space.remove(ball.shape, ball.body)
        data["balls"].remove(ball)
    # Ballの作成かつスコア更新
    if(a_ct == 1 and b_ct == 1):
        data["balls"].append(Ball.Ball02(x, y))
        data["score"] += 1
    elif(a_ct == 2 and b_ct == 2):
        data["balls"].append(Ball.Ball03(x, y))
        data["score"] += 3
    elif(a_ct == 3 and b_ct == 3):
        data["balls"].append(Ball.Ball04(x, y))
        data["score"] += 6
    elif(a_ct == 4 and b_ct == 4):
        data["balls"].append(Ball.Ball05(x, y))
        data["score"] += 10
    elif(a_ct == 5 and b_ct == 5):
        data["balls"].append(Ball.Ball06(x, y))
        data["score"] += 15
    elif(a_ct == 6 and b_ct == 6):
        data["balls"].append(Ball.Ball07(x, y))
        data["score"] += 21
    elif(a_ct == 7 and b_ct == 7):
        data["balls"].append(Ball.Ball08(x, y))
        data["score"] += 28
    elif(a_ct == 8 and b_ct == 8):
        data["balls"].append(Ball.Ball09(x, y))
        data["score"] += 36
    elif(a_ct == 9 and b_ct == 9):
        data["balls"].append(Ball.Ball10(x, y))
        data["score"] += 45
    elif(a_ct == 10 and b_ct == 10):
        data["balls"].append(Ball.Ball11(x, y))
        data["score"] += 55
    pass

def game():
    # Field
    tlx, tly = 100, 450
    brx, bry = 400, 100
    field = Field.Field(tlx, tly, brx, bry)

    # Ball
    balls = []

    # CollisionHandler
    handler = Init.space.add_default_collision_handler()
    handler.data["balls"] = balls
    handler.data["score"] = 0
    handler.post_solve = collide

    # Sample Ball
    cx, cy = 600, 200
    sample_circles = [
        Circle.Circle(cx, cy, Init.color_01, Init.radius_01),
        Circle.Circle(cx, cy, Init.color_02, Init.radius_01),
        Circle.Circle(cx, cy, Init.color_03, Init.radius_01),
        Circle.Circle(cx, cy, Init.color_04, Init.radius_01),
        Circle.Circle(cx, cy, Init.color_05, Init.radius_01),
        Circle.Circle(cx, cy, Init.color_06, Init.radius_01),
        Circle.Circle(cx, cy, Init.color_07, Init.radius_01),
        Circle.Circle(cx, cy, Init.color_08, Init.radius_01),
        Circle.Circle(cx, cy, Init.color_09, Init.radius_01),
        Circle.Circle(cx, cy, Init.color_10, Init.radius_01),
        Circle.Circle(cx, cy, Init.color_11, Init.radius_01),
    ]
    for i, ball in enumerate(sample_circles):
        d = -30 + (-30) * i
        x, y = Init.rotate_cordinates((0, 100), d)
        ball.x += x
        ball.y += y
        pass

    # Current Circle
    current_circle = CurrentCircle.CurrentCircle(
        tlx + (brx - tlx) / 2,
        tly + Init.radius_06,
        Init.color_01,
        Init.radius_01,
        tlx + Init.radius_06,
        brx - Init.radius_06
    )

    # Next Circle
    next_circle = NextCircle.NextCircle(cx, cx)

    # Common Font
    font = pygame.font.SysFont(None, 50)
    # Next Text
    next_text = font.render("Next", True, Init.BLACK)
    next_rect = next_text.get_rect(
        midbottom=Init.convert_cordinates((cx, cx+Init.radius_06))
    )

    # Game Over Custom Event
    CHECKGAMEOVER = pygame.USEREVENT + 1
    # Game Over Flag
    GAMEOVERFLAG = False

    # Game Start
    while(not GAMEOVERFLAG):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return
            if(pygame.key.get_pressed()[pygame.K_DOWN]):
                # Drop Current Circle
                balls.append(current_circle.get_ball())
                # Update Current Circle
                current_circle.color = next_circle.color
                current_circle.radius = next_circle.radius
                # Update Next Circle
                next_circle.update()
                # Set Game Over Custom Event
                pygame.time.set_timer(CHECKGAMEOVER, 1000)
            if(event.type == CHECKGAMEOVER):
                # Check Game Over
                GAMEOVERFLAG = check_game_over(balls, tly)
        # Fiil background
        Init.display.fill(Init.WHEAT)

        # Draw Field
        field.draw()

        # Draw Ball
        for ball in balls:
            ball.draw()

        # Draw Sample Ball
        for ball in sample_circles:
            ball.draw()

        # Draw Current Circle
        current_circle.draw()
        current_circle.handle_keys()

        # Draw Next Circle
        next_circle.draw()

        # Draw Next Text
        Init.display.blit(next_text, next_rect)

        # Draw Score Text
        score_text = font.render("Score: {:,}".format(handler.data["score"]), True, Init.BLACK)
        score_rect = score_text.get_rect(
            bottomleft=Init.convert_cordinates((tlx, cx+Init.radius_06))
        )
        Init.display.blit(score_text, score_rect)

        # Display Update
        pygame.display.update()
        Init.clock.tick(Init.FPS)
        Init.space.step(1/Init.FPS)
    
    # Game Over Text
    game_over_text = font.render("Game Over", True, Init.BLACK)
    game_over_rect = game_over_text.get_rect(
        midbottom=(Init.disp_size[0]/2, Init.disp_size[1]/2)
    )
    # Draw Game Over Text
    Init.display.blit(game_over_text, game_over_rect)
    pygame.display.update()
    time.sleep(5)

if __name__ == '__main__':
    game()
    pygame.quit()