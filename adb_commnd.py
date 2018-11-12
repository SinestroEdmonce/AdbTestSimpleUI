# coding=utf-8

import subprocess
import time
import os
import sys

import pygame
from pygame.locals import *

from adb_warnings import *
from adb_UI import *

# Commands
ADB_COMMANDS = {
    0: ['adb start-server',
        'adb devices'],
    1: ['adb kill-server'],
    2: ['adb shell screencap -p /sdcard/screen.png',
        'adb pull /sdcard/screen.png d:/',
        'adb shell rm /sdcard/screen.png'],
    3: ['adb root',
        'adb remount',
        'adb shell ls system/app',
        'adb shell rm -rf $1',
        'adb reboot'],
    4: ['adb root',
        'adb push $1 $2',
        'adb reboot'],
    5: ['adb shell input keyevent $1'],
    6: ['adb get-serialno'],
    7: ['adb devices'],
    8: ['adb reboot'],
    9: ['adb reboot bootloader'],
    10: ['adb reboot recovery'],
    11: ['adb logcat -t $1'],
    12: ['adb shell cat /sys/class/net/wlan0/address'],
    13: ['adb help'],
    14: ['adb shell cat /proc/cpuinfo'],
    15: ['adb install $1'],
    16: ['adb install -r $1'],
    17: ['adb install -s $1'],
    18: ['adb uninstall $1'],
    19: ['adb uninstall -k $1'],
    20: ['adb shell am start -n $1'],
    21: ['adb shell top'],
    22: ['adb shell top -m 6'],
    23: ['adb shell top -n 1'],
    24: ['adb shell procrank'],
    25: ['adb shell kill $1'],
    26: ['adb shell ps'],
    27: ['adb shell ps -x $1'],
    28: ['adb shell service list'],
    29: ['adb shell cat /proc/meminfo'],
    30: ['adb shell cat /proc/iomem'],
    31: ['adb remount'],
    32: ['adb pull $1 $2'],
    33: ['adb push $1 $2'],
    34: ['adb shell ls $1'],
    35: ['adb shell cd $1'],
    36: ['adb shell rename $1 $2'],
    37: ['adb shell rm /system/avi.apk'],
    38: ['adb shell rm -rf $1'],
    39: ['adb shell chmod 777 $1'],
    40: ['adb shell mv $1 $2'],
    41: ['adb shell mkdir $1'],
    42: ['adb shell cat $1'],
    43: ['adb shell cat /data/misc/wifi/*.conf'],
    44: ['adb logcat -c'],
    45: ['adb bugreport $1'],
    46: ['adb shell cat /system/build.prop'],
    47: ['adb devices',
         'adb root',
         'adb remount']
}

# Max time to wait
TIME_OUT = 16
# Min time to wait
MIN_TIME_EXC = 2

# Commands execution
def execute_command(wins, cmd):
    # If cmd = adb shell, then open the COMMAND for WINDOWS
    if cmd in ['adb shell']:
        subprocess.Popen('cmd', shell=True)
        return 0, 'Auto-open COMMAND for further adb shell testing.\n'

    # Execute commands in a subprocess
    sp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # Exceed the MIN_TIME_EXC and consider that this command requires more time for IO or it has an instant IO
    # time.sleep(MIN_TIME_EXC)
    # wins.change_text_display('正在截获命令行实时输出,请等待...\n')

    # Initialize the keyboard event listening
    pygame.init()
    pygame.display.set_mode((1, 1))
    # Relocate the standard output and error information
    while sp.poll() is None and cmd not in ['adb help']:  # None: executing. Specific process for 'adb help'
        stdout_info = str(sp.stdout.readline()).strip() + '\n'
        wins.change_text_display(stdout_info)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sp.terminate()
                    return 0, 'CTRL-C Happening...\n'
        pygame.display.update()

    # Cease listening
    pygame.quit()
    stdout_info, stderr_info = sp.communicate()
    res = str(stdout_info) + str(stderr_info) + '\n'
    return sp.returncode, res
