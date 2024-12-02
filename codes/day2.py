def check_safe(example):
    is_list_increasing = all(example[i]<example[i+1] for i in range(len(example)-1))
    is_list_decreasing = all(example[i]>example[i+1] for i in range(len(example)-1))

    check = all(1<=abs(example[i]-example[i+1])<=3 for i in range(len(example)-1))

    return (is_list_increasing or is_list_decreasing) and check
    
def check_with_damper(example):
	if check_safe(example):
		return True
	
	for i in range(len(example)):
		modified_after_removal = example[:i]+example[i+1:]
		if check_safe(modified_after_removal):
			return True
	return False

LIST_NUMS = []
FILE_PATH = "../inputs/day2.txt"

with open(FILE_PATH,'r') as file:
    for line in file:
        lines = line.strip()
        numbers = list(map(int,lines.split()))
        LIST_NUMS.append(numbers)


count = sum(1 for example in LIST_NUMS if check_safe(example))
print(count)

count_with_modification = sum(1 for example in LIST_NUMS if check_with_damper(example))
print(count_with_modification)

