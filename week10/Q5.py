f = open('Ques5.txt', 'r+')

word_instances = {}

for line in f:
    l = line.split()
    for word in l:
        word_instances[word] = word_instances.get(word, 0) + 1

print(word_instances)

max_v = 0
max_keys = []

for k, v in word_instances.items():
    if v > max_v:
        max_v = v
        max_keys = [k]
    elif v == max_v:
        max_keys.append(k)

print(max_v)
print(max_keys)

f.seek(0)
content = f.read()

for word in max_keys:
    content = content.replace(word, 'Aligarh')

print(content)

f.seek(0)
f.write(content)
f.truncate()  # Remove any remaining old content

f.close()


