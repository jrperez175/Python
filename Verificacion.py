nums = (3, 35, 30, 37, 27, 31, 41, 20, 16, 26, 45, 37, 9, 41, 28, 21, 31, 35,
        10, 26, 11, 34, 36, 12, 22, 17, 33, 43, 19, 48, 38, 25, 36, 32, 38, 28,
        30, 36, 39, 40)

new_nums = sorted(nums)
i = 0

for e in new_nums:
    if new_nums.index(e) == i:
        print('numero {} se repite {}'.format(e, new_nums.count(e)))
    i += 1