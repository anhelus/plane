import sys
import subprocess

import pytest


def test():
    subprocess.run(['pytest', '-v' '-s'], shell=True, check=True)


if __name__ == '__main__':
    globals()[sys.argv[1]]()