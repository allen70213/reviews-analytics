data = []
count = 0
sum_len = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())           
        #length = data[count].strip()  
        #sum_len += int(len(length))
        count += 1
        if count % 100000 == 0:
            print(len(data))
print('檔案讀取完成, 總共', len(data), '筆資料')
for d in data:
    sum_len += len(d)

print('平均留言長度', sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')