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

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆資料提到good')

# list comprehension
# output =[運算 for 變數 in 清單 if 篩選條件]
good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆資料提到good')

# # 'bad' in d 判斷 True / False
# bad = ['bad' in d for d in data]
# print(bad)


# 文字計數
wc = {} # word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1  #新增新的key進字典

for word in wc:
    if wc[word] > 100:
        print(word, wc[word])

while True:
    word = input('請問你想查甚麼字:')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過', wc[word], '次')
    else:
        print('這個字沒有出現過')
print('感謝使用查詢功能')


