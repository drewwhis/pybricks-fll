from pybricks.media import Font, Image
from pybricks.parameters import Button, Color
from typing import Iterable, List, Union


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
        self.battery = self.__Battery()
        self.buttons = self.__Buttons()
        self.light = self.__Light()
        self.screen = self.__Screen()
        self.speaker = self.__Speaker()

    class __Battery:
        """
        DO NOT INSTANTIATE OR IMPORT.

        A stub class to represent the battery member of the EV3Brick class.
        """

        def __init__(self):
            ...

        def voltage(self) -> int:
            """
            Gets the voltage of the battery.

            Returns:
            Voltage in mV, represented as an int.
            """

            return 0

        def current(self) -> int:
            """
            Gets the current supplied by the battery.

            Returns:
            Battery current in mA, represented as an int.
            """

            return 0

    class __Buttons:
        """
        DO NOT INSTANTIATE OR IMPORT.

        A stub class to represent the buttons member of the EV3Brick class.
        """

        def __init__(self):
            ...

        def pressed(self) -> List[Button]:
            """
            Checks which buttons are currently pressed.

            Returns:
            List of pressed buttons.
            """

            return []

    class __Light:
        """
        DO NOT INSTANTIATE OR IMPORT.

        A stub class to represent the light member of the EV3Brick class.
        """

        def __init__(self):
            ...

        def on(self, color: Color):
            """
            Turns on the light at the specified color.

            Args:
                color (Color): Color of the light. The light turns off if you choose None or a color that is not available.
            """
            ...

        def off(self):
            """
            Turns off the light.
            """
            ...

    class __Screen:
        """
        DO NOT INSTANTIATE OR IMPORT.
        A stub class to represent the screen member of the EV3Brick class.

        Attributes:
            height (int): The height of the screen in pixels.
            width (int): The width of the screen in pixels.
        """

        def __init__(self):
            self.width = 178
            self.height = 128

        def clear(self):
            """
            Clears the screen. All pixels on the screen will be set to Color.WHITE.
            """
            ...

        def draw_text(self, x: int, y: int, text: str, text_color: Color = Color.BLACK, background_color: Color = None,):
            """
            Draws text on the screen.

            The most recent font set using set_font() will be used or Font.DEFAULT if no font has been set yet.

            Args:
                x (int): The x-axis value where the left side of the text will start.
                y (int): The y-axis value where the top of the text will start.
                text (str): The text to draw.
                text_color (Color): The color used for drawing the text.
                background_color (Color): The color used to fill the rectangle behind the text or None for transparent background.
            """
            ...

        def print(self, *args, sep: str = "", end: str = "\n",):
            """
            Prints a line of text on the screen.

            This method works like the builtin print() function, but it writes on the screen instead.

            You can set the font using set_font(). If no font has been set, Font.DEFAULT will be used. The text is always printed used black text with a white background.

            Unlike the builtin print(), the text does not wrap if it is too wide to fit on the screen. It just gets cut off. But if the text would go off of the bottom of the screen, the entire image is scrolled up and the text is printed in the new blank area at the bottom of the screen.

            Args:
                *args (object): Zero or more objects to print.
                sep (str): Separator that will be placed between each object that is printed.
                end (str): End of line that will be printed after the last object.
            """
            ...

        def set_font(self, font: Font):
            """
            Sets the font used for writing on the screen.

            The font is used for both draw_text() and print().

            Args:
                font (Font): The font to use.
            """
            ...

        def load_image(self, source: Union[str, Image]):
            """
            Clears this image, then draws the source image centered in the screen.

            Args:
                source (Image or str): The source Image. If the argument is a string, then the source image is loaded from file.
            """
            ...

        def draw_image(self, x: int, y: int, source: Union[str, Image], transparent: Color = None):
            """
            Draws the source image on the screen.

            Args:
                x (int): The x-axis value where the left side of the image will start.
                y (int): The y-axis value where the top of the image will start.
                source (Image or str): The source Image. If the argument is a string, then the source image is loaded from file.
                transparent (Color): The color of image to treat as transparent or None for no transparency.
            """
            ...

        def draw_pixel(self, x: int, y: int, color: Color = Color.BLACK):
            """
            Draws a single pixel on the screen.

            Args:
                x (int): The x coordinate of the pixel.
                y (int): The y coordinate of the pixel.
                color (Color): The color of the pixel.
            """
            ...

        def draw_line(self, x1: int, y1: int, x2: int, y2: int, width: int = 1, color: Color = Color.BLACK):
            """
            Draws a line on the screen.

            Args:
                x1 (int): The x coordinate of the starting point of the line.
                y1 (int): The y coordinate of the starting point of the line.
                x2 (int): The x coordinate of the ending point of the line.
                y2 (int): The y coordinate of the ending point of the line.
                width (int): The width of the line in pixels.
                color (Color): The color of the line.
            """
            ...

        def draw_box(self, x1: int, y1: int, x2: int, y2: int, r: int = 0, fill: bool = False, color: Color = Color.BLACK):
            """
            Draws a box on the screen.

            Args:
                x1 (int): The x coordinate of the left side of the box.
                y1 (int): The y coordinate of the top of the box.
                x2 (int): The x coordinate of the right side of the box.
                y2 (int): The y coordinate of the bottom of the box.
                r (int): The radius of the corners of the box.
                fill (bool): If True, the box will be filled with color, otherwise only the outline of the box will be drawn.
                color (Color): The color of the box.
            """
            ...

        def draw_circle(self, x: int, y: int, r: int, fill: bool = False, color: Color = Color.BLACK):
            """
            Draws a circle on the screen.

            Args:
                x (int): The x coordinate of the center of the circle.
                y (int): The y coordinate of the center of the circle.
                r (int): The radius of the circle.
                fill (bool): If True, the circle will be filled with color, otherwise only the circumference will be drawn.
                color (Color): The color of the circle.
            """
            ...

        def save(self, filename: str):
            """
            Saves the screen as a .png file.

            Args:
                filename (str): The path to the file to be saved.

            Raises:
                TypeError: filename is not a string
                OSError: There was a problem saving the file.
            """
            ...

    class __Speaker:
        """
        DO NOT INSTANTIATE OR IMPORT.

        A stub class to represent the speaker member of the EV3Brick class.
        """

        def __init__(self):
            ...

        def beep(self, frequency: int = 500, duration: int = 100):
            """
            Play a beep/tone.

            Args:
                frequency (int): Frequency of the beep in Hertz. Frequencies below 100 are treated as 100.
                duration (int): Duration of the beep in milliseconds. If the duration is less than 0, then the method returns immediately, and the frequency play continues to play indefinitely.
            """
            ...

        def play_notes(self, notes: Iterable[str], tempo: int = 120):
            """
            Plays a sequence of musical notes.

            For example, you can play: ['C4/4', 'C4/4', 'G4/4', 'G4/4'].

            Args:
                notes (Iterable[str]): A sequence of notes to be played (see format below).
                tempo (int): Beats per minute where a quarter note is one beat.

            Note:
                Each note is a string with the following format:
                    - The first character is the name of the note, A to G or R for a rest.
                    # (sharp) or b (flat). B#/Cb and E#/Fb are not allowed.
                    - Note names can also include an accidental
                    - The note name is followed by the octave number 2 to 8. For example C4 is middle C. The octave changes to the next number at the note C, for example, B3 is the note below middle C (C4).
                    - The octave is followed by / and a number that indicates the size of the note. For example /4 is a quarter note, /8 is an eighth note and so on.
                    - This can optionally followed by a . to make a dotted note. Dotted notes are 1-1/2 times as long as notes without a dot.
                    - The note can optionally end with a _ which is a tie or a slur. This causes there to be no pause between this note and the next note.
            """
            ...

        def play_file(self, file_name: str):
            """
            Plays a sound file.

            Args:
                file_name (str): Path to the sound file, including the file extension.
            """
            ...

        def say(self, text: str):
            """
            Says a given text string.

            You can configure the language and voice of the text using set_speech_options().

            Args:
                text (str): What to say.
            """
            ...

        def set_speech_options(self, language: str = None, voice: str = None, speed: int = None, pitch: int = None):
            """
            Configures speech settings used by the say() method.

            Any options that is set to None will not be changed. If an option is set to an invalid value say() will use the default value instead.

            Args:
                language (str): Language of the text. For example, you can choose 'en' (English) or 'de' (German). A list of all available languages is given below.
                voice (str): The voice to use. For example, you can choose 'f1' (female voice variant 1) or 'm3' (male voice variant 3). A list of all available voices is given below.
                speed (int): Number of words per minute.
                pitch (int): Pitch (0 to 99). Higher numbers make the voice higher pitched and lower numbers make the voice lower pitched.

            Note:
                You can choose the following languages:
                    - 'af': Afrikaans
                    - 'an': Aragonese
                    - 'bg': Bulgarian
                    - 'bs': Bosnian
                    - 'ca': Catalan
                    - 'cs': Czech
                    - 'cy': Welsh
                    - 'da': Danish
                    - 'de': German
                    - 'el': Greek
                    - 'en': English (default)
                    - 'en-gb': English (United Kingdom)
                    - 'en-sc': English (Scotland)
                    - 'en-uk-north': English (United Kingdom, Northern)
                    - 'en-uk-rp': English (United Kingdom, Received Pronunciation)
                    - 'en-uk-wmids': English (United Kingdom, West Midlands)
                    - 'en-us': English (United States)
                    - 'en-wi': English (West Indies)
                    - 'eo': Esperanto
                    - 'es': Spanish
                    - 'es-la': Spanish (Latin America)
                    - 'et': Estonian
                    - 'fa': Persian
                    - 'fa-pin': Persian
                    - 'fi': Finnish
                    - 'fr-be': French (Belgium)
                    - 'fr-fr': French (France)
                    - 'ga': Irish
                    - 'grc': Greek
                    - 'hi': Hindi
                    - 'hr': Croatian
                    - 'hu': Hungarian
                    - 'hy': Armenian
                    - 'hy-west': Armenian (Western)
                    - 'id': Indonesian
                    - 'is': Icelandic
                    - 'it': Italian
                    - 'jbo': Lojban
                    - 'ka': Georgian
                    - 'kn': Kannada
                    - 'ku': Kurdish
                    - 'la': Latin
                    - 'lfn': Lingua Franca Nova
                    - 'lt': Lithuanian
                    - 'lv': Latvian
                    - 'mk': Macedonian
                    - 'ml': Malayalam
                    - 'ms': Malay
                    - 'ne': Nepali
                    - 'nl': Dutch
                    - 'no': Norwegian
                    - 'pa': Punjabi
                    - 'pl': Polish
                    - 'pt-br': Portuguese (Brazil)
                    - 'pt-pt': Portuguese (Portugal)
                    - 'ro': Romanian
                    - 'ru': Russian
                    - 'sk': Slovak
                    - 'sq': Albanian
                    - 'sr': Serbian
                    - 'sv': Swedish
                    - 'sw': Swahili
                    - 'ta': Tamil
                    - 'tr': Turkish
                    - 'vi': Vietnamese
                    - 'vi-hue': Vietnamese (Hue)
                    - 'vi-sgn': Vietnamese (Saigon)
                    - 'zh': Mandarin Chinese
                    - 'zh-yue': Cantonese Chinese

                You can choose the following voices:
                    - 'f1': female variant 1
                    - 'f2': female variant 2
                    - 'f3': female variant 3
                    - 'f4': female variant 4
                    - 'f5': female variant 5
                    - 'm1': male variant 1
                    - 'm2': male variant 2
                    - 'm3': male variant 3
                    - 'm4': male variant 4
                    - 'm5': male variant 5
                    - 'm6': male variant 6
                    - 'm7': male variant 7
                    - 'croak': croak
                    - 'whisper': whisper
                    - 'whisperf': female whisper
            """
            ...

        def set_volume(self, volume: int, which: str = "_all_"):
            """
            Sets the speaker volume.

            Args:
                volume (int): Volume of the speaker as a percentage (0 to 100).
                which (str): Which volume to set. 'Beep' sets the volume for beep() and play_notes(). 'PCM' sets the volume for play_file() and say(). '_all_' sets both at the same time.
            """
            ...
