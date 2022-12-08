import time, AoC2022_01, AoC2022_02, AoC2022_03, AoC2022_04
import AoC2022_05, AoC2022_06, AoC2022_07, AoC2022_08
'''
, AoC2022_09
import AoC2022_10, AoC2022_11, AoC2022_12, AoC2022_13, AoC2022_14
import AoC2022_15, AoC2022_16, AoC2022_17, AoC2022_18, AoC2022_19
import AoC2022_20, AoC2022_21, AoC2022_22, AoC2022_23
import AoC2022_24, AoC2022_25'''

days = [AoC2022_01.day01, AoC2022_02.day02, AoC2022_03.day03,
AoC2022_04.day04, AoC2022_05.day05, AoC2022_06.day06,
AoC2022_07.day07, AoC2022_08.day08]
''', AoC2022_09.day09,
AoC2022_10.day10, AoC2022_11.day11, AoC2022_12.day12,
AoC2022_13.day13, AoC2022_14.day14, AoC2022_15.day15,
AoC2022_16.day16, AoC2022_17.day17, AoC2022_18.day18,
AoC2022_19.day19, AoC2022_20.day20, AoC2022_21.day21,
AoC2022_22.day22, AoC2022_23.day23,
AoC2022_24.day24, AoC2022_25.day25'''


def infile(i, input_add=None):
    return "inputs/input" + f"{i:02d}" +\
           ("" if input_add is None else "_" + input_add) +\
           ".txt"


def exec_day(i, input_add=None):
    start_time = time.time()
    print("Day" + f"{i:02d}")
    days[i - 1](infile(i, input_add))
    end_time = time.time()
    time_diff = (end_time - start_time)
    print(f"{time_diff:.6f}", "s")


def exec_all():
    for i in range(len(days)):
        exec_day(i + 1)
        print()


def exec_days(day=None, input_add=None):
    print(time.ctime())
    if day is None:
        exec_all()
    else:
        exec_day(day, input_add)
