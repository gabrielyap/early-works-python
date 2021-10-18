def count_absences(chart, actual): #2
    absCount = 0
    for row in range(len(chart)):
        for name in range(len(chart[row])):
            if (chart[row][name] != actual[row][name]):
                absCount += 1
    return(absCount)

positive_words = ["amazing", "appreciate",
    "awesome", "beautiful", "best", "brilliant",
    "celebrate", "cheer", "cool", "delicious", "eager",
    "enjoy", "fortunate", "fun",
    "glad", "good", "happy", "kind", "merry",
    "nice", "pleasant", "polite", "praise", "relax",
    "sweet", "top-notch", "win", "yay"]
negative_words = ["aggressive", "anger", "annoy",
    "bloody", "bored", "careless", "cocky",
    "death", "defy", "denial", "detest", "dirty", "error",
    "fail", "guilt", "haunt", "idiot", "implode", "inhumane",
    "insult", "irritate", "lousy", "mad", "outrage", "poor",
    "refute", "sick", "strict", "stuck", "unequal",
    "waste", "wrong"]

def count_words_by_sentiment(body): #3.1
    posCount = 0
    negCount = 0
    storage = []
    s = ""
    for word in body:
        if (word.isalpha() == False):
            storage.append(s)
            s = ""            
        else:
            s += word
    #done storing into storage, now counting how many pos and neg
    for index in range(len(storage)): #posCounter
        for words in positive_words:
            if (words == storage[index]):
                    posCount += 1                    
    for index in range(len(storage)): #negCounter
        for words in negative_words:
            if (words == storage[index]):
                    negCount += 1 
    tup = (posCount, negCount)
    return tup

def classify_sentiment(counts, cutoff): #3.2
    if ((abs(counts[0] - counts[1])) > cutoff):
        if (counts[0] > counts[1]):
            return "positive"
        else:
            return "negative"
    else:
        return "neutral"

def count_words_by_sentiment2(body): #3.3 
    posCount = 0
    negCount = 0
    storage = []
    s = ""
    for word in body:
        if (word.isalpha() == False):
            storage.append(s)
            s = ""            
        else:
            s += word
    storage.append(s)
    #done storing into storage, now counting how many pos and neg
    for index in range(len(storage)): #posCounter
        for words in positive_words:
            if (words == storage[index]):
                if (index > 0):
                    if (storage[index - 1] == "not"):
                        negCount += 1
                    else:
                        posCount += 1
                else:
                    posCount += 1                    
    for index in range(len(storage)): #negCounter
        for words in negative_words:
            if (words == storage[index]):
                if (index > 0):
                    if (storage[index - 1] == "not"):
                        posCount += 1
                    else:
                        negCount += 1
                else:
                    negCount += 1                   
    tup = (posCount, negCount)
    return tup

def classify_samples(samples): #3.4
    things = []
    for i in samples:
        things.append(classify_sentiment(count_words_by_sentiment2(i), 1))
    return things

def print_accuracy(texts, label): #3.5
    count = 0
    newLst = classify_samples(texts)
    for i in range(len(newLst)):
        if (newLst[i] == label[i]):
            count += 1
    print("{} out of {} correct!" .format(count, len(newLst)))
