import random
ls = ["Snake", "Water", "Gun"]

while 1:
    p1 = random.choice(ls)
    p2 = random.choice(ls)
    if p1 == 'Snake':
        if p2 == 'Gun':
            print('p2 Won')
            break
        elif p2 == 'Water':
            print(f"p1 Won")
            break
    if p1 == 'Water':
        if p2 == 'Gun':
            print(f"p1 Won")
            break
        elif p2 == 'Snake':
            print(f"p2 Won")
            break
    if p1 == 'Gun':
        if p2 == 'Water':
            print(f"p2 Won")
            break
        elif p2 == 'Snake':
            print(f"p1 Won")
            break





