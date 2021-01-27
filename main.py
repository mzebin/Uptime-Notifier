# Imports
import os
import time

OSASCRIPT = """
osascript -e 'display notification "{} hours since boot up." with title "Uptime-Notifier" subtitle "Warning" sound name "pop"'
"""

# Functions

def push_notification(hours):
    os.system(OSASCRIPT.format(hours))
    time.sleep(70)


def get_uptime():
    stream = os.popen("uptime")
    output = stream.read().split()[2][:-1]

    uptime = output.split(":")
    return uptime

# Loop

