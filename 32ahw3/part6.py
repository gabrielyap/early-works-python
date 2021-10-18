numQuizzes = 0
total = 0
lowestVal = 100
while True:
    userInput = input("Enter quiz score: ")
    if (userInput == "Done"):
        break
    score = int(userInput)
    if (score >= 0 and score <= 100):
        numQuizzes += 1
        total += score
        #print(numQuizzes)
        if (score < lowestVal):
            lowestVal = score
        continue
total -= lowestVal
avg = round((total / (numQuizzes - 1)), 0)
avg = int(avg)
print ("The average score is ", avg, ".", sep = "")
#print(lowestVal)
