#!usr/bin/env python3



i = range(1,101)

for x in i:
    if x % 3 ==0 and x% 5 ==0:
        print("fizz buzz")
    elif x % 3 == 0:
            print("fizz")
    elif x % 5 == 0:
                print("buzz")
    else:
        print(x)
