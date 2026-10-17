import statistics
print(statistics.mean([100, 90]))  # 计算平均值

import sys

if len(sys.argv) < 2:
    sys.exit('Too few arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many arguments')
print('hello, my name is', sys.argv[1])