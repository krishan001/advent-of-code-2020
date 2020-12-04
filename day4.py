import re
from collections import Counter

def read_data():
    buffer = ""
    output_lines = []
    with open("inputs/day4_input.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            if line != "":
                buffer += line + " "
            else:
                output_lines.append(buffer)
                buffer = ""
    output_lines.append(buffer)
    buffer = ""
    return output_lines


def fields_present(passports):
    valid_pass_list = []
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in passports:
        dct = get_dict(passport)
        keys = list(dct.keys())
        if Counter(keys) == Counter(required_fields): 
            valid_pass_list.append(dct) 
    return (valid_pass_list)


def valid_fields(dcts):
    valid_pass = []
    for dct in dcts:
        if (valid_range(dct["byr"], 1920, 2002) and valid_range(dct["iyr"], 2010, 2020) and valid_range(dct["eyr"], 2020, 2030)) and valid_height(dct["hgt"]) and valid_eye_colour(dct["ecl"]) and valid_pid(dct["pid"]) != [] and valid_hcl(dct["hcl"]) != []:
            valid_pass.append(dct)
    return valid_pass


def valid_eye_colour(colour):
    eye_colour = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return colour in eye_colour


def valid_range(number, minNum, maxNum):
    return True if minNum <= int(number) <= maxNum else False


def valid_pid(pid):
    return re.findall(r"\d{9}", pid)


def valid_hcl(hcl):
    return re.findall(r"#[a-zA-Z0-9]{6}", hcl)


def valid_height(height):
    unit = height[-2:]
    if unit == "in":
        return valid_range(int(height[:-2]), 56, 76)
    elif unit == "cm":
        return valid_range(int(height[:-2]), 150, 193)
    else:
        return False


def get_dict(passport):
    total_dict = {}
    for field in passport.split(" "):
        lst = field.split(":")
        if lst[0] != '' and lst[0] != 'cid' :
            total_dict[lst[0]] = lst[1]
    return total_dict


def main():
    passports = read_data()
    pass_with_present_fields = fields_present(passports)
    print(len(pass_with_present_fields))
    print(len(valid_fields(pass_with_present_fields)))


if __name__ == "__main__":
    main()