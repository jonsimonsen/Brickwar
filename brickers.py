#Imports

from drawable import *
from brixconf import *
from library import makeFont

class Platform(Rectangle):
    """A class for platforms"""

    def __init__(self, x, y, width):
        """Create a platform.

        x, y: x- and y-components used for a Vector2D object pointing to the
        upper left corner of the platform.
        width: Width of the rectangle.

        Height and color is assumed to be defined as constants.
        """

        Rectangle.__init__(self, width, PLATFORM_H, PLATFORM_C, x, y)

class Brick(Rectangle):
    """A class for a user controlled brick (square)."""

    def __init__(self, x, y, dim, color):
        """Create a brick for the user to control.

        x, y: x- and y-components used for a Vector2D object pointing to the
        upper left corner of the brick.
        dim: width and height of the brick.
        color: Color of the brick.
        """

        Rectangle.__init__(self, dim, dim, color, x, y)

class Target(Rectangle):
    """A class for the exit from a level."""

    def __init__(self, x, y):
        """Create an exit on the level.

        x, y: x- and y-components used for a Vector2D object pointing to the
        upper left corner of the exit.

        Width, height, color and text are assumed to be defined as constants.
        """

        Rectangle.__init__(self, EXIT_W, EXIT_H, EXIT_C, x, y)
        self._text = EXIT_T
        self._font = makeFont(EXIT_F, EXIT_FS)

    def draw(self, layer):
        """Draw the exit on the layer."""

        Rectangle.draw(self, layer)

        textBox = self._font.render(EXIT_T, True, EXIT_TC)
        layer.blit(textBox, self._pos.x, self._pos.y)
