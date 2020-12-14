from itertools import chain, combinations


def get_sorted_list(adapters):
    adapters.append(0)
    adapters.append(max(adapters)+3)
    adapters = sorted(adapters)
    return adapters


def get_differences(sorted_list):
    return [x - sorted_list[i - 1] for i, x in enumerate(sorted_list)][1:]


def get_next_items(target, sorted_list):
    next_items = []
    for i in range(1,4):
        item = target + i
        if item in sorted_list:
            next_items.append(item)
    return next_items


def count_combinations(sorted_list):
    dp = [1]
    for i in range(1, len(sorted_list)):
        ans = 0
        for j in range(0, i):
            if sorted_list[j] + 3 >= sorted_list[i]:
                ans += dp[j]
        dp.append(ans)
    return dp[-1]


def part1(adapters):
    """ Get the combination of adapters to connect your device and the differences between them"""
    sorted_list = get_sorted_list(adapters)
    differences = get_differences(sorted_list)
    return differences.count(1) * differences.count(3)


def part2(adapters):
    total_combinations = 1
    sorted_list = get_sorted_list(adapters)
    return count_combinations(sorted_list)



