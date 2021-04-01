import serial
import string
import time
import numpy as np

from file_handling import format_filename, export_recorded
from plot import plot_data


windows = 'COM6'
linux = '/dev/ttyACM0'
ser = serial.Serial(windows, 230400, timeout=1) 


def read() -> list:
    line = str(ser.readline()).replace(' ', '').replace('\\r\\n', '').replace('b\'', '')
    return line.split(';')


def write(command) -> None: 
    ser.write(command.encode())


def read_bytes(amount) -> bytes:
    return ser.read(amount)


def main():
    channel_names = ['24', '25', '26', '27', '28', '29']
    data_channels = list()

    input('start recording by pressing any button, stop recording by using keyboard interrupt crtl+c: ')
    try:
        while True:
            data_channels.append(read())
    except KeyboardInterrupt:
        plot_data([channel_names, np.transpose(np.array(data_channels))])


if __name__ == '__main__':
    main()
