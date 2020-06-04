from pybricks.__stub.__control import Control
from pybricks.parameters import Direction, Port, Stop
from typing import List, Union


class Motor:
    """
    Generic class to control motors with built-in rotation sensors.

    Attributes:
        control (Control): The motor's PID control. 
    """

    def __init__(self, port: Port, positive_direction: Direction = Direction.CLOCKWISE, gears: Union[List[int], List[List[int]]] = None):
        """
        Generic class to control motors with built-in rotation sensors.

        Args:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should turn when you give a positive speed or angle.
            gears (Union[List[int], List[List[int]]]): List of gears linked to the motor. For example, [12, 36] represents a gear train with a 12-tooth and a 36-tooth gear. Use a list of lists for multiple gear trains, such as [[12, 36], [20, 16, 40]].

        Note:
            When you specify a gear train, all motor commands and settings are automatically adjusted to account for the resulting gear ratio. The motor direction remains unchanged by this.
        """
        self.control = Control()

    def speed(self) -> float:
        """
        Gets the speed of the motor.

        Returns:
            Motor speed in degrees/second.
        """
        return 0

    def angle(self) -> float:
        """
        Get the rotation angle of the motor.

        Returns:
            Motor angle in degrees.
        """
        return 0

    def reset_angle(self, angle: float):
        """
        Sets the accumulated rotation angle of the motor to a desired value.

        Args:
            angle (float): Value to which the angle should be reset in degrees.
        """
        ...

    def stop(self):
        """
        Stops the motor and lets it spin freely.

        The motor gradually stops due to friction.
        """
        ...

    def brake(self):
        """
        Passively brakes the motor.

        The motor stops due to friction, plus the voltage that is generated while the motor is still moving.
        """
        ...

    def hold(self):
        """
        Stops the motor and actively holds it at its current angle.
        """
        ...

    def run(self, speed: float):
        """
        Runs the motor at a constant speed.

        The motor accelerates to the given speed and keeps running at this speed until you give a new command.

        Args:
            speed (float): Speed of the motor in degrees/second.
        """
        ...

    def run_time(self, speed: float, time: float, then: Stop = Stop.HOLD, wait: bool = True):
        """
        Runs the motor at a constant speed for a given amount of time.

        The motor accelerates to the given speed, keeps running at this speed, and then decelerates. The total maneuver lasts for exactly the given amount of time.

        Args:
            speed (float): Speed of the motor in degrees/second.
            time (float): Duration of the maneuver in milliseconds.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing with the rest of the program.
        """
        ...

    def run_angle(self, speed: float, rotation_angle: float, then: Stop = Stop.HOLD, wait: bool = True):
        """
        Run the motor at a constant speed by a given angle. 

        Args:
            speed (float): Speed of the motor in degrees/second.
            rotation_angle (float): Angle by which the motor should rotate in degrees.
            then (Stop): WWhat to do after coming to a standstill.
            wait (bool): Wait for the motor to reach the target before continuing with the rest of the program.
        """
        ...

    def run_target(self, speed: float, target_angle: float, then: Stop = Stop.COAST, wait: bool = True):
        """
        Runs the motor at a constant speed towards a given target angle.

        The direction of rotation is automatically selected based on the target angle. It does matter if speed is positive or negative.

        Args:
            speed (float): Speed of the motor in degrees/second.
            target_angle (float): Angle that the motor should rotate to in degrees.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the motor to reach the target before continuing with the rest of the program.
        """
        ...

    def run_until_stalled(self, speed: float, then: Stop = Stop.COAST, duty_limit: float = None) -> float:
        """
        Runs the motor at a constant speed until it stalls.

        Args:
            speed (float): Speed of the motor in degrees/second.
            then (Stop): What to do after coming to a standstill.
            duty_limit (float) – Torque limit during this command as a percentage (0 - 100). This is useful to avoid applying the full motor torque to a geared or lever mechanism.

        Returns:	
            Angle at which the motor becomes stalled in degrees.
        """
        ...

    def dc(self, duty: float):
        """
        Rotates the motor at a given duty cycle (also known as “power”).

        This method lets you use a motor just like a simple DC motor.

        Args:
            duty (float): The duty cycle as a percentage (-100.0 to 100).
        """
        ...

    def track_target(self, target_angle: float):
        """
        Tracks a target angle. This is similar to run_target(), but the usual smooth acceleration is skipped: it will move to the target angle as fast as possible. This method is useful if you want to continuously change the target angle.

        Args:
            target_angle (float): Target angle that the motor should rotate to in degrees.
        """
        ...