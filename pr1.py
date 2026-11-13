location = "A"
A = "Dirty"
B = "Dirty"

while True:
    print("\nLocation:", location)

    if location == "A":
        if A == "Dirty":
            print("Action: Suck")
            A = "Clean"
        else:
            print("Action: Move Right")
            location = "B"

    else:
        if B == "Dirty":
            print("Action: Suck")
            B = "Clean"
        else:
            print("Action: Move Left")
            location = "A"

    print("A:", A, "| B:", B)

    if A == "Clean" and B == "Clean":
        print("Both rooms are clean!")
        break