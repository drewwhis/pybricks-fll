from enum import Enum


class ImageFile(Enum):
    """
    Paths to standard EV3 images.

    Note:
        Information: ACCEPT, BACKWARD, DECLINE, FORWARD, LEFT, NO_GO, QUESTION_MARK, RIGHT, STOP_1, STOP_2, THUMBS_DOWN, THUMBS_UP, WARNING

        LEGO&reg;: EV3, EV3_ICON

        Objects: TARGET

        Eyes: ANGRY, AWAKE, BOTTOM_LEFT, BOTTOM_RIGHT, CRAZY_1, CRAZY_2, DIZZY, DOWN, EVIL, KNOCKED_OUT, MIDDLE_LEFT, MIDDLE_RIGHT, NEUTRAL, PINCHED_LEFT, PINCHED_MIDDLE, PINCHED_RIGHT, SLEEPING, TIRED_LEFT, TIRED_MIDDLE, TIRED_RIGHT, UP, WINKING
    """
    ACCEPT = "ACCEPT"
    BACKWARD = "BACKWARD"
    DECLINE = "DECLINE"
    FORWARD = "FORWARD"
    LEFT = "LEFT"
    NO_GO = "NO_GO"
    QUESTION_MARK = "QUESTION_MARK"
    RIGHT = "RIGHT"
    STOP_1 = "STOP_1"
    STOP_2 = "STOP_2"
    THUMBS_DOWN = "THUMBS_DOWN"
    THUMBS_UP = "THUMBS_UP"
    WARNING = "WARNING"

    EV3 = "EV3"
    EV3_ICON = "EV3_ICON"

    TARGET = "TARGET"

    ANGRY = "ANGRY"
    AWAKE = "AWAKE"
    BOTTOM_LEFT = "BOTTOM_LEFT"
    BOTTOM_RIGHT = "BOTTOM_RIGHT"
    CRAZY_1 = "CRAZY_1"
    CRAZY_2 = "CRAZY_2"
    DIZZY = "DIZZY"
    DOWN = "DOWN"
    EVIL = "EVIL"
    KNOCKED_OUT = "KNOCKED_OUT"
    MIDDLE_LEFT = "MIDDLE_LEFT"
    MIDDLE_RIGHT = "MIDDLE_RIGHT"
    NEUTRAL = "NEUTRAL"
    PINCHED_LEFT = "PINCHED_LEFT"
    PINCHED_MIDDLE = "PINCHED_MIDDLE"
    PINCHED_RIGHT = "PINCHED_RIGHT"
    SLEEPING = "SLEEPING"
    TIRED_LEFT = "TIRED_LEFT"
    TIRED_MIDDLE = "TIRED_MIDDLE"
    TIRED_RIGHT = "TIRED_RIGHT"
    WINKING = "WINKING"
    UP = "UP"
