#!/bin/python3

import sys
import re

time = input().strip()

match = re.search("(\d{2})(\:\d{2}\:\d{2})(\w{2})",time)
hr = int(match.group(1))
half = match.group(3)
hr = 0 if hr == 12 else hr
hr = hr + 12 if half == 'PM' else hr
hr = "0" + str(hr) if hr < 10 else str(hr)
print(hr + match.group(2))