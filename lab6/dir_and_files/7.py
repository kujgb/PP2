with open("first.txt", "r") as firsttxt, open("second.txt", "w") as secondtxt:
    for line in firsttxt:
        secondtxt.write(line)