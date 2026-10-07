 import random

wordList = [ "panda", "lion", "tiger", "giraffe", "elephant", "hippopotamus", "wolf", "cow", "penguin", "eel",
            "crocodile", "parrot", "clownfish", "rabbit", "monkey", "frog", "owl", "fox", "umbrella", 
            "bicycle", "guitar", "piano", "violin", "drum", "flute", "trumpet", "saxophone", "harp",
            "camera", "laptop", "smartphone", "television", "headphones", "printer", "microwave",
            "refrigerator", "toaster", "blender", "vacuum", "airplane", "helicopter", "submarine", "rocket", 
            " Pizza", "Burger", "Pasta", "Sushi", "Salad", "Ice Cream", "Chocolate", "Cake", "Donut", "Fries",
            "Football", "Basketball", "Tennis", "Baseball", "Golf", "Swimming", "Running", "Cycling",
            "Hiking", "Yoga", "Dancing", "Singing", "Painting", "Drawing", "Writing", "Cooking", "Gardening",]

hints = {
    "panda": "Animal",
    "lion": "Animal",
    "tiger": "Animal",
    "giraffe": "Animal",
    "elephant": "Animal",
    "hippopotamus": "Animal",
    "wolf": "Animal",
    "cow": "Animal",
    "penguin": "Animal",
    "eel": "Animal",
    "crocodile": "Animal",
    "parrot": "Animal",
    "clownfish": "Animal",
    "rabbit": "Animal",
    "monkey": "Animal",
    "frog": "Animal",
    "owl": "Animal",
    "fox": "Animal",
    "umbrella": "Item",
    "bicycle": "Vehicle",
    "guitar": "Instrument",
    "piano": "Instrument",
    "violin": "Instrument",
    "drum": "Instrument",
    "flute": "Instrument",
    "trumpet": "Instrument",
    "saxophone": "Instrument",
    "harp": "Instrument",
    "camera": "Electronic",
    "laptop": "Electronic",
    "smartphone": "Electronic",
    "television": "Electronic",
    "headphones": "Electronic",
    "printer": "Electronic",
    "microwave": "Electronic",
    "refrigerator": "Electronic",
    "toaster": "Electronic",
    "blender": "Electronic",
    "vacuum": "Electronic",
    "airplane": "Vehicle",
    "helicopter": "Vehicle",
    "submarine": "Vehicle",
    "rocket": "Vehicle",
    "pizza": "Food",
    "burger": "Food",
    "pasta": "Food",
    "sushi": "Food",
    "salad": "Food",
    "icecream": "Food",
    "chocolate": "Food",
    "cake": "Food",
    "donut": "Food",
    "fries": "Food",
    "football": "Sport",
    "basketball": "Sport",
    "tennis": "Sport",
    "baseball": "Sport",
    "golf": "Sport",
    "swimming": "Sport",
    "running": "Sport",
    "cycling": "Sport",
    "hiking": "Sport",
    "yoga": "Sport",
    "dancing": "Activity",
    "singing": "Activity",
    "painting": "Activity",
    "drawing": "Activity",
    "writing": "Activity",
    "cooking": "Activity",
    "gardening": "Activity"
}

word = random.choice([w.lower().replace(" ", "") for w in wordList])

guessedWord = ['_'] * len(word)

attempts = 10

while attempts > 0:
   
    print("\nCurrent word: " + ' '.join(guessedWord))
    print("Hint: " + hints.get(word, "No hint available"))

    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Great guess!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left: " + str(attempts))
    if '_' not in guessedWord:
        print("\nCongratulations!! You guessed the word: " + word)
        break
else:
    print("\nYou've run out of attempts! The word was: " + word)