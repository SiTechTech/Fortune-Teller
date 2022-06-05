import random

while True:
    a = ("Ask away")
    b = ("What Do You Need To Know")
    c = ("What Do You Wish To Hear")
    d = ("I May Have An Answer")
    e = ("What Can I Do For You")

    Supply = [a, b, c, d, e]

    random_number = random.randint(0, 4)
    Supply_pick = Supply[random_number]

    Do = input(Supply_pick + ": ")

    Questions = ["Yes ~Definitely", "As i see it yes", "Sign point to yes", "it is certain", "Most likely", "Outlook is good", "Reply is hazy, try again later", "Concentrate and ask again",
                 "Better not tell you now", "Dont count on it", "My reply is no", "My sources say no", "Very doubtful", "I see great stuggle with that", "I see great fortune", "wonderful idea"]

    random_number = random.randint(0, 15)
    Questions_pick = Questions[random_number]

    print(Questions_pick)
    print(''' 
____________________________________''')
