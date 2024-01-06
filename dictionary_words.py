import random
import sys
"""
We will make several assumptions to reduce the complexity of this program:

The program only accepts one argument: the number of words to be selected.
All parameters except the number of words will be hard-coded.
We will use the words file which is available on all Unix systems for our list of words.
The sentences do not have to make grammatical sense.
Word selection can be completely random and the word order does not matter.
"""



# f = open("sample_file.txt", "r")
# #lets print only a specified number of words
# line_count = 0;
# for x in f:
#     print(x)
#     line_count += 1

#     if line_count == 5:
#         break

# f.close()


def read_file(file_path, num_of_words):
    with open(file_path, "r") as file:
        words = file.read().split()

        selected_words = random.sample(words, min(num_of_words, len(words)) )
        return selected_words
   

if __name__ == '__main__':
    if len(sys.argv) > 1:

        file = '/usr/share/dict/words'
        num_of_words = int(sys.argv[1])
        print(read_file(file, num_of_words))
    