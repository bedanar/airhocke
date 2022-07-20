"""Declare all classes related to additional views for game."""
import pygame


class PlayingFieldColoring:
    """Declare all stuff related to game field coloring."""
    
    FIELD_COLORING = pygame.color.Color(255, 255, 255)
    LINE_WIDTH = 2
    GATES_SIZE = 200
    CENTER_CIRCLE_RADIUS = 150

    @classmethod
    def draw(
            cls,
            surface: pygame.Surface,            
            field_borders: tuple[int | float, int | float, int | float, int | float],
    ):
        """Draw all stuff related to playing field."""
        
        # Declare all angles
        left_up = pygame.math.Vector2(field_borders[0], field_borders[1])
        left_down = pygame.math.Vector2(field_borders[0], field_borders[3] - cls.LINE_WIDTH)
        right_up = pygame.math.Vector2(field_borders[2] - cls.LINE_WIDTH, field_borders[1])
        right_down = pygame.math.Vector2(field_borders[2] - cls.LINE_WIDTH, field_borders[3] - cls.LINE_WIDTH)
        
        # Draw left gates
        pygame.draw.line(surface, cls.FIELD_COLORING, left_up,
                (left_down.x, (left_down.y - cls.GATES_SIZE) // 2), width=cls.LINE_WIDTH)
        pygame.draw.line(surface, cls.FIELD_COLORING, left_down,
                (left_down.x, (left_down.y + cls.GATES_SIZE) // 2), width=cls.LINE_WIDTH)
    
        # Draw common borders
        pygame.draw.line(surface, cls.FIELD_COLORING, left_up,
                right_up, width=cls.LINE_WIDTH)
        pygame.draw.line(surface, cls.FIELD_COLORING, left_down,
                right_down, width=cls.LINE_WIDTH)

        # Draw right gates
        pygame.draw.line(surface, cls.FIELD_COLORING, right_up,
                (right_down.x, (right_down.y - cls.GATES_SIZE) // 2), width=cls.LINE_WIDTH)
        pygame.draw.line(surface, cls.FIELD_COLORING, right_down,
                (right_down.x, (right_down.y + cls.GATES_SIZE) // 2), width=cls.LINE_WIDTH)
        
        # Draw center circle
        pygame.draw.line(surface, cls.FIELD_COLORING, (right_up.x / 2, right_up.y),
                (right_down.x / 2, right_down.y), width=cls.LINE_WIDTH)

        pygame.draw.circle(surface, cls.FIELD_COLORING, ((field_borders[0] + field_borders[2]) / 2,
            (field_borders[1] + field_borders[3]) / 2), cls.CENTER_CIRCLE_RADIUS, width=cls.LINE_WIDTH)
        
