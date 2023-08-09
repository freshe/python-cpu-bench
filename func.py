# MIT License
#
# Copyright (c) Fredrik B
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

import math
import multiprocessing

class Range:
    f: int = 0
    t: int = 0

    def __init__(self, f: int, t: int) -> None:
        self.f = f
        self.t = t

def get_cpu_count() -> int:
    return multiprocessing.cpu_count()

def crunch_range(value, f: int, t: int):
    prime_count = 0

    for n in range(f, t + 1):
        if is_prime(n):
            prime_count += 1

    value.value = prime_count

def get_ranges(number: int, count: int) -> [] :
    range_size = number // count
    ranges = []
    start = 1
    end = start + range_size - 1

    for _ in range(count - 1):
        ranges.append(Range(start, end))
        start = end + 1
        end = start + range_size - 1

    ranges.append(Range(start, number))

    return ranges

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    
    if number == 2 or number == 3:
        return True
    
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    end = math.ceil(math.sqrt(number))

    for x in range(5, end + 1):
        if number % x == 0:
            return False
        
    return True
