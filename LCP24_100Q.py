# -*- coding:utf-8 -*-
import enum
try:
    import serial
except ImportError:
    raise ImportError("""[ Import Error ]
            - There is no serial module.
            - Install it with the following command.
            - pip install pyserial""")


class Protocol(enum.IntEnum):
    STX = 2
    ETX = 3
    PWM = ord('w')
    ON = ord('o')
    OFF = ord('f')


class LCP24_100Q:
    CHANNEL_LIST = ('0', '1', '2', '3')
    MIN_BRIGHTNESS = 0
    MAX_BRIGHTNESS = 1023

    def __init__(self, port: str, baudrate=9600):
        self.__serial = serial.Serial(
            port=port,
            baudrate=baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS)

        if self.__serial.isOpen():
            for channel in self.CHANNEL_LIST:
                self.__connect(channel)

    def __del__(self):
        self.close()

    def is_open(self) -> bool:
        """
        Description:
            Check if the device is connected normally.
        """
        return self.__serial.isOpen()

    def close(self):
        """
        Description:
            Disconnect all channels and change the brightness to 0.
        """
        for channel in self.CHANNEL_LIST:
            self.set_brightness(channel=channel, brightness=0)
            self.__disconnect(channel)

    def is_right_channel(self, channel: str) -> bool:
        """
        Description:
            Check that it is the correct channel.
        Args:
            channel: str
        Returns:
            bool
        """
        return channel in self.CHANNEL_LIST

    def is_right_brightness(self, brightness: int) -> bool:
        """
        Description:
            Check that it is the correct brightness.
        Args:
            brightness: int
        Returns:
            bool
        """
        return self.MIN_BRIGHTNESS <= brightness <= self.MAX_BRIGHTNESS

    def __connect(self, channel: str):
        """
        Description:
            Connect the selected channel.
        Args:
            channel: str: One of '0', '1', '2', '3'
        """
        if self.is_right_channel(channel):
            command = bytes([Protocol.STX,
                             ord(channel),
                             Protocol.ON,
                             Protocol.ETX])
            self.__serial.write(command)

    def __disconnect(self, channel: str):
        """
        Description:
            Disconnect the selected channel.
        Args:
            channel: str: One of '0', '1', '2', '3'
        """
        if self.is_right_channel(channel):
            command = bytes([Protocol.STX,
                             ord(channel),
                             Protocol.OFF,
                             Protocol.ETX])
            self.__serial.write(command)

    def set_brightness(self, channel: str, brightness: int):
        """
        Description:
            Set the brightness of the selected channel.
        Args:
            channel: str: One of '0', '1', '2', '3'
            brightness: int: [0, 1024]
        """
        if self.is_right_channel(channel) and self.is_right_brightness(brightness):
            command =  \
                bytes([Protocol.STX, ord(channel), Protocol.PWM]) +  \
                str(brightness).zfill(4).encode() +  \
                bytes([Protocol.ETX])
            self.__serial.write(command)
