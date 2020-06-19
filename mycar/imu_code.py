#!/usr/bin/env python
"""
copyright dhq 2018, GPLV3
"""

from mpu6050 import mpu6050
from time import sleep

sensor = mpu6050(0x68)


class MPU6050():

    def run(self,):
        accel_data = sensor.get_accel_data()
        gyro_data = sensor.get_gyro_data()
        temp = sensor.get_temp()
        mpu6050pack =    ("x: " + str(accel_data['x'])) + ("y: " + str(accel_data['y'])) + ("z: " + str(accel_data['z'])) + ("gx: " + str(gyro_data['x'])) + ("gy: " + str(gyro_data['y'])) + ("gz: " + str(gyro_data['z'])) + ("Temp: " + str(temp) + " C")
        return mpu6050pack
