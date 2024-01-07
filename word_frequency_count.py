"""
We shall Analyze the frequency of words in a body of text.

For example,
 if the source text were the sentence 
 "one fish two fish red fish blue fish", 
 then the word frequency would be 
 "one" -> 1, "fish" -> 4, "two" -> 1, "red" -> 1, "blue" -> 1.
"""
import re

def histogram(source_text):
    d = dict()
    with open(source_text, "r") as file:
        
        file_content = file.read()

    # Remove punctuation and special characters, keeping only words.
    cleaned_text = re.sub(r'[^\w\s]', '', file_content)

    # Split the cleaned text into words
    words = cleaned_text.split()

    #iterate over every word in words
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1


    #print the contents of dictionary
    for key in list(d.keys()):
        print(key,":", d[key])


if __name__ == '__main__':
    histogram("gutenberg.txt")