from .__battery import Battery
from .__buttons import Buttons
from .__light import Light
from .__screen import Screen
from .__speaker import Speaker


class EV3Brick:
    """
    A class to represent a LEGO® MINDSTORMS® EV3 Brick.

    Attributes:
        battery: Represents the battery on the EV3 Brick.
        buttons: Represents the buttons on the EV3 Brick.
        light: Represents the light on the EV3 Brick.
        screen: Represents the screen on the EV3 Brick.
        speaker: Represents the speaker on the EV3 Brick.
    """

    def __init__(self):
        self.battery = None  # type: Battery
        self.buttons = None  # type: Buttons
        self.light = None  # type: Light
        self.screen = None  # type: Screen
        self.speaker = None  # type: Speaker
