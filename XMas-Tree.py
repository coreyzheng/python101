lines = input("How big do you want your X-mas tree to be?")
length = lines * 2 -1
spaces = (length-1)/2
i = 1

while i <= lines:
    print " "*(spaces-i+1), "*"*(2*i-1)
    i = i +1
