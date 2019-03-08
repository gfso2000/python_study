import json

def printLine(indent, n, t1, t2):
    print(indent*4*"*", n.replace('\n', ' ').replace('\r', '') + "\t", t1, "\t", t2)

with open('json1.txt', 'r') as myfile:
    json1_data=myfile.read().replace('\n', '')
with open('json2.txt', 'r') as myfile:
    json2_data = myfile.read().replace('\n', '')

json1_obj = json.loads(json1_data)
json2_obj = json.loads(json2_data)

def compareObject(level, json1_obj, json2_obj):
    # handle currentStep
    printLine(level, json1_obj["n"], json1_obj["t"], json2_obj["t"])

    #no sub, done
    if "sub" not in json1_obj or "sub" not in json2_obj:
        return
    if len(json1_obj["sub"]) == 0 or len(json2_obj["sub"]) == 0:
        return

    # handle sub
    if len(json1_obj["sub"]) > 0 and len(json2_obj["sub"]) > 0:
        handledSub1 = set();
        handledSub2 = set();
        for sub1 in json1_obj["sub"]:
            for sub2 in json2_obj["sub"]:
                if sub1["n"] == sub2["n"]:
                    compareObject(level+1, sub1, sub2);
                    handledSub1.add(sub1["n"]);
                    handledSub2.add(sub2["n"]);
        # handle the not handled subs in json1_obj
        for sub1 in json1_obj["sub"]:
            if sub1["n"] not in handledSub1:
                printLine(level + 1, sub1["n"], sub1["t"], "0")
        # handle the not handled subs in json2_obj
        for sub2 in json2_obj["sub"]:
            if sub2["n"] not in handledSub2:
                printLine(level + 1, sub2["n"], "0", sub2["t"])
    else:
        if len(json1_obj["sub"]) > 0:
            printLine(level+1, json1_obj["sub"]["n"], json1_obj["sub"]["t"], "0")
        else:
            printLine(level+1, json2_obj["sub"]["n"], "0", json2_obj["sub"]["t"])

compareObject(0, json1_obj, json2_obj)
