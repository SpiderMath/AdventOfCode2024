# Assumes that input.txt exists and has the input

# Solution: (Part One)
## So firstly, we have to load the data by reading input.txt file, split it into reports (per line)
## Then continue by splitting each report into levels (by space)
## After that, we can iterate over the list of reports, and for each, check if the magnitude of increase lies between 1 and 3, and if the direction is constant [ can verify by checking sign of diff of the first and second levels ]

import re
from typing import List

def sign(num: int):
    if num > 0: return 1
    elif num < 0: return -1
    else: return 0


with open("./input.txt", "r") as input_file:
    # Taking in the input and splitting into reports
    input_txt: str = input_file.read()
    reports: List[str] = input_txt.split("\n")
    safe_report_count: int = 0

    for k in range(0, len(reports)):
        # Splitting each report into levels
        report: str = reports[k]
        levels: List[int] = [ int(lvl_str) for lvl_str in re.split("\s+", report) ]

        # Checking the "safe"ness of the report
        report_sign: int = sign(levels[1] - levels[0])
        safe_report: bool = True
        for i in range(1, len(levels)):
            diff: int = levels[i] - levels[i - 1]
            change: int = abs(diff)
            diff_sign: int = sign(diff)

            if not 1 <= change <= 3 or not (diff_sign == report_sign):
                safe_report = False
                break

        if safe_report:
            safe_report_count += 1

        print(f"Worked on report number {k}, the result was \033[{'92m' if safe_report else '91m'}{safe_report}\033[0m")

    print(f"The number of safe reports is: \033[93m{safe_report_count}\033[0m")

# Solution: (Part Two)



