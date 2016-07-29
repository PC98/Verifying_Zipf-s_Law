import math

file = open("C:\\Users\\Admin\\Desktop\\qq.txt", "r")
output = open("C:\\Users\\Admin\\Desktop\\OUT.doc", "w")
text = file.read()
words = {}
tmp = ''
for i in range(0, len(text)):
    if text[i].isalpha() or text[i] == '\'':
        tmp += text[i]
    else:
        if tmp != '':
            if tmp.lower() not in words:
                words[tmp.lower()] = 1
            else:
                words[tmp.lower()] += 1
        tmp = ''
r1 = list(words.keys())
r2 = [words[i] for i in r1]
for i in range(0, len(r1) - 1):
    tmp1 = i
    tmp2 = r2[i]
    for j in range(i + 1, len(r1)):
        if r2[j] < tmp2:
            tmp1 = j
            tmp2 = r2[j]
    tmp3 = r2[i]
    r2[i] = r2[tmp1]
    r2[tmp1] = tmp3
    tmp3 = r1[i]
    r1[i] = r1[tmp1]
    r1[tmp1] = tmp3
output.write(
    "Verification of Zipf's Law in a text file of 'A Prisoner of Birth'"
    "\n\nTotal number of words are %d\n\n" % sum(r2))
output.write('{:11s}{:15s}{:15s}{:14s}{:14s}\n\n'.format('WORD', 'FREQUENCY', 'RANK', 'log(RANK)', 'log(FREQUENCY)'))
for i in range(len(r1) - 1, -1, -1):
    output.write('{:13s}{:d}{:12d}{:20.4f}{:16.4f}\n'
                 .format(r1[i], r2[i], len(r1) - i, math.log(len(r1) - i), math.log(r2[i])))
file.close()
output.close()
