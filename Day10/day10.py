
def get_sorted_list(adapters):
    adapters.append(0)
    adapters.append(max(adapters)+3)
    adapters = sorted(adapters)
    return adapters


def part1(adapters):
    """ Get the combination of adapters to connect your device and the differences between them"""
    sorted_list = get_sorted_list(adapters)
    differences = [x - sorted_list[i - 1] for i, x in enumerate(sorted_list)][1:]
    return differences.count(1) * differences.count(3)



    