i = int(input())
s = str(i)
ls = list(map(int, s))

max_num=max(ls)

sum_num=sum(ls)

arifmetic_num=sum_num/len(ls)

min_num=min(ls)

print('Max number',max_num)
print('Sum',sum_num)
print('Arifmetic centr',arifmetic_num)
print('Min number',min_num)

