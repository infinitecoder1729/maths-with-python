def randomize():
    min= int(input("What is the Lower Range of Your Values ? "))
    max= int(input("What is the Upper Range of Your Values ? "))
    import random
    d=int(input("How many Values do you want to generate ? "))
    print ("Rotating the Board...")
    print ("The values are....")
    if max-min<d:
        print("ERROR, Can't generate Values more than the Specified range")
    else :
        for i in range(1,d+1,+1):
            a=(random.randrange(min,max))
            print(a)    
    
randomize()
roll_again =input("Generate again? (Y/N) :")
if roll_again=="Y" :
    randomize()
else :
    quit
