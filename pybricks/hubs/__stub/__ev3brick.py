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
        self.battery = Battery()
        self.buttons = Buttons()
        self.light = Light()
        self.screen = Screen()
        self.speaker = Speaker()

    
    