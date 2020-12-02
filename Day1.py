from inputs import Day1_Input


def find_pair(target, numbers):
    for i in range(0,len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers [j] == target and i != j:
                return numbers[i], numbers[j]
    print("no pair was found")

def find_triple(target, numbers):
    for i in range(0,len(numbers)):
        for j in range(i, len(numbers)):
            for k in range(j, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == target and i != j and j != k:
                    return numbers[i], numbers[j], numbers[k]

def fix_expense_report(target, numbers):
    num1,  num2 = find_pair(target, numbers) 
    print(num1 * num2)
    num1,  num2, num3 = find_triple(target, numbers) 
    print(num1 * num2 * num3)

if __name__ == "__main__":
    numbers = Day1_Input.expense_report
    target = 2020
    fix_expense_report(target, numbers)