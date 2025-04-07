rows = 5
i = 1
while i <= rows:
    spaces = rows - i 
    j = 1
    while j <= spaces:
        print (" ", end="")
        j += 1

    stars = 2 * i - 1
    k = 1
    while k <= stars:
        print ("*", end="")
        k += 1 

    print()
    i +=  1