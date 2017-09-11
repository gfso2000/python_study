withoutSet = set();
b = 1;
index = 1;
with open('C:\\Users\\i325639\\Desktop\\coapi\\04_RSC_all_user_orderby_startdate_and_externalcode_170830114741+0200.csv','rt') as file:
    for line in file:
        if(line in withoutSet):
            print(b, index, line,end="");
            b+=1;
        index+=1;
        withoutSet.add(line);
    print(len(withoutSet));

# withSet = set();
# a = 1;        
# with open('C:\\Users\\i325639\\Desktop\\coapi\\RSC_all_user_without_orderby.csv','rt') as file:
#     for line in file:
#         withSet.add(line);
#         if(not (line in withoutSet)):
#             print(a,line,end="");
#             a+=1;
#     print(len(withSet));