# Author: ATN 1/10/22

def double_stuff(lst):
    for i, v in enumerate(lst):
        lst[i] = (v * 2)
    return lst

print(double_stuff([1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10])
print(double_stuff([1, 2.4]) == [2, 4.8])
print(double_stuff([3, "hi", 4.4]) == [6, "hihi", 8.8])
