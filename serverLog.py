from collections import Counter
import re


stats_company = {}

with open('C:\\Users\\i325639\\Desktop\\DC4\\DC8.txt','rt') as file:
    for line in file:
        company = re.search('\\[\\d+\\]\\s\\[(.+)\\]', line)
        if company:
            company = company.group(1).split(',')[1]
        else:
            pass
        
        if(company in stats_company):
            stats_company[company] += 1
        else:
            stats_company[company] = 1


stats_company = Counter(stats_company)
print(len(stats_company))
print(stats_company.most_common(50))
for a in stats_company.most_common(50):
    print('%s\t%s'%a)


