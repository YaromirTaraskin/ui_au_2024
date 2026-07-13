import sys
import operator

l = len(sys.argv)
if l == 4:
    nums = list(filter(str.isnumeric, sys.argv[1:]))
    op_arg = set.pop(set(sys.argv[1:]) - set(nums))
    print(eval(f"operator.{op_arg.replace('-', '')}({', '.join(nums)})"))
elif l == 2:
    print(eval(sys.argv[1]))
else:
    print("Invalid number of arguments provided")

 
