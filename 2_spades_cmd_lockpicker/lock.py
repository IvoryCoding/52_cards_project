# Date: 2022/10/03
# Description: A cmd lock that has a hidden flag inside

# Assumptions:
# Once picked returns flag
# Code to unlock is 4 digits from the 16 displayed
# Numbers can be between or including 1 - 99
# After 30 secs lock closes

from random import *
import time

def lock_numbers():
    chosen_nums = []

    for i in range(4):
        chosen_nums.append(randint(1,99))

    return chosen_nums

def create_combo(all_nums):
    combo = []

    for i in range(4):
        combo.append(all_nums[randint(1,len(all_nums)-1)])

    return combo

def check_combo(combo, user_input):
    flag = "flag{Y0U_D1D_1T}"
    combo_string = "{} {} {} {}".format(combo[0], combo[1], combo[2], combo[3])

    if combo_string == user_input:
        print(flag)
        return True

    return False

if __name__ == "__main__":
    all_nums = []
    unlocked = False

    for x in range(4):
        nums = lock_numbers()
        print("+----+----+----+----+")
        print("| {:02d} | {:02d} | {:02d} | {:02d} |".format(nums[0], nums[1], nums[2], nums[3]))
        print("+----+----+----+----+")

        all_nums.append(nums[0])
        all_nums.append(nums[1])
        all_nums.append(nums[2])
        all_nums.append(nums[3])

    combo = create_combo(all_nums)
    end = time.time() + 30

    # while not unlocked and time not 30 sec past
    while not unlocked and (time.time() < end):
        string = input("Enter code: ")
        unlocked = check_combo(combo, string)



