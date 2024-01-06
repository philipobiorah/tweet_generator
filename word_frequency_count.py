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
    word_frequency_count("sample_file.txt")