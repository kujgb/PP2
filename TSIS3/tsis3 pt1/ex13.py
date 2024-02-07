import random
count = 0
print("Hello! What is your name?")
name = input()
print("Well, " +name+ ", I am thinking of a number between 1 and 20.")
n = random.randint(1, 20)
while True:
    print("Take a guess.")
    user_n = int(input())
    count +=1
    if user_n < n:
        print("Your guess is too low.")
    elif user_n > n:
        print("Your guess is too high.")
    else:
        print("Good job, KBTU! You guessed my number in " + str(count) + " guesses!")
        break