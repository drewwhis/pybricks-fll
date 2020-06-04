from pybricks.parameters import Port


class TouchSensor:
    """
    LEGO® MINDSTORMS® EV3 Touch Sensor.
    """

    def __init__(self, port: Port):
        """
        LEGO® MINDSTORMS® EV3 Touch Sensor.

        Args:
            port (Port): Port to which the sensor is connected.
        """
        ...

    def pressed(self) -> bool:
        """
        Checks if the sensor is pressed.

        Return:
            True if the sensor is pressed, False if it is not pressed.
        """
        return False
