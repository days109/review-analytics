data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))

sum_len = 0
for d in data:
	sum_len += len(d) #sum_len = sum_len + len(d)
print(sum_len / len(data))

result = []
for cast in data:
	if len(cast) > 500:
		result.append(cast)
print(len(result))

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('共有', len(good), '筆含good留言')
print(good[1])
