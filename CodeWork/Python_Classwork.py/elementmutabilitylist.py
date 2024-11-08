score1 = 45
score2 = 50

# declare a list
score = [45, 50, 35, 60, 94, 100]

print(id(score))

print(score)

# assign a value to the list index
score [1] = 35

print(score[5])

print(len(score))

print("score address after modification", id(score))

name = "balablu"
print("name address after declaration", id(name))

name += "tinubu"
print("name address after modification", id(name))

additional_score = [45, 56, 76]

score += additional_score

print(score)

for index in range(len(score)):
	score[index] += 10

print(score)

# print(score * 3)

print(score[-5])

reverse_list = []

'''
for index in range(len(score)-1, -1, -1):
	reverse_list += [score[index]]
'''

reverse_list = score[::-1]

print(reverse_list)
