# put your code here.
file = open('twain.txt')
count = {}

def word_count(file):
    for line in file:
        linelst = line.split()
        for word in linelst:
            word = word.lower()
            count[word] = count.get(word,0) + 1
    return count