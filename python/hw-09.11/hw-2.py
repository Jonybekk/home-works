# Level 1

# 1
# it_companies = {'Apple', 'Google', 'Apple', 'Samsung', 'IBM', 'Amazon'}
# print(len(it_companies))

# 2
# it_companies = {'Apple', 'Google', 'Apple', 'Samsung', 'IBM', 'Amazon'}
# it_companies.add('Twitter')
# print(it_companies)

# 3
# it_companies = {'Apple', 'Google', 'Apple', 'Samsung', 'IBM', 'Amazon'}
# it_companies.update(['Telegram' , 'WhatsApp' , 'Instagram'])
# print(it_companies)

# 4
# it_companies = {'Apple', 'Google', 'Apple', 'Samsung', 'IBM', 'Amazon'}
# it_companies.remove('Google')
# print(it_companies)

# 5
# Ошибка шыгады
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# it_companies.remove('Telegram')
# print(it_companies)

# Ошибка шыкпайды
# it_companies = {'Apple', 'Google', 'Apple', 'Samsung', 'IBM', 'Amazon'}
# it_companies.discard('Telegram')
# print(it_companies)



# Level 2
# 1
# a = {15, 36, 89, 25, 41, 58}
# b = {47, 63, 20, 11, 15, 58, 36, 12}
# print(a.union(b))

# 2
# a = {15, 36, 89, 25, 41, 58}
# b = {47, 63, 20, 11, 15, 58, 36, 12}
# print(a.intersection(b))

# 3
# a = {15, 36, 89, 25, 41, 58}
# b = {47, 63, 20, 11, 15, 58, 36, 12}
# print(a.issubset(b))

# 4

# 5
# a = {15, 36, 89, 25, 41, 58}
# b = {47, 63, 20, 11, 15, 58, 36, 12}
# print(a.union(b))
# print(b.union(a))

# 6
# a = {15, 36, 89, 25, 41, 58}
# b = {47, 63, 20, 11, 15, 58, 36, 12}
# print(a.symmetric_difference(b))

# 7
# a = {15, 36, 89, 25, 41, 58}
# b = {47, 63, 20, 11, 15, 58, 36, 12}
# del a
# del b


# Level 3

# 1
age = [14, 25, 36, 20, 14, 36, 42, 25, 14]
print(len(age))
print(len(set(age)))
print(len(set(age)) < len(age))

# 3
sentence = 'I am a teacher and I love to inspire and teach people'
sentence_set = sentence.split()
sentence = set(sentence_set)
print(sentence)