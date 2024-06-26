import os
import subprocess
import sys
import time

MAIN_PROGRAM = 'sample_tqdm.py'

args = [
    sys.executable, MAIN_PROGRAM,
]


def process():
    # https://koldfront.dk/making_subprocesspopen_in_python_3_play_nice_with_elaborate_output_1594

    with subprocess.Popen(args,
                          env=os.environ,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT,
                          bufsize=1,
                          universal_newlines=True,
                          text=True
                          ) as proc:
        #stdout = open(os.dup(proc.stdout.fileno()), newline='')

        while True:
            result = proc.poll()
            if result == 0:
                return True
            elif result is not None:
                return False


            #proc.stdout.S
            # doesnt read when tqdm changes buffer
            #proc.stdout.write(b'\r')
            #proc.stdout.flush()
            #line = proc.stdout.readline()



            #proc.stdout.

            #print(proc.stdout.readline())
            c = proc.stdout.read(1)
            if c != '':
                print(c)


            #print(line)

            # yield to other threads
            time.sleep(0)


if __name__ == '__main__':
    print(process())
