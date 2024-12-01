from collections import Counter
FILE_PATH = "../inputs/input1.txt"
LIST_NUMS = []
LIST_1 = []
LIST_2 = []


with open(FILE_PATH,'r') as file:
    for line in file:
        lines = line.strip()
        numbers = list(map(int,lines.split()))
        LIST_NUMS.append(numbers)

for num_array in LIST_NUMS:
    LIST_1.append(num_array[0])
    LIST_2.append(num_array[1])

LIST_1.sort()
LIST_2.sort()

DIFF = sum(abs(LIST_1[i]-LIST_2[i]) for i in range(len(LIST_1)))
print(DIFF)

SET1 = set(LIST_1)
counter = Counter(LIST_2)

MUL_RES = []

for ele in SET1:
    MUL_RES.append(ele*counter[ele])

print(sum(MUL_RES))

