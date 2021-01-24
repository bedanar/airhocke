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
    first = Player([width / 4, height / 2], 40, 1, height, width)
    second = Player([3 * width / 4, height / 2], 40, 0, height, width)
    puck = Puck([width / 2, height / 2], [first, second], 20, height, width)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_LSHIFT and first_coef == 1:
                #
                # if event.key == pygame.K_LCTRL:
                #
                if event.key == pygame.K_w:
                    first.change_movement().change_y(-NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_a:
                    first.change_movement().change_x(-NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_s:
                    first.change_movement().change_y(NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_d:
                    first.change_movement().change_x(NORMAL_MOVEMENT * first_coef)
                # if event.key == pygame.K_RSHIFT:
                #     mult_vector(1 / second_coef, second.movement)
                #     second_coef = FAST_SPEED
                #     mult_vector(FAST_SPEED, second.movement)
                # if event.key == pygame.K_RCTRL:
                #     mult_vector(1 / second_coef, second.movement)
                #     second_coef = FURIOUS_SPEED
                #     mult_vector(FURIOUS_SPEED, second.movement)
                if event.key == pygame.K_UP:
                    second.change_movement().change_y(-NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_LEFT:
                    second.change_movement().change_x(-NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_DOWN:
                    second.change_movement().change_y(NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_RIGHT:
                    second.change_movement().change_x(NORMAL_MOVEMENT * second_coef)
            if event.type == pygame.KEYUP:
                # if event.key == pygame.K_LSHIFT:
                #     mult_vector(1 / first_coef, first.movement)
                # if event.key == pygame.K_LCTRL:
                #     mult_vector(1 / first_coef, first.movement)
                if event.key == pygame.K_w:
                    first.change_movement().change_y(NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_a:
                    first.change_movement().change_x(NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_s:
                    first.change_movement().change_y(-NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_d:
                    first.change_movement().change_x(-NORMAL_MOVEMENT * first_coef)
                # if event.key == pygame.K_RSHIFT:
                #     mult_vector(1 / second_coef, second.movement)
                # if event.key == pygame.K_RCTRL:
                #     mult_vector(1 / second_coef, second.movement)
                if event.key == pygame.K_UP:
                    second.change_movement().change_y(NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_LEFT:
                    second.change_movement().change_x(NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_DOWN:
                    second.change_movement().change_y(-NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_RIGHT:
                    second.change_movement().change_x(-NORMAL_MOVEMENT * second_coef)
        # print(second.movement)
        screen.fill((0, 0, 0))
        pygame.draw.circle(*puck.remove_collision().change_coords().draw_info(screen))
        pygame.draw.circle(*first.change_coords().draw_info(screen))
        pygame.draw.circle(*second.change_coords().draw_info(screen))
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
