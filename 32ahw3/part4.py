userInput = input("> ")
qCount = 0
while userInput != "Done":
    if (userInput == "q"):
        qCount += 1
        #print(qCount) (in case if need to see how many quarters are in
        #continue
    if (userInput == "s" and qCount >= 4):
        print("Enjoy your soda!")
        qCount = 0
        break
    if (userInput == "s" and qCount < 4):
        print("You must enter", 4 - qCount, "more quarters.")
    userInput = input("> ")

