import re
number_cases = int(input())
for i in range(number_cases):
    try:
        rege = input()
        re.compile(rege)
    except:
        print(False)
        continue
    print(True)   
