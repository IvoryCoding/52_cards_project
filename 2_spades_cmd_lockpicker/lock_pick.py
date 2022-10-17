# Date: 2022/10/03
# Description: A cmd lock pick to pop a lock and get hidden flags

# Assumptions:
# Once lock is picked displays flag
# Code to unlock is 4 digits from the 16 displayed
# Numbers can be between or including 1 - 99
# After 30 secs lock closes
# Multiple threads for the same lock

# parse cmd run. Items: the lock file name, code length

import argparse
import re
import pexpect as px

def run_read(filename):
    # there should be a way to make this faster with subprocess just have to figure out how to send
    # data to stdin without calling the subprocess again

    # pexpect is nice but, it is not fast enough to crack the lock in 30 seconds
    # it also is not saving the data using > to lock.txt which is another problem

    cmd = 'python3 {} > lock.txt'.format(filename)

    print("[spawning child]")
    child = px.spawn(cmd)

    gen_passcodes(child, lock_nums=parse_lock())

def parse_lock():
    numbers = []

    for line in open("lock.txt", "r"):
        f = re.findall("[\d\d]+", line)

        if f: # Add each number to the numbers list
            for num in f:
                numbers.append(num)

    return numbers

def gen_passcodes(child, lock_nums):
    for n1 in lock_nums:
        for n2 in lock_nums:
            for n3 in lock_nums:
                for n4 in lock_nums:
                    combo = "{} {} {} {}".format(n1, n2, n3, n4)
                    child.expect("Enter code:")
                    child.sendline(combo)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-lock", help="The file name and extension for the lock.")
    args = parser.parse_args()

    run_read(args.lock)
