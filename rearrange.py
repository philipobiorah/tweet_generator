import random
import sys

def custom_suffle(words):
    # Iterate over the list of words in revers order (excluding the first element)
    for i in range(len(words) - 1, 0, -1):
        # Generate a random index j such that 0 <= j <= i
        j = random.randint(0, i)
        #Swap the element s at indicice i and j.
        words[i], words[j] = words[j], words[i]
    #retrun words
    return words  