"""
Array Pair Sum
Problem
Given an integer array, output all the unique pairs that sum up to a specific value k.
So the input:
pair_sum([1,3,2,2],4)
would return 2 pairs:
 (1,3)
 (2,2)
NOTE: FOR TESTING PURPOSES< CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS



Solution
"""


def pair_sum(arra, k):
	if (len(arra)<2):
		return
	seen= set()
	output = set()
	for num in arra:
		target = k-num
		if target not in seen:
			seen.add(num)
		else:
			output.add((min(target, num), max(target, num)))
	#print("\n".join(map(str, list(output))))
	return len(output)
print("Give comma separated array")
arra = list(map(int, input().split(",")))
print("Give sum")
k = int(input())


print(arra)
print(k)

print(pair_sum(arra,k))
