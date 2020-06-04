from pybricks.parameters import Direction, Port


class GyroSensor:
    """
    LEGO® MINDSTORMS® EV3 Gyro Sensor.
    """

    def __init__(self, port: Port, direction: Direction = Direction.CLOCKWISE):
        """
        LEGO® MINDSTORMS® EV3 Gyro Sensor.

        Args:
            port (Port): Port to which the sensor is connected.
            direction (Direction): Positive rotation direction when looking at the red dot on top of the sensor.
        """
        ...

    def speed(self) -> float:
        """
        Gets the speed (angular velocity) of the sensor.

        Returns:
            Sensor angular velocity in degrees/second.
        """
        return 0

    def angle(self) -> float:
        """
        Gets the accumulated angle of the sensor.

        Returns:
            Rotation angle in degrees.
        """
        return 0

    def reset_angle(self, angle: float):
        """
        Sets the rotation angle of the sensor to a desired value.

        Args:
            angle (float): Value to which the angle should be reset in degrees.
        """
        ...
