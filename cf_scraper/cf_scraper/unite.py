f = open('cf_spider.csv','w')
# f.write('user,rank_sum,contests,grade\n')
lines = open("scores.txt").readlines()
lines = [x.split(',') for x in lines]
lines = sorted(lines, cmp=lambda x, y: cmp(int(x[1]),int(y[1])))
# print lines
prev_score = 0
grades = [1000,2000,3070,4424,6448]
cur_grade = 11
idx = 0
for u, score, nr in lines:
	if(idx<len(grades) and int(score) >= grades[idx] and prev_score < grades[idx]):
		cur_grade -= 1
		idx += 1
	prev_score = int(score)
	f.write(u + ',' + score + ',' + nr[:-1] + ',' + str(cur_grade) + '\n')