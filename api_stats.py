from collections import Counter
import re


stats_minute = {}
stats_company = {}

with open('C:\\Users\\i325639\\Desktop\\DC4\\DC4_0520_0531.txt','rt') as file:
    for line in file:
        str_minute = line[:5]
        company = re.search(',USER:\w+@(\w+),', line)
        if company:
            company = company.group(1)
        else:
            pass
#             print(line)
         
        if(str_minute in stats_minute):
            stats_minute[str_minute] += 1
        else:
            stats_minute[str_minute] = 1
 
        if(company in stats_company):
            stats_company[company] += 1
        else:
            stats_company[company] = 1
 
# stats_minute = sorted(stats_minute.items(), key=itemgetter(1), reverse=1)
# stats_company = sorted(stats_company.items(), key=itemgetter(1), reverse=1)
stats_minute = Counter(stats_minute)
stats_company = Counter(stats_company)

print(stats_minute.most_common())
for a in stats_minute.most_common():
    print('%s\t%s'%a)
print(stats_company.most_common(50))
for a in stats_company.most_common(50):
    print('%s\t%s'%a)
