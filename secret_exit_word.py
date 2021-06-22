secret_exit = "dog"

word = input("Enter a word of to exit the dungeon...")

while word != secret_exit:
    
    word = input("Enter the secret word to exit this loop  ")
    if word == secret_exit:
        break
print("You've successfully left the loop.")