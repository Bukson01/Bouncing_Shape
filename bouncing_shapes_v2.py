import sys
import random
import time
try:
    import bext
except ImportError:
    print('This program requires the bext module which can be installed using the "pip install bext" command')
    sys.exit()

class Logo:
    def __init__(self, color, x, y, direction):
        """Initialize a Logo object."""
        self.color = color
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        """Move the logo based on its direction."""
        if self.direction == 'ur':
            self.x += 2
            self.y -= 1
        elif self.direction == 'ul':
            self.x -= 2
            self.y -= 1
        elif self.direction == 'dr':
            self.x += 2
            self.y += 1
        elif self.direction == 'dl':
            self.x -= 2
            self.y += 1

class BouncingShapes:
    def __init__(self):
        """Initialize a BouncingShapes object."""
        bext.clear()
        self.WIDTH, self.HEIGHT = bext.size()
        self.WIDTH -= 1
        self.logos = [Logo(random.choice(COLORS), random.randint(1, self.WIDTH-4), random.randint(1, self.HEIGHT-4), random.choice(DIRECTIONS)) for _ in range(len(NUMBER_OF_LOGOS))]
        self.corner_bounces = 0

    def check_corner_bounce(self, logo):
        """Check if the logo hits a corner and update its direction."""
        if logo.x == 0 and logo.y == 0:
            logo.direction = DOWN_RIGHT
            self.corner_bounces += 1
        elif logo.x == 0 and logo.y == self.HEIGHT - 1:
            logo.direction = UP_RIGHT
            self.corner_bounces += 1
        elif logo.x == self.WIDTH - 3 and logo.y == 0:
            logo.direction = DOWN_LEFT
            self.corner_bounces += 1
        elif logo.x == self.WIDTH - 3 and logo.y == self.HEIGHT - 1:
            logo.direction = UP_LEFT
            self.corner_bounces += 1

    def handle_edge_bounce(self, logo):
        """Check if the logo hits an edge and update its direction."""
        if logo.x == 0 and logo.direction in [UP_LEFT, DOWN_LEFT]:
            logo.direction = UP_RIGHT if logo.direction == UP_LEFT else DOWN_RIGHT
        elif logo.x == self.WIDTH - 3 and logo.direction in [UP_RIGHT, DOWN_RIGHT]:
            logo.direction = UP_LEFT if logo.direction == UP_RIGHT else DOWN_LEFT
        elif logo.y == 0 and logo.direction in [UP_LEFT, UP_RIGHT]:
            logo.direction = DOWN_LEFT if logo.direction == UP_LEFT else DOWN_RIGHT
        elif logo.y == self.HEIGHT - 1 and logo.direction in [DOWN_LEFT, DOWN_RIGHT]:
            logo.direction = UP_LEFT if logo.direction == DOWN_LEFT else UP_RIGHT

    def update_logo(self, logo):
        """Update the logo's position and direction."""
        original_direction = logo.direction
        self.check_corner_bounce(logo)
        self.handle_edge_bounce(logo)
        if logo.direction != original_direction:
            logo.color = random.choice(COLORS)
        logo.move()

    def display_logos(self):
        """Display logos on the screen."""
        bext.goto(5, 0)
        bext.fg('white')
        print(f'Corner bounces: {self.corner_bounces}', end='')
        for i, logo in enumerate(self.logos):
            bext.goto(logo.x, logo.y)
            bext.fg(logo.color)
            print(NUMBER_OF_LOGOS[i], end='')
        bext.goto(0, 0)
        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)

    def run(self):
        """Run the bouncing shapes simulation."""
        while True:
            self.display_logos()
            for logo in self.logos:
                self.update_logo(logo)

def main():
    """Main function to initialize and run the bouncing shapes simulation."""
    try:
        bouncing_shapes = BouncingShapes()
        bouncing_shapes.run()
    except KeyboardInterrupt:
        print()
        print('Bouncing Shapes Logo')
        sys.exit()

# Set up the constants
NUMBER_OF_LOGOS = ['♥', '♦', '♠', '♣']
PAUSE_AMOUNT = 0.2
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

if __name__ == '__main__':
    main()
