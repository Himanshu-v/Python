secretNumber = 12
retake = 0
while retake < 10:
    print("Guess the number")
    num = int(input())
    if num > secretNumber:
        retake = retake + 1
        print("The number is greater than the secret number\n")
        continue
    elif num<secretNumber:
        retake = retake + 1
        print("The number is less than the secret number\n")
        continue
    else:
        print("The number is the secret number\n")
        break

if retake == 10:
    print("Exceeded the number of re-takes, try again later")
