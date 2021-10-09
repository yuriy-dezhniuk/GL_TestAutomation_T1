import re
fhand = open('number.txt', 'r', encoding = 'utf8')
number_template = r'^[-+]?[0-9]*\.?[0-9]+$'
sum = 0
for line in fhand:
    if line[0] != '#' and line != '\n':
        res = re.findall(number_template, line)
        if len(res) > 0:
            for i in res:
                sum += float(i)
print(sum)
fhand.close()

