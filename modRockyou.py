# Python3

'''Modifies rockyou.txt to certain amount of letters!!!'''

question = int(input("How many Letters?: "))
comparison = input("<, =, or >: ")
word_limit = question  # set the word limit to how long the words should be

basket = []
bigbasket = []

with open('rockyou.txt', errors="ignore") as f:
    # can modify the word limit to be <=, ==, or >=
    if comparison == '=':
        word_limit += 1
        for line in f:
            if len(line) == word_limit:
                basket.append(line)
    if comparison == '<':
        word_limit += 1
        for line in f:
            if len(line) <= word_limit:
                basket.append(line)
    if comparison == '>':
        word_limit += 1
        for line in f:
            if len(line) >= word_limit:
                basket.append(line)

for i in basket:
    bigbasket.append(i.strip())  # strips out newlines

word_limit -= 1
with open(f'modrockyou_with_{word_limit}words.txt', 'w') as n:
    for item in bigbasket:
        n.write(f'{item}\n')

print(f"Saved file as \'modrockyou_with_{word_limit}words.txt\'")
