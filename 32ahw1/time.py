seconds = int(input("Enter a number of seconds: "))
minutes = seconds // 60
newSeconds = seconds - minutes * 60
print("That is", minutes, "minutes and", newSeconds, "seconds.")
