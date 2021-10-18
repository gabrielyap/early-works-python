seconds = int(input("Enter a number of seconds: "))
minutes = seconds // 60
newSeconds = seconds - minutes * 60
if (minutes == 1):
    if(newSeconds == 1):
      print("That is", minutes, "minute and", newSeconds, "second.")
    else:
      print("That is", minutes, "minute and", newSeconds, "seconds.")
else:
    if(newSeconds == 1):
        print("That is", minutes, "minutes and", newSeconds, "second.")
    else:
        print("That is", minutes, "minutes and", newSeconds, "seconds.")
