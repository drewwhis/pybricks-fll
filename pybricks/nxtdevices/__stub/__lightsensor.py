from pybricks.parameters import Port


class LightSensor:
    """
    LEGO® MINDSTORMS® NXT Color Sensor.

    Args:
        port (Port): Port to which the sensor is connected.
    """

    def __init__(self, port: Port):
        ...

    def ambient(self) -> float:
        """
        Measures the ambient light intensity.

        Returns:
            Ambient light intensity, ranging from 0 (dark) to 100 (bright).
        """
        return None

    def reflection(self) -> float:
        """
        Measures the reflection of a surface using a red light.

        Returns:
            Reflection, ranging from 0 (no reflection) to 100 (high reflection).
        """
        return None
