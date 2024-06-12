import random

Die1=random.randint(1,6)
Die2=random.randint(1,6)

if Die1==Die2:
    score=0
    print("Unlucky")

else:
    score=Die1+Die2

    print(score)


