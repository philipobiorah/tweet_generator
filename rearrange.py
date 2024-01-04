import random
import sys

def custom_suffle(words):
    # Iterate over the list of words in revers order (excluding the first element)
    for i in range(len(words) - 1, 0, -1):
        # Generate a random index j such that 0 <= j <= i
        j = random.randint(0, i)
        #Swap the element s at indicice i and j.
        words[i], words[j] = words[j], words[i]
    #return shuffled list
    return words  

#Define a fuction to rearrange the workds
#simple example (not used)
# def rearrange(words):
#     random.shuffle(words)
#     return ' '.join(words)

def rearrange(words):
    # Shuffle the words and join them into a string.
    return ' '.join(custom_suffle(words))


# Check if the script is being run directly (as opposed to being imported).
if __name__ == "__main__":
    # Check if any command-line arguments were provided.
    if len(sys.argv) > 1:
        # Store all command-line arguments (excluding the script name) in a list.
        words = sys.argv[1:]
        print(rearrange(words))
    else:
        print("No words provided, Please provide words as command -line arguments. ")