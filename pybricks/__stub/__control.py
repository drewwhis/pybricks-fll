class Control:
    """
    Class to interact with PID controller and settings.

    Attributes:
        scale (float): Scaling factor between the controlled integer variable and the physical output. For example, for a single motor this is the number of encoder pulses per degree of rotation.
    """

    def __init__(self):
        self.scale = 1.0  # type: float

    def done(self) -> bool:
        """
        Checks if an ongoing command or maneuver is done.

        Returns:
            True if the command is done, False if not.
        """
        return None

    def stalled(self) -> bool:
        """
        Checks if the controller is currently stalled.

        A controller is stalled when it cannot reach the target speed or position, even with the maximum actuation signal.

        Returns:
            True if the controller is stalled, False if not.
        """
        return None

    def limits(self, speed: float = None, acceleration: float = None, actuation: float = None) -> tuple:
        """
        Configures the maximum speed, acceleration, and actuation.

        If no arguments are given, this will return the current values.

        Note:
            You must provide ALL arguments or NO arguments.

        Args:
            speed (float): Maximum speed. All speed commands will be capped to this value. Rotational (degrees/second) or Linear (millimeters/second).
            acceleration (float): Maximum acceleration. Rotational (degrees/second^2) or Linear (millimeters/second^2).
            actuation (float): Maximum actuation as percentage (0 - 100) of absolute maximum.

        Returns:
            Speed, acceleration, and actuation (if no arguments are provided).
        """
        return None

    def pid(self, kp: int = None, ki: int = None, kd: int = None, integral_range: float = None, integral_rate: float = None, feed_forward: float = None) -> tuple:
        """
        Gets or sets the PID values for position and speed control.

        If no arguments are given, this will return the current values.

        Note:
            You must provide ALL arguments or NO arguments.

        Args:	
            kp (int): Proportional position (or integral speed) control constant.
            ki (int): Integral position control constant.
            kd (int): Derivative position (or proportional speed) control constant.
            integral_range (float): Region around the target angle (degrees) or distance (millimeters), in which integral control errors are accumulated.
            integral_rate (float): Maximum rate at which the error integral is allowed to grow. Rotational (degrees/second) or Linear (millimeters/second).
            feed_forward (float): This adds a feed forward signal to the PID feedback signal, in the direction of the speed reference. This value is expressed as a percentage (0 - 100) of the absolute maximum duty cycle.

        Returns:
            kp, ki, kd, integral range, integral rate, and feed forward (if no arguments are provided).
        """
        return None

    def target_tolerances(self, speed: float = None, position: float = None) -> tuple:
        """
        Gets or sets the tolerances that say when a maneuver is done.

        If no arguments are given, this will return the current values.

        Note:
            You must provide ALL arguments or NO arguments.

        Args:	
            speed (float): Allowed deviation from zero speed before motion is considered complete. Linear (millimeters/second) or Rotational (degrees/second)
            position (float): Allowed deviation from the target before motion is considered complete. Linear (millimeters) or Rotational (degrees).

        Returns:
            Allowed deviation from zero speed and allowed deviation from the target (if no arguments are provided).
        """
        return None

    def stall_tolerance(self, speed: float = None, time: float = None) -> tuple:
        """
        Gets or sets stalling tolerances.

        If no arguments are given, this will return the current values.

        Note:
            You must provide ALL arguments or NO arguments.

        Args:	
            speed (float): If the controller cannot reach this speed for some time even with maximum actuation, it is stalled. Rotational (degrees/second) or Linear (millimeters/second).
            time (float): How long the controller has to be below this minimum speed before we say it is stalled in milliseconds.

        Returns:
            Threshold speed and time limit (if no arguments are provided).
        """
        return None
