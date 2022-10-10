# Game of throne

# size of display
width,height = map(int,input().split())

# movement of the crane
shift = 0 # callibriting position of crane is 0
storage = 0

# infinite loop to run all the condition of the game
while True:
    container = list(map(int,input().split()))
    commands = list(map(int,input().split()))

    for run in commands:
        if run == 1:
            # move left command.
            if shift > 0:
                shift -= 1

        elif run == 2:
            # move right command.
            if shift < width-1:
                shift += 1

        elif run == 3:
            # picking up the box
            if container[shift] != 0 and storage == 0:
                container[shift] -= 1
                storage = 1

        elif run == 4:
            # droping the box in the stack
            if container[shift] < height and storage == 1:
                container[shift] += 1
                storage = 0
            pass

        else:
            break
    print(*container)
    break
