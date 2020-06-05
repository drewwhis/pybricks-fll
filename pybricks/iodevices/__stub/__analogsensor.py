from pybricks.parameters import Port


class AnalogSensor:
    """
    Generic or custom analog sensor.

    Args:
        port (Port): Port to which the sensor is connected.
    """

    def __init__(self, port: Port):
        ...

    def voltage(self) -> float:
        """
        Measures analog voltage.

        Returns:
            Analog voltage in millivolts.
        """
        return None

    def resistance(self) -> float:
        """
        Measures resistance.

        This value is only meaningful if the analog device is a passive load such as a resistor or thermistor.

        Returns:
            Resistance of the analog device in ohms.
        """

    def active(self):
        """
        Sets sensor to active mode. This sets pin 5 of the sensor port to high.

        This is used in some analog sensors to control a switch. For example, if you use the NXT Light Sensor as a custom analog sensor, this method will turn the light on. From then on, voltage() returns the raw reflected light value.
        """
        ...

    def passive(self):
        """
        Sets sensor to passive mode. This sets pin 5 of the sensor port to low.

        This is used in some analog sensors to control a switch. For example, if you use the NXT Light Sensor as a custom analog sensor, this method will turn the light off. From then on, voltage() returns the raw ambient light value.

        """
        ...
