"""Игра «Змейка». Стрелки поворачивают змейку, Esc закрывает окно."""

from random import choice

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
CELL_SIZE = (GRID_SIZE, GRID_SIZE)
CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
ALL_CELLS = frozenset(
    (column * GRID_SIZE, row * GRID_SIZE)
    for column in range(GRID_WIDTH)
    for row in range(GRID_HEIGHT)
)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = (UP, DOWN, LEFT, RIGHT)
TURNS = {
    (pygame.K_UP, LEFT): UP,
    (pygame.K_UP, RIGHT): UP,
    (pygame.K_DOWN, LEFT): DOWN,
    (pygame.K_DOWN, RIGHT): DOWN,
    (pygame.K_LEFT, UP): LEFT,
    (pygame.K_LEFT, DOWN): LEFT,
    (pygame.K_RIGHT, UP): RIGHT,
    (pygame.K_RIGHT, DOWN): RIGHT,
}

BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
SPEED = 20
CAPTION = 'Змейка — рекорд: {}'

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class GameObject:
    """Объект игрового поля с позицией и цветом."""

    def __init__(self, body_color=None):
        """Поместить объект в центр поля."""
        self.position = CENTER
        self.body_color = body_color

    def draw(self):
        """Определить отрисовку в дочернем классе."""
        pass


class Apple(GameObject):
    """Яблоко, которое появляется в свободной ячейке."""

    def __init__(self, occupied=(CENTER,)):
        """Выбрать начальную позицию с учётом тела змейки."""
        super().__init__(APPLE_COLOR)
        self.randomize_position(occupied)

    def randomize_position(self, occupied=(CENTER,)):
        """Выбрать любую свободную клетку игрового поля."""
        free_cells = ALL_CELLS.difference(occupied)
        self.position = choice(tuple(free_cells)) if free_cells else None

    def draw(self):
        """Нарисовать яблоко с рамкой, если для него есть место."""
        if self.position is not None:
            cell = pygame.Rect(self.position, CELL_SIZE)
            screen.fill(self.body_color, cell)
            pygame.draw.rect(screen, BORDER_COLOR, cell, 1)


class Snake(GameObject):
    """Змейка, сегменты которой хранятся от головы к хвосту."""

    def __init__(self):
        """Начать движение вправо из центра поля."""
        super().__init__(SNAKE_COLOR)
        self.reset(RIGHT)

    def reset(self, direction=None):
        """Оставить одну голову в центре и выбрать направление движения."""
        self.position = CENTER
        self.positions = [self.position]
        self.length = 1
        self.direction = choice(DIRECTIONS) if direction is None else direction
        self.next_direction = None
        self.last = None

    def get_head_position(self):
        """Вернуть координаты головы змейки."""
        return self.positions[0]

    def update_direction(self):
        """Применить поворот, выбранный для этого шага."""
        if self.next_direction is not None:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self, apple_position=None):
        """Передвинуть голову на клетку и сохранить хвост при поедании."""
        x, y = self.get_head_position()
        dx, dy = self.direction
        self.position = (
            (x + dx * GRID_SIZE) % SCREEN_WIDTH,
            (y + dy * GRID_SIZE) % SCREEN_HEIGHT,
        )
        self.positions.insert(0, self.position)
        if self.position == apple_position:
            self.length += 1
        self.last = None
        if len(self.positions) > self.length:
            self.last = self.positions.pop()

    def draw(self):
        """Стереть освободившуюся клетку и нарисовать голову."""
        if self.last is not None:
            tail_cell = pygame.Rect(self.last, CELL_SIZE)
            screen.fill(BOARD_BACKGROUND_COLOR, tail_cell)
        cell = pygame.Rect(self.get_head_position(), CELL_SIZE)
        screen.fill(self.body_color, cell)
        pygame.draw.rect(screen, BORDER_COLOR, cell, 1)


def handle_keys(game_object):
    """Обработать выход и разрешённые повороты относительно текущего хода."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            turn = TURNS.get((event.key, game_object.direction))
            if turn is not None:
                game_object.next_direction = turn


def main():
    """Запустить игру и обновлять поле после каждого хода."""
    pygame.init()
    snake = Snake()
    apple = Apple(snake.positions)
    record = snake.length
    pygame.display.set_caption(CAPTION.format(record))
    screen.fill(BOARD_BACKGROUND_COLOR)
    snake.draw()
    apple.draw()
    pygame.display.update()

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()
        snake.move(apple.position)
        head = snake.get_head_position()
        ate_apple = head == apple.position

        if snake.length > record:
            record = snake.length
            pygame.display.set_caption(CAPTION.format(record))

        new_round = (
            head in snake.positions[1:] or snake.length == len(ALL_CELLS)
        )
        if new_round:
            snake.reset()
            screen.fill(BOARD_BACKGROUND_COLOR)
        if ate_apple or (new_round and apple.position == snake.position):
            apple.randomize_position(snake.positions)

        snake.draw()
        apple.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
