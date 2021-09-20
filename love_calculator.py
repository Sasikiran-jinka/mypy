import random
print("welcome to the love calculator..💕❤")
you = input("enter your name\n")
your = input("enter the other name you need to check\n")
combined_string = you + your
l_string = combined_string.lower()
t = l_string.count("t")
r = l_string.count("r")
u = l_string.count("u")
e = l_string.count("e")
true = t + r + u + e
L = l_string.count("l")
o = l_string.count("o")
v = l_string.count("v")
e = l_string.count("e")
Love = L + o + v + e
Love_score = int(true + Love)
# Love_score = random.randint(1, 100)
if Love_score < 10 or Love_score > 90:
    print(f"your score is {Love_score},you go together like coke and mentos")
elif 40 < Love_score < 50:
    print(f"your love score is {Love_score},you are alright together")
else:
    print(f"your love score is {Love_score}")
