def remove(word, index): #2
    if type(word) == str:
        newAry = list(word)
        del newAry[index]
        newStr = ""
        for i in newAry:
            newStr += i
        return(newStr)
    else:
        del word[index]
        return(word)
        
def echo(ary): #3
    newList = []
    for i in ary:
        newList.append(i)
        newList.append(i)
    return(newList)
        
def move_left(state): #4
    if state[0] == "A":
        # can't move any further left
        return
    for i in range(1,len(state)):
        if state[i] == "A":
            state[i-1] = "A"
            state[i] = "_"
            # Optional, but saves time, since
            # we know there is only one "A".
            break

def move_right(state):
    if state[-1] == "A":
        # can't move any further right
        return
    for i in range(len(state)-1):
        if state[i] == "A":
            state[i+1] = "A"
            state[i] = "_"
            # Optional, but saves time, since
            # we know there is only one "A".
            break

def game(initial_state):
    for i in initial_state:
        if (i != "x" and i != "A"):
            return False
    state = initial_state
    cmd = ""
    while cmd != "end":
        print("Current:", state)
        cmd = input("Enter command: ")
        if cmd == "left" or cmd == "l":
            move_left(state)
        elif cmd == "right" or cmd == "r":
            move_right(state)
        for i in range(len(state)):
            if (state[i] == "_" or state[i] == "A"):
                if (i == (len(state) - 1)):
                    print("Victory state:" , state)
                    return True
                else:
                    continue
            else:
                 break

def get_key_to_min(collection): #5
    lowestVal = 1000
    for value in collection: #tracks index
        if (collection[value] < lowestVal and collection[value] >= 10):
            lowestVal = collection[value]
    for c in collection:
        if (collection[c] == lowestVal):
            return(c)
