from constants import *
from player import *
from puck import *
from random import randint
from utils import *
from serv import network
import threading
import concurrent.futures
from multiprocessing.pool import ThreadPool
from serv.network import Networking
import json

def two_in_one(pygame):
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


    return_to_menu = Button(465, 540, 65, 50)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return 1000
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if return_to_menu.is_clicked(mouse_pos):
                    return 0

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
        if max(first_score, second_score) >= 11:
            if first_score > second_score:
                return result_screen(pygame, "Red player won")
            else:
                return result_screen(pygame, "Blue player won")

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
        return_to_menu.draw("Menu", 20, pygame=pygame, screen=screen)
        clock.tick(fps)
        pygame.display.flip()
    return 0


def game_intro(pygame):
    pygame.display.set_caption('Air hockey')
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    running = True
    v = 100
    fps = 120
    clock = pygame.time.Clock()
    w = pygame.Color("white")
    running = True
    two_players_button = Button(200, 250, 150, 50)
    online_players_button = Button(450, 250, 90, 50)
    ai_plaing = Button(650, 250, 160, 50)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return 1000

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos 

                if two_players_button.is_clicked(mouse_pos):
                    return 1

                if online_players_button.is_clicked(mouse_pos):
                    return 2

                if ai_plaing.is_clicked(mouse_pos):
                    return 3

        screen.fill((0, 0, 0))
        font = pygame.font.Font('fonts/static/RobotoMono-MediumItalic.ttf', 30)
        text = font.render("Сhoose a game", True, WHITE)
        text_rect = text.get_rect(center=(width / 2, height / 2 - 200))
        screen.blit(text, text_rect)
        two_players_button.draw("Two players", 20, pygame=pygame, screen=screen)
        online_players_button.draw('Online', 20, pygame=pygame, screen = screen)
        ai_plaing.draw("Play with ai", 20, pygame=pygame, screen=screen)

        pygame.display.update()
        clock.tick(fps)



def online(pygame):
    result = [None]
    thread = threading.Thread(target=connect, args=(result, 0))
    thread.start()
    pygame.display.set_caption('Hockey')
    text = "Looking for opponent"
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    running = True
    fps = 120
    opponent = None
    clock = pygame.time.Clock()
    return_to_menu = Button(465, 540, 65, 50)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return 1000

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos 
                if return_to_menu.is_clicked(mouse_pos):
                    return 0
        if result[0]:
            opponent = result[0]
            break
        screen.fill((0, 0, 0))
        
        write_text(text, (330, 250), 30, pygame, screen, color=WHITE)
        return_to_menu.draw("Menu", 20, pygame, screen)
        
        pygame.display.update()
        clock.tick(fps)
    
    print(opponent)
    make_rules = (opponent['my'] > opponent['enemy'][1])
    opponent_ip = opponent['enemy'][0][0]
    opponent_pid = opponent['enemy'][1]
    my_pid = opponent['my']
    print(opponent_ip, opponent_pid)
    ######################################################################################
    ######################################################################################
    ######################################################################################
    ######################################################################################
    ######################################################################################

    running = True
    fps = 120
    clock = pygame.time.Clock()
    first_coef, second_coef = 1, 1
    if make_rules:
        my_player = Player([width / 4, height / 2], 50, 1, height, width)
        opponent_player = Player([3 * width / 4, height / 2], 50, 0, height, width)
    else:
        opponent_player = Player([width / 4, height / 2], 50, 1, height, width)
        my_player = Player([3 * width / 4, height / 2], 50, 0, height, width)
    puck = Puck([width / 2 + 95, height / 2] if randint(0, 1) else [width / 2 - 95, height / 2], [my_player, opponent_player], 25, height, width)
    my_score, opponent_score = 0, 0
    main_font = pygame.font.Font(None, 36)
    is_animated = 1
    animation_color = [55, 55, 55, 255]
    puck_radius = 50
    animation_radius = 50


    return_to_menu = Button(465, 540, 65, 50)


    connected = Networking(37020)
    connected.bind()    
    def predicate(data):
        if not data:
            return False
        return data['pid'] == opponent_pid and data['to'] == my_pid
    past_score = [-1, -1]
    data = {
        'error': '',
        'your_coords': opponent_player.get_coords(),
        'my_coords': my_player.get_coords(),
        'puck_coords': puck.coords,
        "score": (my_score, opponent_score),
        'my_vector': (0, 0)
    }
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                for i in range(10000):
                        connected.send_json({
                            'pid': my_pid,
                            'to': opponent_pid,
                            'error': "Your opponent has left the game",
                        }, opponent_ip)

                return 1000
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    my_player.change_movement().change_y(-NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_a:
                    my_player.change_movement().change_x(-NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_s:
                    my_player.change_movement().change_y(NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_d:
                    my_player.change_movement().change_x(NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_UP:
                    my_player.change_movement().change_y(-NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_LEFT:
                    my_player.change_movement().change_x(-NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_DOWN:
                    my_player.change_movement().change_y(NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_RIGHT:
                    my_player.change_movement().change_x(NORMAL_MOVEMENT * second_coef)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    my_player.change_movement().change_y(NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_a:
                    my_player.change_movement().change_x(NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_s:
                    my_player.change_movement().change_y(-NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_d:
                    my_player.change_movement().change_x(-NORMAL_MOVEMENT * first_coef)
                if event.key == pygame.K_UP:
                    my_player.change_movement().change_y(NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_LEFT:
                    my_player.change_movement().change_x(NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_DOWN:
                    my_player.change_movement().change_y(-NORMAL_MOVEMENT * second_coef)
                if event.key == pygame.K_RIGHT:
                    my_player.change_movement().change_x(-NORMAL_MOVEMENT * second_coef)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if return_to_menu.is_clicked(mouse_pos):
                    for i in range(10000):
                        connected.send_json({
                            'pid': my_pid,
                            'to': opponent_pid,
                            'error': "Your opponent has left the game",
                        }, opponent_ip)

                    return 0

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
        if make_rules:
            connected.send_json({
                'pid': my_pid,
                'to': opponent_pid,
                'your_coords': opponent_player.get_coords(),
                'my_coords': my_player.get_coords(),
                'puck_coords': puck.coords,
                "score": (my_score, opponent_score),
                'error': '',
            }, opponent_ip)
        else:
            connected.send_json({
                'pid': my_pid,
                'to': opponent_pid,
                'my_vector': my_player.movement.get(),
                'error': '',
            }, opponent_ip)
        last_data = data
        data = connected.recv_json_until(predicate=predicate, timeout=0.002)[0]
        
        if not data:
            data = last_data
        if data['error'] != '':
            return result_screen(pygame, data['error'])
        # print(data)
        # data = json.loads(data)


        if animation_color != [255, 255, 255, 255]:
            for i in range(3):
                animation_color[i] += 5
            animation_radius += (25 - puck_radius) / (200 / 5)
            clock.tick(100)
        else:
            is_animated = 0


        if make_rules:
            # print('I"m a big boss')
            opponent_player.movement = Movement(*data['my_vector'])
            rezult = puck.check_goal()
            if rezult:
                if rezult == 1:
                    puck.coords = width / 2, height / 2
                    puck.movement.set(0, 0)
                    my_score += 1
                    puck.coords = [width / 2 + 95, height / 2]

                if rezult == 2:
                    puck.coords = width / 2, height / 2
                    puck.movement.set(0, 0)
                    opponent_score += 1
                    puck.coords = [width / 2 - 95, height / 2]

                is_animated = 1
                animation_color = [55, 55, 55, 255]
                animation_radius = 50
                my_player.coords = [width / 4, height / 2]
                opponent_player.coords = [3 * width / 4, height / 2]

            '''
                rewriting objects
            '''
            if is_animated:
                pygame.draw.circle(*puck.remove_collision().change_coords().draw_info(screen, pygame.Color(*animation_color), animation_radius))
                pygame.draw.circle(*my_player.draw_info(screen))
                pygame.draw.circle(*opponent_player.draw_info(screen))
            else:
                pygame.draw.circle(*puck.remove_collision().change_coords().draw_info(screen))
                pygame.draw.circle(*my_player.change_coords().draw_info(screen))
                pygame.draw.circle(*opponent_player.change_coords().draw_info(screen))
        else:

            my_player.coords = data['your_coords']
            

            opponent_player.coords = data['my_coords']
            puck.coords = data['puck_coords']
            opponent_score, my_score = data['score']
            if past_score != data['score']:
                past_score = data['score']
                is_animated = 1
                animation_color = [55, 55, 55, 255]
                animation_radius = 50
                my_player.coords = [width / 4, height / 2]
                opponent_player.coords = [3 * width / 4, height / 2]
            if is_animated:
                pygame.draw.circle(*puck.remove_collision().change_coords().draw_info(screen, pygame.Color(*animation_color), animation_radius))
                pygame.draw.circle(*my_player.draw_info(screen))
                pygame.draw.circle(*opponent_player.draw_info(screen))
            else:
                pygame.draw.circle(*puck.draw_info(screen))
                pygame.draw.circle(*my_player.draw_info(screen))
                pygame.draw.circle(*opponent_player.draw_info(screen))
            
        if max(my_score, opponent_score) >= 11:
            if make_rules:
                for i in range(1000):
                    
                    connected.send_json({
                        'pid': my_pid,
                        'to': opponent_pid,
                        'your_coords': opponent_player.get_coords(),
                        'my_coords': my_player.get_coords(),
                        'puck_coords': puck.coords,
                        'error': '',
                        "score": (my_score, opponent_score),
                    }, opponent_ip)
            del connected
            if my_score > opponent_score:
                return result_screen(pygame, "You're won")
            else:
                return result_screen(pygame, "You're lose")
        if make_rules:

            first_score_object = main_font.render(str(my_score), True, WHITE)
            second_score_object = main_font.render(str(opponent_score), True, WHITE)
        else:
            first_score_object = main_font.render(str(opponent_score), True, WHITE)
            second_score_object = main_font.render(str(my_score), True, WHITE)

        screen.blit(first_score_object, (width / 2 - 40, 10))
        screen.blit(second_score_object, (width / 2 + 30, 10))
    

        return_to_menu.draw("Menu", 20, pygame=pygame, screen=screen)
        clock.tick(fps)
        pygame.display.flip()
    return 0
    ######################################################################################
    ######################################################################################
    ######################################################################################
    ######################################################################################


def result_screen(pygame, rez):

    pygame.display.set_caption('Hockey')
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    running = True
    fps = 120
    clock = pygame.time.Clock()
    return_to_menu = Button(465, 540, 65, 50)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return 1000

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos 
                if return_to_menu.is_clicked(mouse_pos):
                    return 0

        screen.fill((0, 0, 0))

        font = pygame.font.Font('fonts/static/RobotoMono-MediumItalic.ttf', 25)
        text = font.render(rez, True, WHITE)
        text_rect = text.get_rect(center=(width / 2, height / 2))
        screen.blit(text, text_rect)
        return_to_menu.draw('Menu', 20, pygame, screen)
        pygame.display.update()
        clock.tick(fps)




def ai(pygame):
    pass