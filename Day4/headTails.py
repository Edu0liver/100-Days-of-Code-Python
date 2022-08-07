import random

aposta = int(input("Head(1) or tails(0) ? "))

result = random.randint(0,1)

if result == 0 and aposta == 0:
    print(f"Tails {result}, you won!")

elif result == 0 and aposta == 1:
    print(f"Tails {result}, you lose!")

elif result == 1 and aposta == 1:
    print(f"Head {result}, you won!")

elif result == 1 and aposta == 0:
    print(f"Head {result}, you lose!")