import sys
import time
from winpty import PtyProcess

MAIN_PROGRAM = 'sample_tqdm.py'

args = [
    sys.executable, MAIN_PROGRAM,
]


def process():
    proc = PtyProcess.spawn(' '.join(args))
    while proc.isalive():
        print(proc.read())
        time.sleep(0.25)


if __name__ == '__main__':
    print(process())