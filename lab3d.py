#!/usr/bin/env python3

# Author ID: ssachdeva25

import subprocess

def free_space():
    # Launch the Linux command and capture the output
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, capture_output=True, text=True)
    # Return the output as a UTF-8 string with newline characters stripped
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())
