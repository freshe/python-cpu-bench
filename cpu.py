"""
MIT License

Copyright (c) Fredrik B

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE
"""

import func
import sys
import getopt
import time
import math
import multiprocessing
from multiprocessing import Value

DEFAULT_NUMBER = 10000000

def main(argv):
    number = DEFAULT_NUMBER
    opts, args = getopt.getopt(argv, "n:")

    try:
        for opt, arg in opts:
            if opt in ("-n"):
                number = int(arg)
    except:
        pass

    if number < 1000:
        number = DEFAULT_NUMBER

    cpu_count = func.get_cpu_count()
    ranges = func.get_ranges(number, cpu_count)
    
    total_prime_count = 0
    procs = []
    values = []

    start_time = time.time()

    for x in ranges:
        value = Value('i', 0)
        proc = multiprocessing.Process(target=func.crunch_range, args=(value, x.f, x.t), daemon=False)

        procs.append(proc)
        values.append(value)

        proc.start()

    print("crunching primes from number " + str(number) + " using " + str(cpu_count) + " cores")

    for x in procs:
        x.join()

    for x in values:
        total_prime_count += x.value

    stop_time = time.time()
    seconds = math.floor(stop_time - start_time)

    print("Found " + str(total_prime_count) + " primes in " + str(seconds) + " seconds")

if __name__ == "__main__":
    main(sys.argv[1:])