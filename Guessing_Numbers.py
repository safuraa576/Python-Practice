import random

# Generate a random number between 1 and 50
lucky_num = random.randint(1, 50)

print("🎮 Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 50.")
print("Can you guess it? 👀\n")

while True:

    user_num = int(input("🔢 Guess the number: "))

    if user_num == lucky_num:
        print("🎉 Correct Guess! YOU WON!!!")
        break

    elif user_num > lucky_num:
        print("📈 Too High! Try again.")

    else:
        print("📉 Too Low! Try again.")

print("\n🏁 Game has ended!")
print("Thanks for playing! 💙")