from pybricks.__stub.__control import Control
from pybricks.ev3devices import Motor
from typing import Tuple


class DriveBase:
    """
    Class representing a robotic vehicle with two powered wheels and optional wheel caster(s).

    Attributes:
        distance_control (Control): The traveled distance and drive speed are controlled by a PID controller. You can use this attribute to change its settings.
        heading_control (Control): The robot turn angle and turn rate are controlled by a PID controller. You can use this attribute to change its settings.
    """

    def __init__(self, left_motor: Motor, right_motor: Motor, wheel_diameter: float, axle_track: float):
        """
        A robotic vehicle with two powered wheels and an optional support wheel or caster.

        By specifying the dimensions of your robot, this class makes it easy to drive a given distance in millimeters or turn by a given number of degrees.

        Positive distances and drive speeds mean driving forward. Negative means backward.

        Positive angles and turn rates mean turning right. Negative means left. So when viewed from the top, positive means clockwise and negative means counterclockwise.

        Args:
            left_motor (Motor): The motor that drives the left wheel.
            right_motor (Motor): The motor that drives the right wheel.
            wheel_diameter (float): Diameter of the wheels in millimeters.
            axle_track (float): Distance between the points where both wheels touch the ground in millimeters.
        """
        self.distance_control = Control()
        self.heading_control = Control()

    def straight(self, distance: float):
        """
        Drives straight for a given distance then stops.

        Args:
            distance (float): Distance to travel in millimeters.
        """
        ...

    def turn(self, angle: float):
        """
        Turns in place by a given angle then stops.

        Args:
            angle (float): Angle of the turn in degrees.
        """
        ...

    def settings(self, straight_speed: float, straight_acceleration: float, turn_rate: float, turn_acceleration: float):
        """
        Configures the speed and acceleration used by straight() and turn().

        If you give no arguments, this returns the current values as a tuple.

        You can only change the settings while the robot is stopped. This is either before you begin driving or after you call stop().

        Args:
            straight_speed (float):  Speed of the robot during straight() in millimeters/second.
            straight_acceleration (float): Acceleration and deceleration of the robot at the start and end of straight() in millimeters/second^2.
            turn_rate (float): Turn rate of the robot during turn() in degrees/second.
            turn_acceleration (float): Angular acceleration and deceleration of the robot at the start and end of turn() in degrees/second^2.
        """
        ...

    def drive(self, drive_speed: float, turn_rate: float):
        """
        Start driving at the specified speed and turnrate. Both values are measured at the center point between the wheels of the robot.

        Args:
            drive_speed (float): Speed of the robot in millimeters/second.
            turn_rate (float): Turn rate of the robot in degrees/second.
        """
        ...

    def stop(self):
        """
        Stops the robot by letting the motors spin freely.
        """
        ...

    def distance(self) -> float:
        """
        Get the estimated driven distance.

        Returns:
            Driven distance since last reset in millimeters.
        """
        return 0

    def angle(self) -> float:
        """
        Get the estimated rotation angle of the drive base.

        Returns:
            Accumulated angle since last reset in degrees.
        """
        return 0

    def state(self) -> Tuple(float, float, float, float):
        """
        Gets the state of the robot.

        This returns the current distance(), the drive speed, the angle(), and the turn rate.

        Returns:
            Distance (float) in millimeters, Drive Speed (float) in millimeters/second, Angle (float) in degrees, Rotational Speed (float) in degrees/second
        """
        return (0, 0, 0, 0)

    def reset(self):
        """
        Resets the estimated driven distance and angle to 0.
        """
        ...
