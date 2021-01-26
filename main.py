import time
import pygame
from random import randint
from player import Player
from movement import Movement
from constants import *
from puck import Puck
from vector_math import *


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Hockey')
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    running = True
    v = 100
    fps = 120
    clock = pygame.time.Clock()
    w = pygame.Color("white")
    first_coef, second_coef = 1, 1
    first = Player([width / 4, height / 2], 50, 1, height, width)
    second = Player([3 * width / 4, height / 2], 50, 0, height, width)
    puck = Puck([width / 2 + 95, height / 2] if randint(0, 1) else [width / 2 - 95, height / 2], [first, second], 25, height, width)
    first_score, second_score = 0, 0
    main_font = pygame.font.Font(None, 36)
    is_animated = 1
    animation_color = [55, 55, 55, 255]
    puck_radius = 50
    animation_radius = 50

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    first.change_movement().change_y(-NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_a:
                    first.change_movement().change_x(-NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_s:
                    first.change_movement().change_y(NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_d:
                    first.change_movement().change_x(NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_UP:
                    second.change_movement().change_y(-NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_LEFT:
                    second.change_movement().change_x(-NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_DOWN:
                    second.change_movement().change_y(NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_RIGHT:
                    second.change_movement().change_x(NORMAL_MOVEMENT * second_coef)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    first.change_movement().change_y(NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_a:
                    first.change_movement().change_x(NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_s:
                    first.change_movement().change_y(-NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_d:
                    first.change_movement().change_x(-NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_UP:
                    second.change_movement().change_y(NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_LEFT:
                    second.change_movement().change_x(NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_DOWN:
                    second.change_movement().change_y(-NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_RIGHT:
                    second.change_movement().change_x(-NORMAL_MOVEMENT * second_coef)

        screen.fill((0, 0, 0))


        '''
            draw field
        '''
        pygame.draw.line(screen, WHITE, [0, 0], [width, 0], BORDERS)
        pygame.draw.line(screen, WHITE, [0, height - 1], [width , height - 1], BORDERS)
        pygame.draw.line(screen, WHITE, [0, 0], [0, height / 2 - GATES_SIZE / 2], BORDERS)
        pygame.draw.line(screen, WHITE, [0, height/ 2 + GATES_SIZE / 2], [0, height], BORDERS)
        pygame.draw.line(screen, WHITE, [width - 1, 0], [width - 1, height / 2 - GATES_SIZE / 2], BORDERS)
        pygame.draw.line(screen, WHITE, [width - 1, height/ 2 + GATES_SIZE / 2], [width - 1, height], BORDERS)
        pygame.draw.line(screen, WHITE, [width / 2, 0], [width / 2, height], BORDERS - 1)
        pygame.draw.circle(screen, WHITE, [width / 2, height / 2], 95, 1)
        '''
            render goals
        '''
        rez = puck.check_goal()
        if rez:
            if rez == 1:
                puck.coords = width / 2, height / 2
                puck.movement.set(0, 0)
                first_score += 1
                puck.coords = [width / 2 + 95, height / 2]

            if rez == 2:
                puck.coords = width / 2, height / 2
                puck.movement.set(0, 0)
                second_score += 1

                puck.coords = [width / 2 - 95, height / 2]

            is_animated = 1
            animation_color = [55, 55, 55, 255]
            animation_radius = 50
            first.coords = [width / 4, height / 2]
            second.coords = [3 * width / 4, height / 2]

        if animation_color != [255, 255, 255, 255]:
            for i in range(3):
                animation_color[i] += 5
            animation_radius += (25 - puck_radius) / (200 / 5)
            clock.tick(100)
        else:
            is_animated = 0

        '''
            rewriting objects
        '''
        if is_animated:
            pygame.draw.circle(*puck.remove_collision().change_coords().draw_info(screen, pygame.Color(*animation_color), animation_radius))
            pygame.draw.circle(*first.draw_info(screen))
            pygame.draw.circle(*second.draw_info(screen))
        else:
            pygame.draw.circle(*puck.remove_collision().change_coords().draw_info(screen))
            pygame.draw.circle(*first.change_coords().draw_info(screen))
            pygame.draw.circle(*second.change_coords().draw_info(screen))

        first_score_object = main_font.render(str(first_score), True, BLUE)
        second_score_object = main_font.render(str(second_score), True, RED)
        screen.blit(first_score_object, (width / 2 - 40, 10))
        screen.blit(second_score_object, (width / 2 + 30, 10))
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
