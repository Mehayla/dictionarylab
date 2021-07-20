"""Restaurant rating lister."""

# opening the scores.txt file and attaching to variable
score_file = open('scores.txt')
# reads through the whole file
score_file = score_file.read()
res_dictionary = {}

def res_ratings(file):
    line = score_file.split('\n')

    for row in line:
        split_lines = row.split(':')
        key = split_lines[0]
        value = split_lines[1]
        res_dictionary[key] = value
    keys = res_dictionary.keys()
    sort_keys = sorted(keys)

    for key in sort_keys:
        print(f"{key} has a rating of {res_dictionary[key]}")
