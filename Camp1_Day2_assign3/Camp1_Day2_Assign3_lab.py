import json
def getNumberfromFile(filename):
    file = open(filename, "r")
    data = json.load(file)
    StrSequence = data["sequence"]
    TempSequence = StrSequence.split(",")
    return TempSequence

if __name__ == '__main__':
    EvenNumber = []
    NumberList = getNumberfromFile("ListNumber.json")
    for i in range(len(NumberList)):
        if(int(NumberList[i]) % 2 == 0):
            EvenNumber.append(NumberList[i])
    strtmp = ','.join(EvenNumber)
    print ("The even numbers are "+strtmp)
