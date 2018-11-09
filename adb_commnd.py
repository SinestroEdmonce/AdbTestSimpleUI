
import subprocess
import time

# Commands
ADB_COMMANDS = {
    0: ['adb start-server'],
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
    45: ['adb bugreport'],
    46: ['adb shell cat /system/build.prop'],
}

# Max time to wait
TIME_OUT = 60

# Commands execution
def execute_command(cmd):
    # Execute commands in a subprocess
    sp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # Set time out
    if cmd in ['adb shell top', 'adb shell top -m 6']:
        time_begin = time.time()
        stdoutinfo = str('')

        while sp.poll() is None:
            line = sp.stdout.readline()
            stdoutinfo = stdoutinfo + line

            # Calculate time
            interval = time.time() - time_begin
            if interval > TIME_OUT:
                sp.terminate()
                break
            time.sleep(0.1)
        return 0, stdoutinfo
    else:
        stdoutinfo, stderrinfo = sp.communicate()
        res = str(stdoutinfo) + str(stderrinfo) + '\n'
        return sp.returncode, res