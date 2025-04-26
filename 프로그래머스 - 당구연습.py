m = 10 
n = 10
startX = 3
startY = 7
balls = [[7, 7], [2, 7], [7, 3]]

start = [startX, startY]
minLength = []

for ball in balls:
    if(start[1] == ball[1] and start[0] != ball[0]):
        foldBallOne = [ball[0],  n + (n-ball[1])]
        foldBallTwo = [ball[0], -1 * ball[1]]

        if(start[0] > ball[0]):
            foldBallThree = [m+(m-ball[0]), ball[1]]
        elif(start[0] < ball[0]):
            foldBallThree = [-1 * ball[0], ball[1]]

        foldBallOneLength = ((start[0]-foldBallOne[0]) ** 2 + (start[1] - foldBallOne[1]) ** 2)
        foldBallTwoLength = ((start[0]-foldBallTwo[0]) ** 2 + (start[1] - foldBallTwo[1]) ** 2)
        foldBallThreeLength = ((start[0]-foldBallThree[0]) ** 2 + (start[1] - foldBallThree[1]) ** 2)

        length = [foldBallOneLength, foldBallTwoLength, foldBallThreeLength]
        minLength.append(min(length))
    
    elif(start[0] == ball[0] and start[1] != ball[1]):
        foldBallOne = [-1 * ball[0], ball[1]]
        foldBallTwo = [m+(m-ball[0]), ball[1]]

        if(start[1] > ball[1]):
            foldBallThree = [ball[0],  n + (n-ball[1])]
        elif(start[1] < ball[1]):
            foldBallThree = [ball[0], -1 * ball[1]]

        foldBallOneLength = ((start[0]-foldBallOne[0]) ** 2 + (start[1] - foldBallOne[1]) ** 2)
        foldBallTwoLength = ((start[0]-foldBallTwo[0]) ** 2 + (start[1] - foldBallTwo[1]) ** 2)
        foldBallThreeLength = ((start[0]-foldBallThree[0]) ** 2 + (start[1] - foldBallThree[1]) ** 2)

        length = [foldBallOneLength, foldBallTwoLength, foldBallThreeLength]
        minLength.append(min(length))
    
    else:
        foldBallOne = [ball[0],  n + (n-ball[1])]
        foldBallTwo = [ball[0], -1 * ball[1]]
        foldBallThree = [-1 * ball[0], ball[1]]
        foldBallFour = [m+(m-ball[0]), ball[1]]

        foldBallOneLength = ((start[0]-foldBallOne[0]) ** 2 + (start[1] - foldBallOne[1]) ** 2)
        foldBallTwoLength = ((start[0]-foldBallTwo[0]) ** 2 + (start[1] - foldBallTwo[1]) ** 2)
        foldBallThreeLength = ((start[0]-foldBallThree[0]) ** 2 + (start[1] - foldBallThree[1]) ** 2)
        foldBallFourLength = ((start[0]-foldBallFour[0]) ** 2 + (start[1] - foldBallFour[1]) ** 2)

        length = [foldBallOneLength, foldBallTwoLength, foldBallThreeLength, foldBallFourLength]
        minLength.append(min(length))


print(minLength)