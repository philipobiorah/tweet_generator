"""
We shall Analyze the frequency of words in a body of text.

For example,
 if the source text were the sentence 
 "one fish two fish red fish blue fish", 
 then the word frequency would be 
 "one" -> 1, "fish" -> 4, "two" -> 1, "red" -> 1, "blue" -> 1.
"""

def word_frequency_count(file_path):
    d = dict()
    with open(file_path, "r") as file:
        words = file.read().split()

    


    