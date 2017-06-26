#Imports

from drawable import *
from brixconf import *

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