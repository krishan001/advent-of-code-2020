from common import get_input


def get_contents(contents):
    bag_dct = {}
    each_bag = contents.split(", ")
    if each_bag[0] == "no other":
        return None
    else:
        for bag in each_bag:
            bag_dct[bag[2:]] = int(bag[:1])  # colour of bag is the key, quantity is the value
    return bag_dct


def get_bag_dict(rules):
    bag_contents = {}
    for rule in rules:
        bag_list = (rule.split(" contain "))
        bag_contents[bag_list[0]] = get_contents(bag_list[1])
    return bag_contents


def get_possible_bags(target_bag, dct):
    possible_bags = []
    for k in dct.keys():
        if dct[k] is not None and target_bag in dct[k].keys():
            possible_bags.append(k)
    return possible_bags


def part_1(bag_dict, target_bag):
    possible_bags = []
    if possible_bags == []:
        b = get_possible_bags(target_bag, bag_dict)
        possible_bags += b
    for bag in possible_bags:
        b = get_possible_bags(bag, bag_dict)
        possible_bags += b

    return len(set(possible_bags))


def format_data(data):
    new_data = []
    for line in data:
        new_data.append(line.replace(" bags", "").replace(" bag", "").replace(".", ""))
    return new_data


def part_2(bag_name, all_bags):
    """ Recursively count the containers """
    if all_bags[bag_name] == None:
        return 1
    count = 1
    for name, items in all_bags.items():
        if bag_name in name:
            for bag, bag_count in items.items():
                count += int(bag_count) * part_2(bag, all_bags)
    return count


def main():
    data = get_input("inputs/day7_input.txt")
    data = format_data(data)
    bag_dict = get_bag_dict(data)
    print(part_1(bag_dict, "shiny gold"))
    print(part_2("shiny gold", bag_dict) - 1)


if __name__ == "__main__":
    main()
