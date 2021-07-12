import random

score = random.randint(0, 100)
level = str
if score >= 90 :
    level = 'A'
elif 80 <= score < 90 :
    level = 'B'
elif 70 <= score < 80 :
    level = 'C'
elif 60 <= score < 70 :
    level = 'D'
else :
    level = 'F'

print(score, "점은 ",level, "등급입니다")
