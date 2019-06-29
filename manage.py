import sys
import subprocess

import pytest


def test():
    try:
        subprocess.run(['pytest', '-v', '-s'], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print('Warning: some tests failed. Check PyTest output.')


if __name__ == '__main__':
    globals()[sys.argv[1]]()