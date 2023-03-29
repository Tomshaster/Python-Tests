# print(input('type here: '))
name = input('file name: ')
handle = open(name)

counts = {}
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = []
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword.clear()
        bigword.append(word)
        bigcount = count
for word,count in counts.items():
    if count == bigcount and word != bigword[0]:
        bigword.append(word)


if len(bigword) > 1:
    print('The most common words are: ',bigword, ' which appeared: ',bigcount,' times')
else:
    print('The most common word is: ',bigword, ' which appeared: ',bigcount,' times')
print(sorted([(v,k) for k,v in counts.items()], reverse=True))